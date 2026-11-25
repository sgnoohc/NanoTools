#!/bin/bash
#SBATCH --job-name=v54_launch
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=96:00:00
#SBATCH --output=logs_v54/submit_v54.log
#SBATCH --error=logs_v54/submit_v54.log

# v54: the v30 4Lep skim re-run with three extra NanoAOD collections (IsoTrack, Photon,
# TrigObj) via the opt-in channel 4LepExtra (= Analysis_4Leptons, unchanged selection; same
# 4Lep matrix column and lepton PDs). A SEPARATE campaign: NOT linked into v30 (user request).
# Groups = the set that reproduces v30's four 4Lep tags (coverage: local_v54/coverage.py):
#   Run2 Bkg 240 (+8 ZZTo4Q/ZZTo2Q2L the matrix allows but v30's 4Lep never ran),
#   Run2 Data 86, Run3 Bkg 171, Run3 Data 141 (2022-2025). Not: 2026 data, zz4l_extra, vg2l.
# Runs on a compute node, never a login node.

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
export X509_USER_PROXY=$HOME/private/x509_proxy
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir

SAMPLES="run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_ttz_lowmass,run2_bkg_zh4l,run2_bkg_zz4l,run2_data,run3_bkg,run3_bkg_ggzz4l,run3_bkg_hh,run3_bkg_hh_bbtautau,run3_bkg_twz,run3_bkg_zh4l,run3_data"
CH=4LepExtra

echo "host=$(hostname)  start=$(date)"
echo "=== GATE: dry run ==="
python3 -u submit.py --samples "${SAMPLES}" --channels ${CH} --version v54 \
    --pack-size 6 --dry-run > logs_v54/dryrun_gate_v54.log 2>&1
rc=$?
echo "dry-run rc=${rc}"
grep -E "^=== Group" logs_v54/dryrun_gate_v54.log
echo "  datasets: $(grep -c '^  --- /' logs_v54/dryrun_gate_v54.log)"
if [ "$rc" -ne 0 ]; then
    echo "DRY RUN FAILED -- refusing to submit"
    grep -A6 Traceback logs_v54/dryrun_gate_v54.log | head -12
    exit 1
fi

echo "=== REAL SUBMISSION ==="
python3 -u submit.py --samples "${SAMPLES}" --channels ${CH} --version v54 \
    --pack-size 6 --cpus-per-subjob 1
echo "V54_RC=$?  end=$(date)"
