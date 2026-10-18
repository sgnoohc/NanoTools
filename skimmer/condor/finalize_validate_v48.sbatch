#!/bin/bash
#SBATCH --job-name=v48_final
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=2
#SBATCH --mem=12G
#SBATCH --time=12:00:00
#SBATCH --output=logs_v48/finalize_validate_v48.log
#SBATCH --error=logs_v48/finalize_validate_v48.log

cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9 > /dev/null 2>&1
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH

echo "host=$(hostname) start=$(date)"

# 1. wait for every job to land (io_mapping is authoritative; the driver log is not)
for i in $(seq 1 240); do
  python3 - > /tmp/v48_state.$$ <<'PY'
import pickle,os,glob
T=glob.glob("/blue/avery/p.chang/tasks/*_v48_4LepLoose")
t=d=z=0
for D in T:
    try: io=pickle.load(open(f"{D}/backup.pkl","rb"))["io_mapping"]
    except Exception: continue
    if not io: z+=1; continue
    t+=len(io); d+=sum(os.path.isfile(str(getattr(o,'name',o))) for _,o in io)
print(f"{d} {t} {z} {len(T)}")
PY
  read D T Z NT < /tmp/v48_state.$$
  echo "  [$(date '+%H:%M:%S')] jobs ${D}/${T}  zero-job tasks=${Z}  tasks=${NT}"
  [ "$T" -gt 0 ] && [ "$D" -eq "$T" ] && break
  sleep 180
done
rm -f /tmp/v48_state.$$

# stop the driver: zero-job tasks (INVALID datasets) mean it never self-terminates
scancel 46480176 2>/dev/null
sleep 15

echo; echo "###### regen runs_summary ######"
python3 -u regen_runs_summary.py --skim-name VBSVVH_skim_v48 --execute 2>&1 | tail -2

echo; echo "###### finalize: v13 consolidation + era aliases ######"
python3 -u finalize_v48.py --execute

echo; echo "###### check.py ######"
python3 -u check.py --skim-name VBSVVH_skim_v48 --no-dashboard 2>&1 | tee check_v48.log | grep -E "^SUMMARY"
grep -oP 'ERROR: \K.*' check_v48.log | sed 's/\[job [0-9]*\]//; s/[0-9]\+/N/g' | sort | uniq -c | sort -rn | head -4

echo; echo "###### check_weights ######"
python3 -u check_weights.py VBSVVH_skim_v48 2>&1 | grep -E "groups checked|disagreements|mismatches|unreadable"

echo; echo "###### final inventory ######"
for t in Run2_Bkg_v15_v48_4LepLoose Run2_Data_v15_v48_4LepLoose Run3_Bkg_v15_v48_4LepLoose Run3_Data_v15_v48_4LepLoose Run3_Bkg_v13_v48_4LepLoose; do
  d=/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v48/$t
  [ -d "$d" ] || continue
  n=$(ls -1 "$d" | grep -vc 'Summer24for2025$')
  a=$(ls -1 "$d" | grep -c 'Summer24for2025$')
  echo "  $t : $n datasets, $a aliases, $(du -shL $d 2>/dev/null | cut -f1)"
done
echo "V48_FINAL_DONE $(date)"
