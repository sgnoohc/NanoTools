#!/bin/bash
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=12:00:00

# ROOT-integrity layer of /validate-skim: opens every output file (zombie,
# auto-recovered, Events entries vs runs_summary eventCount).
#   sbatch -J v49_rootchk -o logs_v49/check_root_v49.log check_root.sbatch v49
VER=$1
[ -n "$VER" ] || { echo "usage: VER"; exit 1; }
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
t0=$(date +%s); echo "host=$(hostname) start=$(date)"
python3 -u check.py --skim-name "VBSVVH_skim_${VER}" --no-dashboard --check-root > "check_${VER}_root.log" 2>&1
rc=$?
echo "check_rc=${rc} elapsed=$(( $(date +%s) - t0 ))s"
grep -E "^SUMMARY" "check_${VER}_root.log"
grep -oP '(ERROR|WARNING): \K.*' "check_${VER}_root.log" | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head -8
