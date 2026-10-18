#!/bin/bash
#SBATCH --job-name=check_v42
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=12G
#SBATCH --time=04:00:00
#SBATCH --output=logs_v47/check_v42_postrename.log
#SBATCH --error=logs_v47/check_v42_postrename.log

# Structural re-validation of v42 after the in-place branch rename.
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
python3 -u check.py --skim-name VBSVVH_skim_v42 --no-dashboard
echo "CHECK_RC=$?"
python3 -u check_weights.py VBSVVH_skim_v42
echo "WEIGHTS_RC=$?"
