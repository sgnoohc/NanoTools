#!/bin/bash

# slurm_packed_executable.sh
#
# Runs multiple sub-jobs in parallel within a single SLURM allocation.
# Each sub-job produces its own output file independently.
# Failed sub-jobs don't affect successful ones.
#
# Usage: ./slurm_packed_executable.sh manifest.tsv
#
# Manifest format (tab-separated):
#   TASK_NAME \t INDEX \t OUTPUTDIR OUTPUTNAME INPUTFILENAMES IFILE CMSSWVERSION SCRAMARCH EXTRAARGS...

MANIFEST=$(realpath $1)

MAX_RETRIES=6
RETRY_SLEEP=30
CPUS_PER_SUBJOB=${PACKED_CPUS_PER_SUBJOB:-1}

# Timer helper: prints "[packed][timer] <label> T=<elapsed>s at <timestamp>"
T0=$(date +%s)
timer() {
    local NOW=$(date +%s)
    local ELAPSED=$((NOW - T0))
    echo "[packed][timer] $1 T=${ELAPSED}s at $(date '+%H:%M:%S')"
}

# If a proxy file was staged into the working directory, use it
if [ -f x509up_proxy ] && [ -z "${X509_USER_PROXY}" ]; then
    export X509_USER_PROXY=$(pwd)/x509up_proxy
    echo "[packed] Using staged proxy: ${X509_USER_PROXY}"
fi

# Grid CA + VOMS dirs (matches the hpggsetup* aliases in ~/dot/mybashrc).
# Required for xrootd GSI server-cert verification — without these the new
# xrootd 5.x client falls back to ztn and fails "non-TLS" auth, killing xrdcp.
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir

timer "Script started"

echo -e "\n--- begin packed header ---\n"
echo "hostname: $(hostname)"
echo "uname -a: $(uname -a)"
echo "time: $(date +%s)"
echo "pwd: $(pwd)"
echo "df -h .: $(df -h . | tail -1)"
echo "manifest: ${MANIFEST}"
echo "cpus_per_subjob: ${CPUS_PER_SUBJOB}"
echo -e "\n--- end packed header ---\n"

# === Common CMSSW setup (done once) ===

# Read CMSSWVERSION and SCRAMARCH from first manifest line
FIRST_LINE=$(head -1 ${MANIFEST})
# Fields: TASK_NAME INDEX OUTPUTDIR OUTPUTNAME INPUTFILENAMES IFILE CMSSWVERSION SCRAMARCH EXTRAARGS...
CMSSWVERSION=$(echo "${FIRST_LINE}" | awk -F'\t' '{split($3, a, " "); print a[5]}')
SCRAMARCH=$(echo "${FIRST_LINE}" | awk -F'\t' '{split($3, a, " "); print a[6]}')

echo "[packed] CMSSWVERSION=${CMSSWVERSION}"
echo "[packed] SCRAMARCH=${SCRAMARCH}"

if [ -r "$OSGVO_CMSSW_Path"/cmsset_default.sh ]; then
    source "$OSGVO_CMSSW_Path"/cmsset_default.sh
elif [ -r "$OSG_APP"/cmssoft/cms/cmsset_default.sh ]; then
    source "$OSG_APP"/cmssoft/cms/cmsset_default.sh
elif [ -r /cvmfs/cms.cern.ch/cmsset_default.sh ]; then
    source /cvmfs/cms.cern.ch/cmsset_default.sh
else
    echo "ERROR! Couldn't find cmsset_default.sh"
    exit 1
fi

timer "CMSSW sourced"

export SCRAM_ARCH=${SCRAMARCH}

scramv1 project CMSSW $CMSSWVERSION
cd $CMSSWVERSION
eval $(scramv1 runtime -sh)

timer "CMSSW project setup done"

mv ../package.tar.gz package.tar.gz
tar xf package.tar.gz

timer "Package extracted"

