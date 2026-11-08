#!/bin/bash
#SBATCH --job-name=v51_validate
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --output=logs_v51/validate_v51.log
#SBATCH --error=logs_v51/validate_v51.log

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
echo "host=$(hostname) start=$(date)"
SKIM=VBSVVH_skim_v51
BASE=/cmsuf/data/store/user/phchang/skim/${SKIM}

# Two conditions: 994 task dirs exist AND all their jobs are done.
read D T Z NT < <(python3 v48_state.py "*_v51_*")
echo "state: jobs ${D}/${T} zero-job=${Z} tasks=${NT}/994"
if [ "${NT:-0}" -ne 994 ] || [ "${T:-0}" -ne 4086 ] || [ "${D:-0}" -ne 4086 ]; then
  echo "NOT COMPLETE -- refusing to validate"; exit 1
fi

# Let the driver exit on its own ("All job finished"); cancel by name if it lingers.
for i in $(seq 1 40); do squeue -h -n v51_launch | grep -q . || break; sleep 30; done
if squeue -h -n v51_launch | grep -q .; then echo "driver still alive -> scancel"; scancel --name=v51_launch; sleep 15; fi
grep -a -m1 "All job finished" logs_v51/submit_v51.log || echo "(no 'All job finished' line)"

echo; echo "###### inputs vs dedup list (io_mapping) ######"
python3 -u ../local_v51/dedup_leak_check.py 2>&1 | tail -25

echo; echo "###### regen runs_summary ######"
python3 -u regen_runs_summary.py --skim-name ${SKIM} --execute 2>&1 | tail -3
echo; echo "###### check.py (structure) ######"
t0=$(date +%s)
python3 -u check.py --skim-name ${SKIM} --no-dashboard 2>&1 | tee check_v51.log | tail -15
echo "structural pass: $(( $(date +%s) - t0 )) s"
echo "-- error classes:"; grep -oP 'ERROR: \K.*' check_v51.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo "-- warning classes:"; grep -oP 'WARN(ING)?: \K.*' check_v51.log | sed 's/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo; echo "###### check_weights ######"
python3 -u check_weights.py ${SKIM} 2>&1 | tail -15
echo; echo "###### check.py --check-root ######"
t0=$(date +%s)
python3 -u check.py --skim-name ${SKIM} --no-dashboard --check-root 2>&1 | tee check_v51_root.log | tail -15
echo "root pass: $(( $(date +%s) - t0 )) s"
echo "-- root error classes:"; grep -oP 'ERROR: \K.*' check_v51_root.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head

echo; echo "###### largest outputs (ROOT 100 GB TTree limit) ######"
find ${BASE} -name 'output_*.root' -size +80G -printf '%s %p\n' | sort -rn | awk '{printf "  %6.1f GB  %s\n", $1/1e9, $2}' | head -15
echo "  outputs > 80 GB: $(find ${BASE} -name 'output_*.root' -size +80G | wc -l)   > 95 GB: $(find ${BASE} -name 'output_*.root' -size +95G | wc -l)"

echo; echo "###### inventory ######"
for d in ${BASE}/*/; do echo "  $(basename $d): $(ls -1 $d | wc -l) datasets, $(find $d -name 'output_*.root' | wc -l) files, $(du -sh $d | cut -f1)"; done
echo "  total: $(du -sh ${BASE} | cut -f1)"
echo "V51_VALIDATE_DONE $(date)"
