---
description: Report what skim work is currently running and the state of recent versions
---

Report the current state of VBS VVH skim production. Be factual and read from
authoritative sources only.

```bash
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor
source ../setup.sh el9
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
```

Gather and report:

**1. Running work**

```bash
squeue -u $USER -o "%i %T %M %j" | head -20
pgrep -af 'submit\.py'
```

Separate *your* skim jobs from unrelated ones — jobs named `packed__*` are
Metis sub-jobs; anything else (e.g. `librarian`) is not this production. Do not
count them together.

**2. Progress of any in-flight version, from io_mapping**

```bash
python3 v48_state.py '*_vNN_*'      # done total zero_job n_tasks
```

Never read completion from the driver log — the Metis loop reprints its
progress lines on every monitoring pass, so grep double-counts.

**3. Long-running drivers that should be stopped**

A driver whose jobs are all finished but which never printed "All job
finished" is stuck on zero-job tasks (DAS-invalid datasets) and will loop
forever. Report any driver running more than a day with its work complete, but
do not kill it without asking.

**4. Proxy**

```bash
voms-proxy-info -file ~/private/x509_proxy -timeleft
```

Report hours remaining; flag it if under a day.

**5. Recent versions**

Read the ledger in `skimmer/CLAUDE.md` and report the newest few rows with
their status. Cross-check anything marked VALIDATING against the actual job
state rather than trusting the row.

**6. Disk**

```bash
du -sh /cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v*  | tail -8
blue_quota
```

## Reporting

Lead with what is in flight and whether it needs attention. Keep it to a short
table plus any anomaly worth acting on. If something looks wrong, say what the
evidence is rather than speculating — and distinguish "queued, waiting on
priority" from "failing", which look similar at a glance but need opposite
responses.