cat gitversion.txt

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.

SETUP_DIR=$(pwd)
echo "[packed] SETUP_DIR=${SETUP_DIR}"

echo "ls -lrth of setup dir:"
ls -lrth
ls -lrth mc/ 2>/dev/null

echo -e "\n--- begin packed sub-jobs ---\n"

# === CPU profiler (background) ===
CPU_PROFILE="${SETUP_DIR}/cpu_profile.log"
(
    while true; do
        TS=$(date +%s)
        LOAD=$(cat /proc/loadavg | awk '{print $1}')
        NSKIM=$(pgrep -c skim 2>/dev/null || echo 0)
        CPU_LINE=$(top -bn1 2>/dev/null | grep "^%Cpu\|^Cpu" | head -1)
        echo "${TS} load=${LOAD} skim_procs=${NSKIM} ${CPU_LINE}"
        sleep 5
    done
) > ${CPU_PROFILE} 2>/dev/null &
PROFILER_PID=$!
echo "[packed] CPU profiler started (PID=${PROFILER_PID}), logging every 5s to cpu_profile.log"

timer "Launching sub-jobs"

# === Launch sub-jobs in parallel ===
PIDS=()
SUBJOB_LABELS=()

while IFS=$'\t' read -r TASK_NAME SUBJOB_INDEX SUBJOB_ARGS; do
    # Parse arguments from the third field (space-separated)
    read -r OUTPUTDIR OUTPUTNAME INPUTFILENAMES IFILE CMSSWVERSION_SUB SCRAMARCH_SUB EXTRAARGS <<< "${SUBJOB_ARGS}"

    LABEL="${TASK_NAME}__${SUBJOB_INDEX}"
    echo "[packed] Starting sub-job ${LABEL}: OUTPUTDIR=${OUTPUTDIR} OUTPUTNAME=${OUTPUTNAME} IFILE=${IFILE}"

    (
        # Sub-job timer (relative to script start)
        SUBJOB_T0=$(date +%s)
        subjob_timer() {
            local NOW=$(date +%s)
            local ELAPSED=$((NOW - T0))
            local SUBJOB_ELAPSED=$((NOW - SUBJOB_T0))
            echo "[packed][${LABEL}][timer] $1 T=${ELAPSED}s (subjob ${SUBJOB_ELAPSED}s) at $(date '+%H:%M:%S')"
        }

        # Each sub-job works in its own subdirectory
        SUBDIR="${SETUP_DIR}/subjob_${LABEL}"
        mkdir -p ${SUBDIR}
        cd ${SUBDIR}

        # Symlink shared binaries and resources from setup dir
        ln -s ${SETUP_DIR}/skim . 2>/dev/null
        for so in ${SETUP_DIR}/*.so; do
            [ -f "$so" ] && ln -s "$so" . 2>/dev/null
        done
        if [ -d ${SETUP_DIR}/mc ]; then
            ln -s ${SETUP_DIR}/mc . 2>/dev/null
        fi

        # Handle input files
        # Prepend xrootd redirector for /store paths
        if [[ ${INPUTFILENAMES} != /cmsuf/* ]]; then
            INPUTFILENAMES=${INPUTFILENAMES//\/store/root:\/\/cmsxrootd.fnal.gov\/\/store}
        fi

        if [[ ${INPUTFILENAMES} == /cmsuf/* ]]; then
            INPUTFILENAMES=${INPUTFILENAMES//,/ }
            subjob_timer "Input files ready (local)"
        else
            # xrdcp with retry
            LOCALINPUTFILENAMES=""
            for INPUTFILE in $(echo ${INPUTFILENAMES} | tr ',' ' '); do
                fulldest="${INPUTFILE/*\/store\//}"
                dest=$(dirname $fulldest)
                mkdir -p ${dest}
                XRDCP_STATUS=1
                for (( xrdcp_attempt=1; xrdcp_attempt<=MAX_RETRIES; xrdcp_attempt++ )); do
                    # Redirector fallback: FNAL (1-2) -> UNL (3) -> CMS Global (4-6)
                    if [ ${xrdcp_attempt} -le 2 ]; then
                        XRDCP_FILE=${INPUTFILE}
                    elif [ ${xrdcp_attempt} -eq 3 ]; then
                        XRDCP_FILE=${INPUTFILE//cmsxrootd.fnal.gov/xrootd.unl.edu}
                        echo "[packed][${LABEL}] Switching to UNL redirector"
                    else
                        XRDCP_FILE=${INPUTFILE//cmsxrootd.fnal.gov/cms-xrd-global.cern.ch}
                        [ ${xrdcp_attempt} -eq 4 ] && echo "[packed][${LABEL}] Switching to CMS global redirector"
                    fi
                    echo "[packed][${LABEL}] xrdcp attempt ${xrdcp_attempt}/${MAX_RETRIES}: ${XRDCP_FILE}"
                    xrdcp ${XRDCP_FILE} ${dest}
                    XRDCP_STATUS=$?
                    if [ ${XRDCP_STATUS} == 0 ]; then
                        break
                    fi
                    echo "[packed][${LABEL}] xrdcp failed (exit ${XRDCP_STATUS}), sleeping ${RETRY_SLEEP}s"
                    sleep ${RETRY_SLEEP}
                done
                if [ ${XRDCP_STATUS} != 0 ]; then
                    echo "[packed][${LABEL}] ERROR: xrdcp failed after ${MAX_RETRIES} attempts for ${INPUTFILE}"
                    exit 1
                fi
                if [ -z ${LOCALINPUTFILENAMES} ]; then
                    LOCALINPUTFILENAMES=${fulldest}
                else
                    LOCALINPUTFILENAMES=${LOCALINPUTFILENAMES}","${fulldest}
                fi
            done
            INPUTFILENAMES=${LOCALINPUTFILENAMES}
            INPUTFILENAMES=${INPUTFILENAMES//,/ }
            subjob_timer "Input files copied (xrdcp)"
        fi

        # Run skim (single worker per sub-job, using CPUS_PER_SUBJOB for internal parallelism)
        ALL_FILES=($INPUTFILENAMES)
        NFILES=${#ALL_FILES[@]}
        NPARALLEL=${CPUS_PER_SUBJOB}
        if [ ${NPARALLEL} -gt ${NFILES} ]; then
            NPARALLEL=${NFILES}
        fi

        echo "[packed][${LABEL}] Running ./skim: ${NFILES} files, NPARALLEL=${NPARALLEL}"

        if [ ${NPARALLEL} -le 1 ]; then
            # Single worker with retry
            for (( attempt=1; attempt<=MAX_RETRIES; attempt++ )); do
                echo "[packed][${LABEL}] Attempt ${attempt}/${MAX_RETRIES}: ./skim"
                echo ./skim $INPUTFILENAMES -n ${OUTPUTNAME} ${EXTRAARGS}
                ./skim $INPUTFILENAMES -n ${OUTPUTNAME} ${EXTRAARGS}
                RET=$?
                if [ ${RET} == 0 ]; then
                    break
                fi
                echo "[packed][${LABEL}] Failed (exit ${RET}), sleeping ${RETRY_SLEEP}s"
                sleep ${RETRY_SLEEP}
            done
            subjob_timer "Skim finished (single worker, exit ${RET})"
        else
            # Parallel workers within this sub-job
            SKIM_PIDS=()
            PART_NAMES=()
            FILES_PER_PART=$(( (NFILES + NPARALLEL - 1) / NPARALLEL ))

            for (( p=0; p<NPARALLEL; p++ )); do
                START=$(( p * FILES_PER_PART ))
                CHUNK=("${ALL_FILES[@]:${START}:${FILES_PER_PART}}")
                if [ ${#CHUNK[@]} -eq 0 ]; then
                    break
                fi
                PARTNAME="part${p}"
                PART_NAMES+=("${PARTNAME}")
                echo ./skim "${CHUNK[@]}" -n ${OUTPUTNAME}_${PARTNAME} ${EXTRAARGS} &
                ./skim "${CHUNK[@]}" -n ${OUTPUTNAME}_${PARTNAME} ${EXTRAARGS} &
                SKIM_PIDS+=($!)
            done

            # Wait and collect failed parts
            FAILED_PARTS=()
            for (( p=0; p<${#SKIM_PIDS[@]}; p++ )); do
                wait ${SKIM_PIDS[$p]}
                RETCODE=$?
                if [ ${RETCODE} != 0 ]; then
                    FAILED_PARTS+=($p)
                fi
            done

            subjob_timer "Skim parallel done (${#FAILED_PARTS[@]} failed parts)"

            # Retry failed parts sequentially
            for (( attempt=2; attempt<=MAX_RETRIES; attempt++ )); do
                if [ ${#FAILED_PARTS[@]} -eq 0 ]; then break; fi
                echo "[packed][${LABEL}] Retry attempt ${attempt}/${MAX_RETRIES} for ${#FAILED_PARTS[@]} failed part(s)"
                STILL_FAILED=()
                for p in "${FAILED_PARTS[@]}"; do
                    START=$(( p * FILES_PER_PART ))
                    CHUNK=("${ALL_FILES[@]:${START}:${FILES_PER_PART}}")
                    PARTNAME="part${p}"
                    echo ./skim "${CHUNK[@]}" -n ${OUTPUTNAME}_${PARTNAME} ${EXTRAARGS}
                    ./skim "${CHUNK[@]}" -n ${OUTPUTNAME}_${PARTNAME} ${EXTRAARGS}
                    RETCODE=$?
                    if [ ${RETCODE} != 0 ]; then
                        STILL_FAILED+=($p)
                    fi
                done
                FAILED_PARTS=("${STILL_FAILED[@]}")
                if [ ${#FAILED_PARTS[@]} -gt 0 ]; then
                    sleep ${RETRY_SLEEP}
                fi
            done

            RET=0
            if [ ${#FAILED_PARTS[@]} -gt 0 ]; then
                echo "[packed][${LABEL}] Parts still failing: ${FAILED_PARTS[*]}"
                RET=1
            fi

            # Merge partial outputs
            if [ ${RET} == 0 ]; then
                PART_ROOT_FILES=""
                for PARTNAME in "${PART_NAMES[@]}"; do
                    PART_ROOT_FILES="${PART_ROOT_FILES} ${OUTPUTNAME}_${PARTNAME}.root"
                done
                haddnano.py ${OUTPUTNAME}.root ${PART_ROOT_FILES}
                MERGE_RET=$?
                if [ ${MERGE_RET} != 0 ]; then
                    echo "[packed][${LABEL}] ERROR: haddnano.py failed"
                    rm -f ${OUTPUTNAME}.root ${PART_ROOT_FILES}
                    RET=1
                else
                    rm -f ${PART_ROOT_FILES}

                    # Merge cutflow CSV and cflow files from parallel parts
                    PART_NAMES_STR="${PART_NAMES[*]}"
                    python3 << MERGEEOF
import csv, os

def merge_csv(part_files, out):
    """Merge multiple Cutflow_TheEnd.csv files by summing numeric columns."""
    existing = [f for f in part_files if os.path.isfile(f)]
    if not existing:
        return
    if len(existing) == 1:
        os.rename(existing[0], out)
        return
    rows = {}
    order = []
    for path in existing:
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                cut = row["cut"]
                if cut not in rows:
                    rows[cut] = {"raw_events": 0.0, "weighted_events": 0.0}
                    order.append(cut)
                rows[cut]["raw_events"] += float(row["raw_events"])
                rows[cut]["weighted_events"] += float(row["weighted_events"])
    with open(out, "w") as f:
        f.write("cut,raw_events,weighted_events\n")
        for cut in order:
            r = rows[cut]
            f.write(f"{cut},{r['raw_events']:.6f},{r['weighted_events']:.6f}\n")
    for path in existing:
        os.remove(path)
    print(f"[packed][${LABEL}] Merged {len(existing)} cutflow CSVs -> {out}")

def merge_cflow(part_files, out):
    """Merge multiple .cflow files by summing columns 2-5."""
    existing = [f for f in part_files if os.path.isfile(f)]
    if not existing:
        return
    if len(existing) == 1:
        os.rename(existing[0], out)
        return
    rows = {}
    order = []
    for path in existing:
        with open(path) as f:
            for line in f:
                parts = line.strip().split(",")
                name = parts[0]
                nums = [float(x) for x in parts[1:5]]
                rest = parts[5:]
                if name not in rows:
                    rows[name] = [0.0]*4 + rest
                    order.append(name)
                for i in range(4):
                    rows[name][i] += nums[i]
    with open(out, "w") as f:
        for name in order:
            vals = rows[name]
            nums = [f"{int(v)}" for v in vals[:4]]
            f.write(",".join([name] + nums + vals[4:]) + "\n")
    for path in existing:
        os.remove(path)
    print(f"[packed][${LABEL}] Merged {len(existing)} cutflow cflows -> {out}")

part_names = "${PART_NAMES_STR}".split()
merge_csv(["${OUTPUTNAME}_" + p + "_Cutflow_TheEnd.csv" for p in part_names],
          "${OUTPUTNAME}_Cutflow_TheEnd.csv")
merge_cflow(["${OUTPUTNAME}_" + p + "_Cutflow.cflow" for p in part_names],
            "${OUTPUTNAME}_Cutflow.cflow")
MERGEEOF
                    subjob_timer "Merge done (haddnano + cutflow)"
                fi
            fi
        fi

        if [ ${RET} != 0 ]; then
            echo "[packed][${LABEL}] FAILED with exit code ${RET}"
            exit ${RET}
        fi

        # Sweeproot
        python3 -u << SWEEPEOF
import sys, os
try:
    import ROOT as r
except ImportError:
    print("[packed][${LABEL}][RSR] ERROR: cannot import ROOT, skipping sweeproot", file=sys.stderr)
    sys.exit(1)
foundBad = False
try:
    f1 = r.TFile("${OUTPUTNAME}.root")
    t = f1.Get("Events")
    nevts = t.GetEntries()
    for i in range(0, t.GetEntries(), 1):
        if t.GetEntry(i) < 0:
            foundBad = True
            print("[packed][${LABEL}][RSR] found bad event %i" % i)
            break
except: foundBad = True
if foundBad:
    print("[packed][${LABEL}][RSR] removing bad output")
    os.system("rm ${OUTPUTNAME}.root")
else:
    print("[packed][${LABEL}][RSR] passed sweeproot")
SWEEPEOF
        SWEEP_RET=$?
        if [ ${SWEEP_RET} != 0 ]; then
            echo "[packed][${LABEL}] WARNING: sweeproot failed (exit ${SWEEP_RET}), removing output as precaution"
            rm -f ${OUTPUTNAME}.root
        fi
        subjob_timer "Sweeproot done"

        # Runs summary (with retry)
        RUNS_MAX_RETRIES=3
        for (( runs_attempt=1; runs_attempt<=RUNS_MAX_RETRIES; runs_attempt++ )); do
            echo "[packed][${LABEL}] runs_summary attempt ${runs_attempt}/${RUNS_MAX_RETRIES}"
            rm -f runs_summary.json runs_summary.tmp.json
            python3 -u << RUNSEOF
import sys
try:
    import ROOT as r
except ImportError:
    print("[packed][${LABEL}][runs] ERROR: cannot import ROOT, skipping runs_summary", file=sys.stderr)
    sys.exit(1)
import json, os

fname = "${OUTPUTNAME}.root"
out = {}

if os.path.isfile(fname):
    f = r.TFile.Open(fname)

    # Get total events from Events tree
    events_tree = f.Get("Events")
    if events_tree:
        out["eventCount"] = int(events_tree.GetEntries())

    # MC: summarize GenWeights from Runs TTree
    t = f.Get("Runs")
    if t and t.GetBranch("genEventCount"):
        scalars = {"genEventCount": 0, "genEventSumw": 0.0, "genEventSumw2": 0.0}
        arrays = {}
        for i in range(t.GetEntries()):
            t.GetEntry(i)
            for k in scalars:
                scalars[k] += getattr(t, k)
            if i == 0:
                for bname in ["LHEScaleSumw", "LHEPdfSumw", "PSSumw"]:
                    br = t.GetBranch(bname)
                    if br:
                        n = getattr(t, "n" + bname)
                        arrays[bname] = [0.0] * n
            for bname, sums in arrays.items():
                vals = getattr(t, bname)
                for j in range(len(sums)):
                    sums[j] += vals[j]
        out.update(scalars)
        out.update(arrays)

    f.Close()

if out:
    # Ensure all values are JSON-serializable (convert ROOT types)
    for k, v in out.items():
        if isinstance(v, list):
            out[k] = [float(x) for x in v]
        elif isinstance(v, float) or hasattr(v, '__float__'):
            out[k] = float(v)
        elif isinstance(v, int) or hasattr(v, '__int__'):
            out[k] = int(v)
    try:
        with open("runs_summary.tmp.json", "w") as jf:
            json.dump(out, jf, indent=2)
        os.rename("runs_summary.tmp.json", "runs_summary.json")
    except Exception as e:
        print("[packed][${LABEL}][runs] ERROR: failed to write JSON:", e, file=sys.stderr)
        if os.path.exists("runs_summary.tmp.json"):
            os.remove("runs_summary.tmp.json")
    if "genEventCount" in out:
        print("[packed][${LABEL}][runs] genEventCount:", out["genEventCount"])
    print("[packed][${LABEL}][runs] eventCount:", out.get("eventCount"))
RUNSEOF
            RUNS_RET=$?
            if [ ${RUNS_RET} != 0 ]; then
                echo "[packed][${LABEL}] WARNING: runs_summary failed (exit ${RUNS_RET})"
            fi
            # Validate runs_summary.json if it exists
            if [ -f "runs_summary.json" ]; then
                if [ ! -s "runs_summary.json" ]; then
                    echo "[packed][${LABEL}] WARNING: runs_summary.json is empty (0 bytes), removing"
                    rm -f runs_summary.json
                else
                    python3 -c "import json; json.load(open('runs_summary.json'))" 2>/dev/null
                    if [ $? != 0 ]; then
                        echo "[packed][${LABEL}] WARNING: runs_summary.json is invalid JSON, removing"
                        rm -f runs_summary.json
                    fi
                fi
            fi
            # If valid JSON exists, we're done
            if [ -f "runs_summary.json" ]; then
                echo "[packed][${LABEL}] runs_summary.json OK (attempt ${runs_attempt})"
                break
            fi
            # Retry unless last attempt
            if [ ${runs_attempt} -lt ${RUNS_MAX_RETRIES} ]; then
                echo "[packed][${LABEL}] Retrying runs_summary in 5s..."
                sleep 5
            else
                echo "[packed][${LABEL}] WARNING: runs_summary failed after ${RUNS_MAX_RETRIES} attempts, no runs_summary.json will be produced"
            fi
        done
        subjob_timer "Runs summary done"

        # Copy output to destination
        if [ -f "${OUTPUTNAME}.root" ]; then
            if [[ $(hostname) == *"ufhpc"* ]]; then
                COPY_DEST_DIR="${OUTPUTDIR}"
                mkdir -p ${COPY_DEST_DIR}
                cp ${OUTPUTNAME}.root ${COPY_DEST_DIR}/${OUTPUTNAME}_${IFILE}.root
                COPY_STATUS=$?
                if [[ $COPY_STATUS != 0 ]]; then
                    echo "[packed][${LABEL}] ERROR: cp failed with exit code $COPY_STATUS"
                    exit 1
                fi
                # Copy cutflow/runs files if they exist
                [ -f "cutflow.txt" ] && cp cutflow.txt ${COPY_DEST_DIR}/cutflow_${IFILE}.txt
                [ -f "${OUTPUTNAME}_Cutflow.cflow" ] && cp ${OUTPUTNAME}_Cutflow.cflow ${COPY_DEST_DIR}/cutflow_${IFILE}.cflow
                [ -f "${OUTPUTNAME}_Cutflow_TheEnd.csv" ] && cp ${OUTPUTNAME}_Cutflow_TheEnd.csv ${COPY_DEST_DIR}/cutflow_${IFILE}.csv
                [ -f "runs_summary.json" ] && cp runs_summary.json ${COPY_DEST_DIR}/runs_summary_${IFILE}.json
                echo "[packed][${LABEL}] Output copied to ${COPY_DEST_DIR}"
            else
                OUTPUTDIRPATHNEW=$(echo ${OUTPUTDIR} | sed 's/^.*\(\/store.*\).*$/\1/')
                COPY_SRC="file://$(pwd)/${OUTPUTNAME}.root"
                COPY_DEST="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/${OUTPUTNAME}_${IFILE}.root"
                env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC} ${COPY_DEST}
                COPY_STATUS=$?
                if [[ $COPY_STATUS != 0 ]]; then
                    echo "[packed][${LABEL}] ERROR: gfal-copy failed with exit code $COPY_STATUS"
                    exit 1
                fi
                echo "[packed][${LABEL}] Output copied via gfal-copy"
            fi
            subjob_timer "Output copy done"
        else
            echo "[packed][${LABEL}] No output file produced (sweeproot removed it?)"
            exit 1
        fi

        subjob_timer "Sub-job complete"
        echo "[packed][${LABEL}] SUCCESS"
        exit 0

    ) &
    PIDS+=($!)
    SUBJOB_LABELS+=("${LABEL}")

done < ${MANIFEST}

timer "All ${#PIDS[@]} sub-jobs launched"

echo -e "\n--- waiting for ${#PIDS[@]} sub-jobs ---\n"

# === Wait for all sub-jobs and report ===
FAILED=0
SUCCEEDED=0
for i in "${!PIDS[@]}"; do
    wait ${PIDS[$i]}
    RET=$?
    if [ ${RET} != 0 ]; then
        echo "[packed] FAILED: ${SUBJOB_LABELS[$i]} (exit ${RET})"
        FAILED=$((FAILED + 1))
    else
        echo "[packed] SUCCESS: ${SUBJOB_LABELS[$i]}"
        SUCCEEDED=$((SUCCEEDED + 1))
    fi
done

timer "All sub-jobs finished"

echo -e "\n--- packed summary ---"
echo "[packed] Total: ${#PIDS[@]}, Succeeded: ${SUCCEEDED}, Failed: ${FAILED}"

# Stop CPU profiler and dump results
kill ${PROFILER_PID} 2>/dev/null
wait ${PROFILER_PID} 2>/dev/null
echo -e "\n--- CPU profile ---"
if [ -f ${CPU_PROFILE} ]; then
    cat ${CPU_PROFILE}
fi
echo "--- end CPU profile ---"

timer "Script finished"
echo "--- end packed ---\n"

# Exit 0 even if some sub-jobs failed — completion is tracked per output file
exit 0
