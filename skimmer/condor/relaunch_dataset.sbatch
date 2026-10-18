#!/bin/bash
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=24:00:00

# Re-drive ONE dataset of an existing v48-style campaign, e.g. after its task
# dir was removed so that it picks up a new tarball (task dirs bake their own).
# Submit under the campaign's driver job name so its waiter's
# `scancel --name=<ver>_launch` still finds it:
#
#   sbatch -J v48_launch -o logs_v48/relaunch_%j.log relaunch_dataset.sbatch \
#       v48 4LepLoose '^/Muon1/Run2025B-PromptReco-v1/NANOAOD$'
VER=$1; CHAN=$2; MATCH=$3
[ -n "$VER" ] && [ -n "$CHAN" ] && [ -n "$MATCH" ] || { echo "usage: VER CHAN REGEX"; exit 1; }

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

echo "host=$(hostname) start=$(date) ver=${VER} chan=${CHAN} match=${MATCH}"
echo "=== GATE: dry run ==="
python3 -u submit.py --samples "${ALL}" --version "${VER}" --channels "${CHAN}" \
    --pack-size 6 --dataset-match "${MATCH}" --dry-run > "logs_${VER}/relaunch_dryrun_${SLURM_JOB_ID}.log" 2>&1
rc=$?
n=$(grep -c '^  --- /' "logs_${VER}/relaunch_dryrun_${SLURM_JOB_ID}.log")
echo "dry-run rc=${rc} datasets matched=${n}"
if [ "$rc" -ne 0 ] || [ "$n" -ne 1 ]; then
    echo "GATE FAILED (need rc=0 and exactly 1 dataset) -- refusing to submit"
    exit 1
fi

echo "=== REAL SUBMISSION ==="
python3 -u submit.py --samples "${ALL}" --version "${VER}" --channels "${CHAN}" \
    --pack-size 6 --cpus-per-subjob 1 --dataset-match "${MATCH}"
echo "RELAUNCH_RC=$?  end=$(date)"
