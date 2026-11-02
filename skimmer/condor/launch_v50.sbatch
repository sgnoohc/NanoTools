#!/bin/bash
#SBATCH --job-name=v50_launch
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=48:00:00
#SBATCH --output=logs_v50/submit_v50.log
#SBATCH --error=logs_v50/submit_v50.log

# v50: run2_bkg_zh4l (Run2 UL16APV/UL16/UL17/UL18 ZH_HToZZ_4LFilter, the Run2
# counterpart of run3_bkg_zh4l) x 4LepLooseNoLH only -- the loosest 4L skim
# (v49 channel). Runs on a compute node, never a login node.

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
export X509_USER_PROXY=$HOME/private/x509_proxy
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir

SAMPLES="run2_bkg_zh4l"

echo "host=$(hostname)  start=$(date)"
echo "=== GATE: dry run ==="
python3 -u submit.py --samples "${SAMPLES}" --version v50 --channels 4LepLooseNoLH \
    --pack-size 6 --dry-run > logs_v50/dryrun_gate_v50.log 2>&1
rc=$?
echo "dry-run rc=${rc}"
grep -E "^=== Group" logs_v50/dryrun_gate_v50.log
echo "  datasets: $(grep -c '^  --- /' logs_v50/dryrun_gate_v50.log)"
if [ "$rc" -ne 0 ]; then
    echo "DRY RUN FAILED -- refusing to submit"
    grep -A6 Traceback logs_v50/dryrun_gate_v50.log | head -12
    exit 1
fi

echo "=== REAL SUBMISSION ==="
python3 -u submit.py --samples "${SAMPLES}" --version v50 --channels 4LepLooseNoLH \
    --pack-size 6 --cpus-per-subjob 1
echo "V50_RC=$?  end=$(date)"
