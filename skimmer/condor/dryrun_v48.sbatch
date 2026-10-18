#!/bin/bash
#SBATCH --job-name=v48_dryrun
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=03:00:00
#SBATCH --output=logs_v48/dryrun_v48.log
#SBATCH --error=logs_v48/dryrun_v48.log

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export X509_USER_PROXY=$HOME/private/x509_proxy

MC2="run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_zz4l"
MC3="run3_bkg,run3_bkg_hh,run3_bkg_ggzz4l,run3_bkg_hh_bbtautau,run3_bkg_zh4l"
DATA="run2_data,run3_data,run3_data_2026"

python3 -u submit.py --samples "${MC2},${MC3},${DATA}" \
    --version v48 --channels 4LepLoose --pack-size 6 --dry-run
echo "DRY_RC=$?"
