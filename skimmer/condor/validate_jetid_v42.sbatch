#!/bin/bash
#SBATCH --job-name=jetid_validate
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --array=0-19
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs_v47/validate/shard_%a.log
#SBATCH --error=logs_v47/validate/shard_%a.log

# Independent read-only re-scan of every v42 file after the rename.
# Every file must report already_done; anything else is a problem.
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
echo "host=$(hostname) shard=${SLURM_ARRAY_TASK_ID} start=$(date '+%H:%M:%S')"
python3 -u rename_jetid.py VBSVVH_skim_v42 -j 4 \
    --shard "${SLURM_ARRAY_TASK_ID}" --nshards 20
echo "shard=${SLURM_ARRAY_TASK_ID} rc=$? end=$(date '+%H:%M:%S')"
