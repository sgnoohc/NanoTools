#!/bin/bash

OUTPUTDIR=$1
OUTPUTNAME=$2
INPUTFILENAMES=$3
IFILE=$4
CMSSWVERSION=$5
SCRAMARCH=$6
shift 6
CMDLINE_EXTRAARGS="$@"

# If a proxy file was staged into the working directory (e.g. by SLURM wrapper), use it
if [ -f x509up_proxy ] && [ -z "${X509_USER_PROXY}" ]; then
    export X509_USER_PROXY=$(pwd)/x509up_proxy
    echo "[proxy] Using staged proxy: ${X509_USER_PROXY}"
fi

function getjobad {
    grep -i "^$1" "$_CONDOR_JOB_AD" | cut -d= -f2- | xargs echo
}
function setup_chirp {
    if [ -e ./condor_chirp ]; then
    # Note, in the home directory
        mkdir chirpdir
        mv condor_chirp chirpdir/
        export PATH="$PATH:$(pwd)/chirpdir"
        echo "[chirp] Found and put condor_chirp into $(pwd)/chirpdir"
    elif [ -e /usr/libexec/condor/condor_chirp ]; then
        export PATH="$PATH:/usr/libexec/condor"
        echo "[chirp] Found condor_chirp in /usr/libexec/condor"
    else
        echo "[chirp] No condor_chirp :("
    fi
}
function chirp {
    # Note, $1 (the classad name) must start with Chirp
    condor_chirp set_job_attr_delayed $1 $2
    ret=$?
    echo "[chirp] Chirped $1 => $2 with exit code $ret"
}

