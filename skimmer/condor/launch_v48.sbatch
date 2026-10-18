#!/bin/bash
#SBATCH --job-name=v48_launch
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=12G
#SBATCH --time=96:00:00
#SBATCH --output=logs_v48/submit_v48.log
#SBATCH --error=logs_v48/submit_v48.log

# v48: full self-contained 4LepLoose campaign for the ZZZ analysis.
#   MC   = the group set that reproduces (and supersets) the v30 4Lep list
#   Data = Run2 + Run3 2022-2025 + Run3 2026, all into one Run3_Data directory
# Runs on a compute node, never a login node.

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
export X509_USER_PROXY=$HOME/private/x509_proxy
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir

MC2="run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_zz4l"
MC3="run3_bkg,run3_bkg_hh,run3_bkg_ggzz4l,run3_bkg_hh_bbtautau,run3_bkg_zh4l"
DATA="run2_data,run3_data,run3_data_2026"
ALL="${MC2},${MC3},${DATA}"

echo "host=$(hostname)  start=$(date)"
echo "=== GATE: dry run ==="
python3 -u submit.py --samples "${ALL}" --version v48 --channels 4LepLoose \
    --pack-size 6 --dry-run > logs_v48/dryrun_v48.log 2>&1
rc=$?
echo "dry-run rc=${rc}"
grep -E "^=== Group" logs_v48/dryrun_v48.log
echo "  datasets: $(grep -c '^  --- /' logs_v48/dryrun_v48.log)"
if [ "$rc" -ne 0 ]; then
    echo "DRY RUN FAILED -- refusing to submit"
    grep -A6 Traceback logs_v48/dryrun_v48.log | head -12
    exit 1
fi

echo "=== REAL SUBMISSION ==="
python3 -u submit.py --samples "${ALL}" --version v48 --channels 4LepLoose \
    --pack-size 6 --cpus-per-subjob 1
echo "V48_RC=$?  end=$(date)"
