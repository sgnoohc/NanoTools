#!/bin/bash
#SBATCH --job-name=v49_final
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=12G
#SBATCH --time=12:00:00
#SBATCH --output=logs_v49/finalize_validate_v49.log
#SBATCH --error=logs_v49/finalize_validate_v49.log

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
echo "host=$(hostname) start=$(date)"

# Wait on TWO conditions, not one: the expected number of TASKS must exist AND
# all their jobs must be done. Waiting only on "jobs complete" raced badly once:
# a task dir had just been deleted for resubmission, so it was not counted as
# outstanding, and this job declared victory and cancelled the driver five
# seconds into its dry run.
EXPECT_TASKS=883
COMPLETE=0
for i in $(seq 1 480); do
  read D T Z NT < <(python3 v48_state.py "*_v49_4LepLooseNoLH")
  echo "  [$(date '+%H:%M:%S')] jobs ${D}/${T}  zero-job=${Z}  tasks=${NT}/${EXPECT_TASKS}"
  if [ "${NT:-0}" -ge "$EXPECT_TASKS" ] && [ "${T:-0}" -gt 0 ] && [ "${D:-0}" -eq "${T:-1}" ]; then
      echo "  all tasks present and complete"; COMPLETE=1; break
  fi
  sleep 180
done
# Never cancel the driver or validate a partial campaign on a timeout.
if [ "$COMPLETE" -ne 1 ]; then
  echo "TIMEOUT: campaign not complete -- driver left running, nothing validated"
  exit 1
fi

# stop the driver by NAME, not a hardcoded id: zero-job tasks (DAS-invalid
# datasets) mean Metis never prints "All job finished" and never self-exits.
scancel --name=v49_launch 2>/dev/null
sleep 15

echo; echo "###### regen runs_summary ######"
python3 -u regen_runs_summary.py --skim-name VBSVVH_skim_v49 --execute 2>&1 | tail -2
echo; echo "###### finalize: v13 consolidation + era aliases ######"
python3 -u finalize_v48.py --skim VBSVVH_skim_v49 --channel 4LepLooseNoLH --execute
echo; echo "###### check.py ######"
python3 -u check.py --skim-name VBSVVH_skim_v49 --no-dashboard 2>&1 | tee check_v49.log | grep -E "^SUMMARY"
grep -oP 'ERROR: \K.*' check_v49.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head -4
echo; echo "###### check_weights ######"
python3 -u check_weights.py VBSVVH_skim_v49 2>&1 | grep -E "groups checked|disagreements|mismatches|unreadable"
echo; echo "###### final inventory ######"
for t in Run2_Bkg_v15_v49_4LepLooseNoLH Run2_Data_v15_v49_4LepLooseNoLH Run3_Bkg_v15_v49_4LepLooseNoLH Run3_Data_v15_v49_4LepLooseNoLH Run3_Bkg_v13_v49_4LepLooseNoLH; do
  d=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v49/$t
  [ -d "$d" ] || continue
  n=$(ls -1 "$d" | grep -vc 'Summer24for2025$')
  a=$(ls -1 "$d" | grep -c 'Summer24for2025$')
  echo "  $t : $n datasets, $a aliases, $(du -shL $d 2>/dev/null | cut -f1)"
done
echo "V49_FINAL_DONE $(date)"
