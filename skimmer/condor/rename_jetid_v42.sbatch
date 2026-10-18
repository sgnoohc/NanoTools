#!/bin/bash
#SBATCH --job-name=jetid_rename
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --array=0-19
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs_v47/rename/shard_%a.log
#SBATCH --error=logs_v47/rename/shard_%a.log

# Rename the stale v12 Jet_jetId branch across VBSVVH_skim_v42.
#
# Run as a SLURM array, NOT on a login node: the full pass is ~16k files and a
# single process would exceed the login-node runtime limit while loading a
# shared, heavily-used machine. Each array task takes 1/20 of the files with 4
# workers, so every process finishes in a couple of minutes.
#
# The script is idempotent -- files already carrying Jet_jetId_v12 are skipped --
# so this safely resumes the partially-completed run and re-verifies as it goes.

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor

echo "host=$(hostname)  shard=${SLURM_ARRAY_TASK_ID}  start=$(date '+%H:%M:%S')"
python3 -u rename_jetid.py VBSVVH_skim_v42 \
    --execute -j 4 \
    --shard "${SLURM_ARRAY_TASK_ID}" --nshards 20
rc=$?
echo "shard=${SLURM_ARRAY_TASK_ID}  rc=${rc}  end=$(date '+%H:%M:%S')"
exit $rc
