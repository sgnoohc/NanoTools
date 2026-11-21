#!/bin/bash
#SBATCH --job-name=v52_validate
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=02:00:00
#SBATCH --output=logs_v52/validate_v52.log
#SBATCH --error=logs_v52/validate_v52.log

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
echo "host=$(hostname) start=$(date)"

# Two conditions: 4 task dirs exist AND all their jobs are done.
read D T Z NT < <(python3 v48_state.py "*_v52_4Lep")
echo "state: jobs ${D}/${T} zero-job=${Z} tasks=${NT}/4"
if [ "${NT:-0}" -ne 4 ] || [ "${T:-0}" -ne 4 ] || [ "${D:-0}" -ne 4 ]; then
  echo "NOT COMPLETE -- refusing to validate"; exit 1
fi

# Let the driver exit on its own ("All job finished"); cancel by name if it lingers.
for i in $(seq 1 40); do squeue -h -n v52_launch | grep -q . || break; sleep 30; done
if squeue -h -n v52_launch | grep -q .; then echo "driver still alive -> scancel"; scancel --name=v52_launch; sleep 15; fi
grep -m1 "All job finished" logs_v52/submit_v52.log || echo "(no 'All job finished' line)"

echo; echo "###### regen runs_summary ######"
python3 -u regen_runs_summary.py --skim-name VBSVVH_skim_v52 --execute 2>&1 | tail -3
echo; echo "###### check.py (structure) ######"
t0=$(date +%s)
python3 -u check.py --skim-name VBSVVH_skim_v52 --no-dashboard 2>&1 | tee check_v52.log | tail -15
echo "structural pass: $(( $(date +%s) - t0 )) s"
echo "-- error classes:"; grep -oP 'ERROR: \K.*' check_v52.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo "-- warning classes:"; grep -oP 'WARN(ING)?: \K.*' check_v52.log | sed 's/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head
echo; echo "###### check_weights ######"
python3 -u check_weights.py VBSVVH_skim_v52 2>&1 | tail -15
echo; echo "###### check.py --check-root ######"
t0=$(date +%s)
python3 -u check.py --skim-name VBSVVH_skim_v52 --no-dashboard --check-root 2>&1 | tee check_v52_root.log | tail -15
echo "root pass: $(( $(date +%s) - t0 )) s"
echo; echo "###### inventory ######"
d=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v52/Run2_Bkg_v15_v52_4Lep
echo "  $(ls -1 $d | wc -l) datasets, $(du -sh $d | cut -f1)"
for x in $d/*/; do echo "  $(basename $x | cut -c1-40)...$(basename $x | grep -oE 'RunIISummer20UL[0-9]+NanoAOD(APV)?'): $(grep -E '^(AllEvents|FourLeptons),' $x/cutflow_*.csv | tr '\n' ' ')"; done
echo; echo "###### v30 equivalence (being linked into v30) ######"
# Reference = v30's GluGluHToZZTo4L 4Lep output of the SAME era (HLT menus differ by year).
V30=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v30/Run2_Bkg_v15_v30_4Lep
L=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/local_zh4l_v52
for f in $d/*/output_*.root; do
  era=$(basename $(dirname $f) | grep -oE '_RunIISummer20UL.*$')
  REF=$(ls $V30/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8${era}/output_1.root)
  echo "  $era  (ref: GluGluHToZZTo4L, same era)"
  python3 $L/cmp_branches.py $f $REF | sed 's/^/    /'
  python3 $L/v30_4lep_check.py $f | sed 's/^/    /'
done
echo "V52_VALIDATE_DONE $(date)"