INPUTFILENAMES=${INPUTFILENAMES//\/store/root:\/\/cmsxrootd.fnal.gov\/\/store}
# if [[ ${INPUTFILENAMES} == *"Run201"* ]]; then
#     INPUTFILENAMES=${INPUTFILENAMES//\/store/root:\/\/cmsxrootd.fnal.gov\/\/store}
# elif [[ ${INPUTFILENAMES} == *"ULSignalSamples"* ]]; then
#     INPUTFILENAMES=${INPUTFILENAMES//\/ceph\/cms\/store/root:\/\/redirector.t2.ucsd.edu:1095\/\/store}
# else
#     INPUTFILENAMES=${INPUTFILENAMES//\/store/root:\/\/cmseos.fnal.gov\/\/store\/group\/lpcvvv\/NanoAODv9\/store}
# fi

# Make sure OUTPUTNAME doesn't have .root since we add it manually
OUTPUTNAME=$(echo $OUTPUTNAME | sed 's/\.root//')

###UNCOMMENT TO COPY FAILING FILES DIRECTLY TO CONDOR NODE
#input=$(echo "${INPUTFILENAMES}" | sed 's/^.*\(\/store.*\).*$/\1/')
#dest="${input/\/store\//}"
#dest=$(dirname $dest)
#mkdir -p $dest
#xrdcp root://cms-xrd-global.cern.ch/$input $dest
#localpath=$(echo ${INPUTFILENAMES} | sed 's/^.*\(\/store.*\).*$/\1/')
#localpath="${localpath/\/store\//}"
#INPUTFILE=${localpath}

setup_chirp

echo -e "\n--- begin header output ---\n" #                     <----- section division
echo "OUTPUTDIR: $OUTPUTDIR"
echo "OUTPUTNAME: $OUTPUTNAME"
echo "INPUTFILENAMES: $INPUTFILENAMES"
echo "IFILE: $IFILE"
echo "CMSSWVERSION: $CMSSWVERSION"
echo "SCRAMARCH: $SCRAMARCH"

echo "GLIDEIN_CMSSite: $GLIDEIN_CMSSite"
echo "hostname: $(hostname)"
echo "uname -a: $(uname -a)"
echo "time: $(date +%s)"
echo "args: $@"

echo -e "\n--- end header output ---\n" #                       <----- section division

if [ -r "$OSGVO_CMSSW_Path"/cmsset_default.sh ]; then
    echo "sourcing environment: source $OSGVO_CMSSW_Path/cmsset_default.sh"
    source "$OSGVO_CMSSW_Path"/cmsset_default.sh
elif [ -r "$OSG_APP"/cmssoft/cms/cmsset_default.sh ]; then
    echo "sourcing environment: source $OSG_APP/cmssoft/cms/cmsset_default.sh"
    source "$OSG_APP"/cmssoft/cms/cmsset_default.sh
elif [ -r /cvmfs/cms.cern.ch/cmsset_default.sh ]; then
    echo "sourcing environment: source /cvmfs/cms.cern.ch/cmsset_default.sh"
    source /cvmfs/cms.cern.ch/cmsset_default.sh
else
    echo "ERROR! Couldn't find $OSGVO_CMSSW_Path/cmsset_default.sh or /cvmfs/cms.cern.ch/cmsset_default.sh or $OSG_APP/cmssoft/cms/cmsset_default.sh"
    exit 1
fi

export SCRAM_ARCH=${SCRAMARCH}

scramv1 project CMSSW $CMSSWVERSION
cd $CMSSWVERSION
eval $(scramv1 runtime -sh)
mv ../package.tar.gz package.tar.gz
tar xf package.tar.gz

if [[ ${INPUTFILENAMES} == *"ULSignalSamples"* ]]; then
    :
else
    ##########################################################
    #UNCOMMENT TO COPY FAILING FILES DIRECTLY TO CONDOR NODE
    MAX_RETRIES=6
    RETRY_SLEEP=30
    echo "Before XRootD copy"
    echo INPUTFILENAMES=${INPUTFILENAMES}
    LOCALINPUTFILENAMES=""
    for INPUTFILE in $(echo ${INPUTFILENAMES} | tr ',' ' '); do
        fulldest="${INPUTFILE/*\/store\//}"
        dest=$(dirname $fulldest)
        mkdir -p ${dest}
        echo ${dest}
        XRDCP_STATUS=1
        for (( xrdcp_attempt=1; xrdcp_attempt<=MAX_RETRIES; xrdcp_attempt++ )); do
            # Redirector fallback: FNAL (1-2) -> UNL (3) -> CMS Global (4-6)
            if [ ${xrdcp_attempt} -le 2 ]; then
                XRDCP_FILE=${INPUTFILE}
            elif [ ${xrdcp_attempt} -eq 3 ]; then
                XRDCP_FILE=${INPUTFILE//cmsxrootd.fnal.gov/xrootd.unl.edu}
                echo "[xrdcp] Switching to UNL redirector"
            else
                XRDCP_FILE=${INPUTFILE//cmsxrootd.fnal.gov/cms-xrd-global.cern.ch}
                [ ${xrdcp_attempt} -eq 4 ] && echo "[xrdcp] Switching to CMS global redirector"
            fi
            echo "[xrdcp] Attempt ${xrdcp_attempt}/${MAX_RETRIES}: xrdcp ${XRDCP_FILE} ${dest}"
            xrdcp ${XRDCP_FILE} ${dest}
            XRDCP_STATUS=$?
            if [ ${XRDCP_STATUS} == 0 ]; then
                break
            fi
            echo "[xrdcp] Failed (exit ${XRDCP_STATUS}), sleeping ${RETRY_SLEEP}s"
            sleep ${RETRY_SLEEP}
        done
        if [ ${XRDCP_STATUS} != 0 ]; then
            echo "ERROR: xrdcp failed after ${MAX_RETRIES} attempts for ${INPUTFILE}"
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
    echo "After XRootD copy"
    echo INPUTFILENAMES=${INPUTFILENAMES}
    ##########################################################
fi

cat gitversion.txt

# need this to find the .so files, even though they are in the same
# directory
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.

echo "before running: ls -lrth"
ls -lrth 
ls -lrth mc/

echo -e "\n--- begin running ---\n" #                           <----- section division

EXTRAARGS="$(getjobad metis_extraargs)"
# If running under SLURM (no condor classad), use command-line extra args
if [ -z "${EXTRAARGS}" ] && [ -n "${CMDLINE_EXTRAARGS}" ]; then
    EXTRAARGS="${CMDLINE_EXTRAARGS}"
fi
# if [[ $(hostname) == *"t2.ucsd.edu"* ]] && [[ $INPUTFILENAMES == *"/hadoop"* ]]; then
#     : # Don't need to do anything
# else
#     INPUTFILENAMES=${INPUTFILENAMES/\/store/root:\/\/cmsxrootd.fnal.gov\/\/store}
# fi
echo Executing ./skim $INPUTFILENAMES -n ${OUTPUTNAME} ${EXTRAARGS}
./skim $INPUTFILENAMES -n ${OUTPUTNAME} ${EXTRAARGS}
RET=$?

echo "after running: ls -lrth"
ls -lrth

if [ ${RET} != 0 ]; then
    if [[ "${EXTRAARGS}" = *"ignorebadfiles"* ]]; then
        echo "Ignoring exit code of ${RET}"
    else
        echo "Removing output file because ./skim returned exit code ${RET}"
        rm ${OUTPUTNAME}.root
        exit 1 # Added because otherwise condor does not know job failed?
    fi
fi

# Rigorous sweeproot which checks ALL branches for ALL events.
# If GetEntry() returns -1, then there was an I/O problem, so we will delete it
python3 << EOL
import ROOT as r
import os
foundBad = False
try:
    f1 = r.TFile("${OUTPUTNAME}.root")
    t = f1.Get("Events")
    nevts = t.GetEntries()
    for i in range(0,t.GetEntries(),1):
        if t.GetEntry(i) < 0:
            foundBad = True
            print("[RSR] found bad event %i" % i)
            break
except: foundBad = True
if foundBad:
    print("[RSR] removing output file because it does not deserve to live")
    os.system("rm ${OUTPUTNAME}.root")
else: print("[RSR] passed the rigorous sweeproot")
EOL

echo -e "\n--- end running ---\n" #                             <----- section division

echo "after running: ls -lrth"
ls -lrth

# Summarize Runs TTree (GenWeights) into JSON
echo -e "\n--- begin runs summary ---\n"
python3 << RUNSEOF
import ROOT as r
import json, os

fname = "${OUTPUTNAME}.root"
out = {}

if os.path.isfile(fname):
    f = r.TFile.Open(fname)
    t = f.Get("Runs")
    if t:
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
    else:
        print("[runs] WARNING: No Runs TTree found")
else:
    print("[runs] WARNING: Output file not found, skipping runs summary")

if out:
    with open("runs_summary.json", "w") as jf:
        json.dump(out, jf, indent=2)
    print("[runs] Wrote runs_summary.json")
    print("[runs] genEventCount:", out.get("genEventCount"))
    print("[runs] genEventSumw:", out.get("genEventSumw"))
else:
    print("[runs] No data to write")
RUNSEOF
echo -e "\n--- end runs summary ---\n"

if [[ $(hostname) == *"ufhpc"* ]]; then
    echo -e "\n--- begin copying output (HiPerGator shared filesystem) ---\n"
    COPY_DEST_DIR="${OUTPUTDIR}"
    COPY_DEST="${COPY_DEST_DIR}/${OUTPUTNAME}_${IFILE}.root"
    echo "Running: mkdir -p ${COPY_DEST_DIR}"
    mkdir -p ${COPY_DEST_DIR}
    echo "Running: cp ${OUTPUTNAME}.root ${COPY_DEST}"
    cp ${OUTPUTNAME}.root ${COPY_DEST}
    COPY_STATUS=$?
    if [[ $COPY_STATUS == 0 ]]; then
        echo "Copy success!"
    else
        echo "ERROR: Copy failed with exit code $COPY_STATUS"
        exit 1
    fi
    # Copy cutflow files if they exist
    if [ -f "cutflow.txt" ]; then
        cp cutflow.txt ${COPY_DEST_DIR}/cutflow_${IFILE}.txt
    fi
    if [ -f "${OUTPUTNAME}_Cutflow.cflow" ]; then
        cp ${OUTPUTNAME}_Cutflow.cflow ${COPY_DEST_DIR}/cutflow_${IFILE}.cflow
    fi
    if [ -f "${OUTPUTNAME}_Cutflow_TheEnd.csv" ]; then
        cp ${OUTPUTNAME}_Cutflow_TheEnd.csv ${COPY_DEST_DIR}/cutflow_${IFILE}.csv
    fi
    if [ -f "runs_summary.json" ]; then
        cp runs_summary.json ${COPY_DEST_DIR}/runs_summary_${IFILE}.json
    fi
elif [[ $(hostname) == *"uaf-10"* ]]; then
    echo -e "\n--- begin copying output ---\n" #                    <----- section division
    echo "Sending output file output/${OUTPUTNAME}.root"
    OUTPUTDIRPATHNEW=$(echo ${OUTPUTDIR} | sed 's/^.*\(\/store.*\).*$/\1/')
    COPY_SRC="output/${OUTPUTNAME}.root"
    COPY_DEST_DIR="/ceph/cms/${OUTPUTDIRPATHNEW}/"
    COPY_DEST="${COPY_DEST_DIR}/${OUTPUTNAME}_${IFILE}.root"
    echo "Running: mkdir -p ${COPY_DEST_DIR}"
    mkdir -p ${COPY_DEST_DIR}
    echo "Running: cp ${COPY_SRC} ${COPY_DEST}"
    cp ${COPY_SRC} ${COPY_DEST}
    COPY_STATUS=$?
    if [[ $COPY_STATUS == 0 ]]; then
        echo "Copy success!"
    fi
else
    echo -e "\n--- begin copying output ---\n" #                    <----- section division
    # copy output.root file
    echo "Sending output file output/${OUTPUTNAME}.root"
    OUTPUTDIRPATHNEW=$(echo ${OUTPUTDIR} | sed 's/^.*\(\/store.*\).*$/\1/')
    COPY_SRC="file://`pwd`/${OUTPUTNAME}.root"
    COPY_DEST="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/${OUTPUTNAME}_${IFILE}.root"
    
    echo "Running: env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC} ${COPY_DEST}"
    env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC} ${COPY_DEST}
    COPY_STATUS=$?

    if [[ $COPY_STATUS != 0 ]]; then
        echo "Removing output file because gfal-copy crashed with code $COPY_STATUS"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-rm --verbose ${COPY_DEST}
        REMOVE_STATUS=$?
        if [[ $REMOVE_STATUS != 0 ]]; then
            echo "Uhh, gfal-copy crashed and then the gfal-rm also crashed with code $REMOVE_STATUS"
        fi
        exit 1
    fi

    # copy cuflow.txt file if it exists
    echo "Sending output file output/cutflow.txt if it exists"
    COPY_SRC_CUTFLOW="file://`pwd`/cutflow.txt"
    COPY_DEST_CUTFLOW="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/cutflow_${IFILE}.txt"
    if [ -f "$(pwd)/cutflow.txt" ]; then
        echo "Running: env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}
    else
        echo "Warning: gfal-ls command failed or file  '$COPY_SRC_CUTFLOW' does not exist:"
    fi
    
    echo "Sending output file ${OUTPUTNAME}_Cutflow.cflow if it exists"
    COPY_SRC_CUTFLOW="file://`pwd`/${OUTPUTNAME}_Cutflow.cflow"
    COPY_DEST_CUTFLOW="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/cutflow_${IFILE}.cflow"
    if [ -f "$(pwd)/${OUTPUTNAME}_Cutflow.cflow" ]; then
        echo "Running: env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}
    else
        echo "Warning: file '${OUTPUTNAME}_Cutflow.cflow' does not exist"
    fi

    echo "Sending output file ${OUTPUTNAME}_Cutflow_TheEnd.csv if it exists"
    COPY_SRC_CUTFLOW="file://`pwd`/${OUTPUTNAME}_Cutflow_TheEnd.csv"
    COPY_DEST_CUTFLOW="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/cutflow_${IFILE}.csv"
    if [ -f "$(pwd)/${OUTPUTNAME}_Cutflow_TheEnd.csv" ]; then
        echo "Running: env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}
    else
        echo "Warning: file '${OUTPUTNAME}_Cutflow_TheEnd.csv' does not exist"
    fi

    echo "Sending output file runs_summary.json if it exists"
    COPY_SRC_RUNS="file://$(pwd)/runs_summary.json"
    COPY_DEST_RUNS="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/runs_summary_${IFILE}.json"
    if [ -f "$(pwd)/runs_summary.json" ]; then
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_RUNS} ${COPY_DEST_RUNS}
    fi
fi
