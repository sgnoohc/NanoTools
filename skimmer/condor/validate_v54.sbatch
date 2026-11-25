#!/bin/bash
#SBATCH --job-name=v54_validate
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=08:00:00
#SBATCH --output=logs_v54/validate_v54.log
#SBATCH --error=logs_v54/validate_v54.log

# v54 = v30's 4Lep skim + IsoTrack/Photon/TrigObj (channel 4LepExtra). NOT linked into v30.
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
echo "host=$(hostname) start=$(date)"
S=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v54
L=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/local_v54

# Two conditions: 646 task dirs exist AND all their jobs are done. The 10 INVALID DY PTLL
# datasets are zero-job tasks by design (DAS lists no valid files for them).
read D T Z NT < <(python3 v48_state.py "*_v54_*")
echo "state: jobs ${D}/${T} zero-job=${Z} tasks=${NT}/646"
if [ "${NT:-0}" -ne 646 ] || [ "${Z:-0}" -ne 10 ] || [ "${T:-0}" -eq 0 ] || [ "${D:-0}" -ne "${T:-0}" ]; then
  echo "NOT COMPLETE -- refusing to validate"; exit 1
fi

# v48_state counts a job done once output_N.root EXISTS, but the packed wrapper copies a big output into place
# before writing cutflow/runs_summary. Validating then would let the regen step rebuild a runs_summary from a
# half-written file. So also wait for this version's packed__ jobs to exit.
inflight() { for j in $(squeue -u "$USER" -h -o '%i %j' | awk '$2 ~ /^packed__/ {print $1}'); do
  scontrol show job "$j" 2>/dev/null | grep -q '_v54_' && echo "$j"; done; }
for i in $(seq 1 60); do [ -z "$(inflight)" ] && break; echo "packed jobs still running: $(inflight | xargs)"; sleep 60; done
[ -n "$(inflight)" ] && { echo "packed jobs still running after 60 min -- refusing to validate"; exit 1; }

# The zero-job tasks mean the driver never prints "All job finished" -> cancel it by name.
if squeue -h -n v54_launch | grep -q .; then echo "driver still alive (zero-job tasks) -> scancel"; scancel --name=v54_launch; sleep 15; fi

echo; echo "###### regen runs_summary ######"
python3 -u regen_runs_summary.py --skim-name VBSVVH_skim_v54 --execute 2>&1 | tail -3
echo; echo "###### check.py (structure) ######"
t0=$(date +%s)
python3 -u check.py --skim-name VBSVVH_skim_v54 --no-dashboard 2>&1 | tee check_v54.log | tail -12
echo "structural pass: $(( $(date +%s) - t0 )) s"
echo "-- error classes:"; grep -oP 'ERROR: \K.*' check_v54.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo "-- warning classes:"; grep -oP 'WARN(ING)?: \K.*' check_v54.log | sed 's/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo; echo "###### check_weights ######"
python3 -u check_weights.py VBSVVH_skim_v54 2>&1 | tail -15
echo; echo "###### check.py --check-root ######"
t0=$(date +%s)
python3 -u check.py --skim-name VBSVVH_skim_v54 --no-dashboard --check-root 2>&1 | tee check_v54_root.log | tail -12
echo "root pass: $(( $(date +%s) - t0 )) s"
echo; echo "###### inventory ######"
du -sh $S | sed 's/^/  total /'
for t in $(ls $S); do echo "  $t: $(find $S/$t -mindepth 1 -maxdepth 1 -type d | wc -l) ds, $(du -sh $S/$t | cut -f1)"; done

echo; echo "###### per-dataset comparison with v30's 4Lep ######"
python3 -u $L/v30_compare.py 2>&1

echo; echo "###### v30 4Lep selection re-derived on every output ######"
: > $L/v54_dirs.txt
for t in $(ls $S); do
  kind=$(echo $t | cut -d_ -f2)
  for x in $(find $S/$t -mindepth 1 -maxdepth 1 -type d); do echo "4Lep $kind $t/$(basename $x)" >> $L/v54_dirs.txt; done
done
python3 -u /blue/avery/p.chang/work/skim/NanoTools_/skimmer/local_ttz_v53/v30_selection_check.py $L/v54_dirs.txt $S/ 2>&1 \
  | tee $L/v54_selection.log | grep -vE ' OK ' | tail -20
echo "selection: $(grep -c ' OK ' $L/v54_selection.log) OK lines of $(wc -l < $L/v54_dirs.txt) dirs"
echo "V54_VALIDATE_DONE $(date)"
