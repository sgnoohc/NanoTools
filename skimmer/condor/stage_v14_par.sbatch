#!/bin/bash
#SBATCH --job-name=v14stage
#SBATCH --output=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor/logs_stage/stagepar_%A_%a.out
#SBATCH --error=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor/logs_stage/stagepar_%A_%a.out
#SBATCH --partition=hpg-default
#SBATCH --time=24:00:00
#SBATCH --mem=4gb
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#
# Run PAR slices of stage_v14.sh concurrently inside ONE job.
#
# Why: a slice moves one file at a time, and per-stream WAN throughput from FNAL
# EOS (~2.5 files/min for ~1 GB MC files) -- not CPU -- is the limit. When the
# QOS caps the number of jobs (p.chang: 16 CPUs), more streams per job is the only
# way to go faster. xrdcp needs a fraction of a core, so PAR streams share one CPU.
#
# The split is UNCHANGED: array task k runs slices k*PAR .. k*PAR+PAR-1 of the
# same NSLICES-way partition, so no two streams ever touch the same line, and it
# is safe to mix with plain stage_v14.sh runs of the same manifest/NSLICES as long
# as the slice ranges do not overlap. Each slice logs to stage_<tag>_s<slice>.out
# and ends with stage_v14.sh's usual SLICE_DONE line.
#
# Usage: sbatch --array=0-11 --account=.. --qos=.. stage_v14_par.sbatch <manifest> <nslices> <par> <tag>
set -uo pipefail
MANIFEST=${1:?manifest}; NSLICES=${2:?nslices}; PAR=${3:?par}; TAG=${4:?tag}
K=${SLURM_ARRAY_TASK_ID:?must run as an array}
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor
echo "host=$(hostname) start=$(date) k=$K slices $((K*PAR))..$((K*PAR+PAR-1)) of $NSLICES"
pids=()
for (( j=0; j<PAR; j++ )); do
    s=$((K*PAR+j))
    [ "$s" -ge "$NSLICES" ] && break
    SLURM_ARRAY_TASK_ID=$s bash stage_v14.sh "$MANIFEST" "$NSLICES" \
        > "logs_stage/stage_${TAG}_s${s}.out" 2>&1 &
    pids+=($!)
done
rc=0
for p in "${pids[@]}"; do wait "$p" || rc=1; done
echo "STAGEPAR_DONE k=$K rc=$rc $(date)"
exit $rc
