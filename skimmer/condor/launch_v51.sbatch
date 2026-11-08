#!/bin/bash
#SBATCH --job-name=v51_launch
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=96:00:00
#SBATCH --output=logs_v51/submit_v51.log
#SBATCH --error=logs_v51/submit_v51.log

# v51: v14 PFNano samples added to the index AFTER v42 (2026-11-06 index):
#   bkg  -- QCD_Mu (MuEnrichedPt5, 7 pT bins) + W->lnu 4Jets MLNu HT + Z->nunu 4Jets HT
#   data -- MuonEG (2022 C-D, 2022EE E-G, 2023 Cv2-4, 2023BPix D)
# via the *_since42 groups in vbsvvh_v14.py, all default channels (as v42).
# Tags match v42's (Run3_<era>_<Kind>_v14_v51_<ch>). Inputs read from /cmsuf
# (staged), with duplicate-CRAB-task files dropped per v14_dedup.json.

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
export X509_USER_PROXY=$HOME/private/x509_proxy
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir

SAMPLES="v14_2022_bkg_since42,v14_2022EE_bkg_since42,v14_2023_bkg_since42,v14_2023BPix_bkg_since42,v14_2022_data_since42,v14_2022EE_data_since42,v14_2023_data_since42,v14_2023BPix_data_since42"

echo "host=$(hostname)  start=$(date)"
echo "=== GATE 1: every job-producing v14 sample reads an existing /cmsuf file ==="
python3 -u check_staged_paths.py bkg data || { echo "STAGING GATE FAILED -- refusing to submit"; exit 1; }

echo "=== GATE 2: dry run ==="
python3 -u submit.py --samples "${SAMPLES}" --version v51 \
    --pack-size 6 --dry-run ${EXTRA_ARGS:-} > logs_v51/dryrun_gate_v51.log 2>&1
rc=$?
echo "dry-run rc=${rc}"
grep -E "^=== Group" logs_v51/dryrun_gate_v51.log
echo "  datasets: $(grep -c '^  --- /' logs_v51/dryrun_gate_v51.log)"
if [ "$rc" -ne 0 ]; then
    echo "DRY RUN FAILED -- refusing to submit"
    grep -A6 Traceback logs_v51/dryrun_gate_v51.log | head -12
    exit 1
fi

echo "=== REAL SUBMISSION === EXTRA_ARGS='${EXTRA_ARGS:-}'"
# Relaunch 2026-11-08 for the QCD_Mu 0Lep1FJ stragglers (8 h timeouts, 12 GB pack OOMs, and
# jobs whose output would pass ROOT's 100 GB TTree limit). The 16 incomplete tasks were moved
# to tasks/_moved_resplit_v51-20261108 (outputs to skim/_resplit_old_v51-20261108) and
# re-split. Pass EXTRA_ARGS via the environment -- --export=VAR=... would split on its commas:
#   EXTRA_ARGS="--time 24:00:00 --mem-per-subjob 4 --max-files-per-job 20 --channels 0Lep1FJ,0Lep2FJ
#     --dataset-match (QCD_PT-(1000|300to470|470to600|600to800|800to1000)_MuEnriched|Zto2Nu-4Jets_HT-(1500to2500|2500)_)"
#     sbatch launch_v51.sbatch
python3 -u submit.py --samples "${SAMPLES}" --version v51 \
    --pack-size 6 --cpus-per-subjob 1 ${EXTRA_ARGS:-}
echo "V51_RC=$?  end=$(date)"
