---
description: Launch a VBS VVH skim campaign on SLURM, with every pre-flight gate enforced
argument-hint: <vNN> <sample-groups> [--channels TAG] [--pack-size N]
---

Launch skim campaign: **$ARGUMENTS**

You are running CMS NanoAOD skim production on HiPerGator. Read
`skimmer/CLAUDE.md` (the runbook and version ledger) and the top entries of
`skimmer/log.md` before acting. Follow the steps below in order. Do not skip a
gate because it looks redundant — each one exists because skipping it has cost
days before.

## 0. Confirm scope before anything else

"Produce vNN" has meant wildly different things: a full re-skim, one new
channel over existing samples, one new data group. If the scope in the
arguments is ambiguous, ask the user rather than guessing. Check the ledger in
`skimmer/CLAUDE.md` for the next free version number and tell the user which
one you are using.

Sample groups live in `skimmer/condor/samples.py`. List them with
`python3 submit.py --list-samples`. Channels are `ALL_CHANNELS` in
`submit.py`; opt-in channels in `EXTRA_CHANNELS` (e.g. `4LepLoose`) only run
when named explicitly with `--channels`.

## 1. Pre-flight — all four must pass

Run these and report the results before submitting anything.

```bash
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9          # REQUIRED: sets USEDASGOCLIENT=1; without it submit.py crashes
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
```

- **Proxy** — `voms-proxy-info -file ~/private/x509_proxy -timeleft`. Must
  comfortably outlast the run. If stale, ask the user to run
  `hpggsetupel9 && gsetupgen` (note `gsetupgen`, not `gsetup`). An expired
  proxy also makes DAS return nothing, which looks like "dataset not found".
- **Binary and tarball current** — if any code under `skimmer/src`,
  `NanoCORE/` or `rapido/src` changed since the last version, rebuild AND
  re-tar. `make` does NOT track header dependencies, so after a header-only
  change you must `touch src/main.cc` first or nothing recompiles:
  ```bash
  touch src/main.cc && make -j8 && bash condor/maketar.sh
  ```
- **Local smoke test** with **several** input files, never one. Per-tree setup
  code runs once per file, so single-file tests hide real bugs.
- **Disk** — estimate the output volume and check there is room.

## 2. Submit via sbatch, never on a login node

Write an sbatch wrapper modelled on `skimmer/condor/launch_v48.sbatch`. It must:

- run the **dry run first as a gate** and `exit 1` if it fails, so a bad config
  never creates task dirs
- `export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH` (a missing PYTHONPATH is a
  real failure that has happened)
- use `--account=avery --qos=avery --partition=hpg-default`; prefer `avery`
  over the burst QOS `avery-b`, which has sat fully pending for hours
- set a generous `--time` (the Metis driver runs for hours to days)
- log to `logs_vNN/submit_vNN.log`

Record the exact command as a commented line in `skimmer/condor/my_submit.sh`.

## 3. Monitor from io_mapping, never from the driver log

The Metis loop reprints "jobs expected" and "Job N submitted" on every
monitoring pass, so grepping the log double-counts and has produced false
alarms twice. The authoritative check is:

```bash
python3 condor/v48_state.py '*_vNN_*'   # prints: done total zero_job n_tasks
```

It aborts loudly if `PYTHONPATH` is unset rather than reporting a false `0 0`.

A campaign is finished when **both** conditions hold: the expected number of
task dirs exists **and** all their jobs are done. Checking only job completion
races badly if a task dir has just been deleted for resubmission.

Note the driver may never self-terminate: a dataset that is INVALID in DAS
produces a task with an empty `io_mapping` that never counts as complete, so
"All job finished" never prints. Stop it with `scancel --name=<jobname>`.

## 4. Validate, then update the ledger

Run `/validate-skim vNN`. When it passes, add a row to the ledger in
`skimmer/CLAUDE.md` and a dated narrative entry to `skimmer/log.md`, then
commit and push to branch `vvh_skimmer`.

## If a job fails repeatedly

- Check whether it is OOM or wall-clock: `sacct -j <id> -o State,Elapsed,MaxRSS`.
- Remember `MAX_FILES_PER_JOB` bounds **input**, not output — a high-acceptance
  channel can make a modest file count unschedulable. Split on expected output
  size.
- **Changing a split requires DELETING the task dir.** `io_mapping` and the
  tarball are frozen in `backup.pkl`; re-running prints the new split and
  silently reuses the old one.
- "COMPLETED exit 0:0" with no output file means the skim crashed but the
  wrapper still exited 0. Read `<taskdir>/logs/std_logs/*.err` for a stack
  trace — do not assume success from the exit code.

## Reporting

Tell the user the dataset and job counts from the dry run before submitting,
and report honestly afterwards: if jobs failed, say so with the evidence. Never
report a campaign complete based on the driver log alone.
