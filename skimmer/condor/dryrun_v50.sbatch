#!/bin/bash
#SBATCH --job-name=v50_dryrun
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=01:00:00
#SBATCH --output=logs_v50/dryrun_v50.log
#SBATCH --error=logs_v50/dryrun_v50.log

# v50: run2_bkg_zh4l (4 UL eras of ZH_HToZZ_4LFilter) x 4LepLooseNoLH only.
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
export X509_USER_PROXY=$HOME/private/x509_proxy

python3 -u submit.py --samples run2_bkg_zh4l \
    --version v50 --channels 4LepLooseNoLH --pack-size 6 --dry-run
echo "DRY_RC=$?"
