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

if [[ ${INPUTFILENAMES} != /cmsuf/* ]]; then
    INPUTFILENAMES=${INPUTFILENAMES//\/store/root:\/\/cmsxrootd.fnal.gov\/\/store}
fi

# Make sure OUTPUTNAME doesn't have .root since we add it manually
OUTPUTNAME=$(echo $OUTPUTNAME | sed 's/\.root//')

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
elif [[ ${INPUTFILENAMES} == /cmsuf/* ]]; then
    # Local files on shared filesystem — just convert commas to spaces
    INPUTFILENAMES=${INPUTFILENAMES//,/ }
    echo "Using local files (no xrdcp needed): ${INPUTFILENAMES}"
else
    ##########################################################
    #UNCOMMENT TO COPY FAILING FILES DIRECTLY TO CONDOR NODE
    echo "Before XRootD copy"
    echo INPUTFILENAMES=${INPUTFILENAMES}
    LOCALINPUTFILENAMES=""
    for INPUTFILE in $(echo ${INPUTFILENAMES} | tr ',' ' '); do
        fulldest="${INPUTFILE/*\/store\//}"
        dest=$(dirname $fulldest)
        mkdir -p ${dest}
        echo ${dest}
        echo xrdcp ${INPUTFILE} ${dest}
        xrdcp ${INPUTFILE} ${dest}
        XRDCP_STATUS=$?
        if [ ${XRDCP_STATUS} != 0 ]; then
            echo "ERROR: xrdcp failed with exit code ${XRDCP_STATUS} for ${INPUTFILE}"
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

# Split input files into an array
ALL_FILES=($INPUTFILENAMES)
NFILES=${#ALL_FILES[@]}
echo "[parallel] Total input files: ${NFILES}"

if [ ${NFILES} -le 1 ]; then
    # Single file (or zero): run one ./skim as normal
    echo Executing ./skim $INPUTFILENAMES -n ${OUTPUTNAME} ${EXTRAARGS}
    ./skim $INPUTFILENAMES -n ${OUTPUTNAME} ${EXTRAARGS}
    RET=$?
else
    # Split files into two halves
    HALF=$(( (NFILES + 1) / 2 ))
    FILES_A=("${ALL_FILES[@]:0:${HALF}}")
    FILES_B=("${ALL_FILES[@]:${HALF}}")

    echo "[parallel] Part A (${#FILES_A[@]} files): ${FILES_A[*]}"
    echo "[parallel] Part B (${#FILES_B[@]} files): ${FILES_B[*]}"

    # Run two ./skim processes in parallel
    echo Executing ./skim "${FILES_A[@]}" -n ${OUTPUTNAME}_partA ${EXTRAARGS}
    ./skim "${FILES_A[@]}" -n ${OUTPUTNAME}_partA ${EXTRAARGS} &
    PID_A=$!

    echo Executing ./skim "${FILES_B[@]}" -n ${OUTPUTNAME}_partB ${EXTRAARGS}
    ./skim "${FILES_B[@]}" -n ${OUTPUTNAME}_partB ${EXTRAARGS} &
    PID_B=$!

    wait $PID_A
    RET_A=$?
    wait $PID_B
    RET_B=$?

    echo "[parallel] Part A exit code: ${RET_A}"
    echo "[parallel] Part B exit code: ${RET_B}"

    # Check both exit codes
    if [ ${RET_A} != 0 ] || [ ${RET_B} != 0 ]; then
        RET=1
        if [[ "${EXTRAARGS}" = *"ignorebadfiles"* ]]; then
            echo "[parallel] Ignoring exit codes (ignorebadfiles)"
            RET=0
        fi
    else
        RET=0
    fi

    # Merge partial outputs with haddnano.py
    if [ ${RET} == 0 ]; then
        echo "[parallel] Merging with haddnano.py"
        echo "Running: haddnano.py ${OUTPUTNAME}.root ${OUTPUTNAME}_partA.root ${OUTPUTNAME}_partB.root"
        haddnano.py ${OUTPUTNAME}.root ${OUTPUTNAME}_partA.root ${OUTPUTNAME}_partB.root
        MERGE_RET=$?
        if [ ${MERGE_RET} != 0 ]; then
            echo "ERROR: haddnano.py failed with exit code ${MERGE_RET}"
            rm -f ${OUTPUTNAME}.root ${OUTPUTNAME}_partA.root ${OUTPUTNAME}_partB.root
            exit 1
        fi
        # Clean up partial files
        rm -f ${OUTPUTNAME}_partA.root ${OUTPUTNAME}_partB.root
        echo "[parallel] Merge complete, cleaned up partial files"
    fi
fi

echo "after running: ls -lrth"
ls -lrth

if [ ${RET} != 0 ]; then
    if [[ "${EXTRAARGS}" = *"ignorebadfiles"* ]]; then
        echo "Ignoring exit code of ${RET}"
    else
        echo "Removing output file because ./skim returned exit code ${RET}"
        rm -f ${OUTPUTNAME}.root
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
    if [ -f "output_Cutflow.cflow" ]; then
        cp output_Cutflow.cflow ${COPY_DEST_DIR}/cutflow_${IFILE}.cflow
    fi
    if [ -f "output_Cutflow_TheEnd.csv" ]; then
        cp output_Cutflow_TheEnd.csv ${COPY_DEST_DIR}/cutflow_${IFILE}.csv
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

    echo "Sending output file output/output_Cutflow.cflow if it exists"
    COPY_SRC_CUTFLOW="file://`pwd`/output_Cutflow.cflow"
    COPY_DEST_CUTFLOW="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/cutflow_${IFILE}.cflow"
    if [ -f "$(pwd)/output_Cutflow.cflow" ]; then
        echo "Running: env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}
    else
        echo "Warning: gfal-ls command failed or file  '$COPY_SRC_CUTFLOW' does not exist:"
    fi

    echo "Sending output file output/output_Cutflow*.csv if it exists"
    COPY_SRC_CUTFLOW="file://`pwd`/output_Cutflow_TheEnd.csv"
    COPY_DEST_CUTFLOW="davs://redirector.t2.ucsd.edu:1095//${OUTPUTDIRPATHNEW}/cutflow_${IFILE}.csv"
    if [ -f "$(pwd)/output_Cutflow_TheEnd.csv" ]; then
        echo "Running: env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}"
        env -i X509_USER_PROXY=${X509_USER_PROXY} gfal-copy -p -f -t 4200 --verbose --checksum ADLER32 ${COPY_SRC_CUTFLOW} ${COPY_DEST_CUTFLOW}
    else
        echo "Warning: gfal-ls command failed or file  '$COPY_SRC_CUTFLOW' does not exist:"
    fi
fi
