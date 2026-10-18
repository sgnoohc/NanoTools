#!/bin/bash
#SBATCH --job-name=jetid_spot
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --array=0-9
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:45:00
#SBATCH --output=logs_v47/spotcheck/shard_%a.log
#SBATCH --error=logs_v47/spotcheck/shard_%a.log

# Event-level spot check after the in-place rename. Reads EVERY entry of each
# sampled file, stratified across all 80 era/kind/channel tags.
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
echo "host=$(hostname) shard=${SLURM_ARRAY_TASK_ID} start=$(date '+%H:%M:%S')"
python3 -u spotcheck_jetid.py VBSVVH_skim_v42 --sample 400 -j 4 \
    --shard "${SLURM_ARRAY_TASK_ID}" --nshards 10
echo "shard=${SLURM_ARRAY_TASK_ID} rc=$? end=$(date '+%H:%M:%S')"
