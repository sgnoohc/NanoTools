#!/bin/bash
#SBATCH --job-name=v53_validate
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=02:00:00
#SBATCH --output=logs_v53/validate_v53.log
#SBATCH --error=logs_v53/validate_v53.log

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
echo "host=$(hostname) start=$(date)"

# Two conditions: 45 task dirs exist AND all their jobs are done.
read D T Z NT < <(python3 v48_state.py "*_v53_*")
echo "state: jobs ${D}/${T} zero-job=${Z} tasks=${NT}/45"
if [ "${NT:-0}" -ne 45 ] || [ "${T:-0}" -ne 45 ] || [ "${D:-0}" -ne 45 ]; then
  echo "NOT COMPLETE -- refusing to validate"; exit 1
fi

# Let the driver exit on its own ("All job finished"); cancel by name if it lingers.
for i in $(seq 1 40); do squeue -h -n v53_launch | grep -q . || break; sleep 30; done
if squeue -h -n v53_launch | grep -q .; then echo "driver still alive -> scancel"; scancel --name=v53_launch; sleep 15; fi
grep -m1 "All job finished" logs_v53/submit_v53.log || echo "(no 'All job finished' line)"

echo; echo "###### regen runs_summary ######"
python3 -u regen_runs_summary.py --skim-name VBSVVH_skim_v53 --execute 2>&1 | tail -3
echo; echo "###### check.py (structure) ######"
t0=$(date +%s)
python3 -u check.py --skim-name VBSVVH_skim_v53 --no-dashboard 2>&1 | tee check_v53.log | tail -15
echo "structural pass: $(( $(date +%s) - t0 )) s"
echo "-- error classes:"; grep -oP 'ERROR: \K.*' check_v53.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo "-- warning classes:"; grep -oP 'WARN(ING)?: \K.*' check_v53.log | sed 's/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo; echo "###### check_weights ######"
python3 -u check_weights.py VBSVVH_skim_v53 2>&1 | tail -15
echo; echo "###### check.py --check-root ######"
t0=$(date +%s)
python3 -u check.py --skim-name VBSVVH_skim_v53 --no-dashboard --check-root 2>&1 | tee check_v53_root.log | tail -15
echo "root pass: $(( $(date +%s) - t0 )) s"
echo; echo "###### inventory ######"
S=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v53
du -sh $S | sed 's/^/  total /'
for t in $(ls $S); do
  echo "  $t: $(ls $S/$t | wc -l) ds, $(du -sh $S/$t | cut -f1)"
  for x in $S/$t/*/; do echo "    $(basename $x | grep -oE 'RunIISummer20UL[0-9]+NanoAOD(APV)?'): $(awk -F, 'NR==2{a=$2} END{print "AllEvents=" a+0, "kept=" $2+0}' $(ls $x/cutflow_*.csv | head -1)) files=$(ls $x/output_*.root | wc -l)"; done
done

echo; echo "###### v30 equivalence (being linked into v30) ######"
# Branch set vs v30's TTZToLLNuNu_M-10 output of the SAME era and channel (HLT menus differ by year).
V30=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v30
L=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/local_ttz_v53
: > $L/v53_dirs.txt
for t in $(ls $S); do
  ch=${t##*_v53_}
  for x in $S/$t/*/; do
    ds=$(basename $x)
    if [[ $t == Run2_* ]]; then   # TTZ M-1to10 -> v30 TTZToLLNuNu_M-10, same era
      era=$(echo $ds | grep -oE '_RunIISummer20UL.*$')
      ref=$(ls $V30/Run2_Bkg_v15_v30_${ch}/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8${era}/output_*.root | head -1)
      lab=$(echo $era | grep -oE 'UL[0-9]+NanoAOD(APV)?')
    else                          # Run3 Summer24 TWZ -> v30 Summer24 TZQB (amcatnlo), same channel
      ref=$(ls $V30/Run3_Bkg_v15_v30_${ch}/TZQB-Zto2L-4FS_Bin-MLL-30_*Summer24*_NANOAODSIM/output_*.root | head -1)
      lab=Summer24-TWZ
    fi
    echo "  $ch $lab: $(python3 $L/cmp_branches.py $(ls $x/output_*.root | head -1) $ref | awk '{printf "%s ", $0} END{print ""}' | grep -oE '(Events|Runs): new=[0-9]+ ref=[0-9]+|only_new=[0-9]+ only_ref=[0-9]+ type_diff=[0-9]+' | paste -sd' ')"
    echo "$ch Bkg $t/$ds" >> $L/v53_dirs.txt
  done
done
echo; echo "###### v30 selection re-derived on every output ######"
python3 -u $L/v30_selection_check.py $L/v53_dirs.txt $S/ 2>&1
echo "V53_VALIDATE_DONE $(date)"
