# VBS VVH Skimmer — onboarding

CMS NanoAOD skim production for the VBS VVH / ZZZ analyses, running on
HiPerGator with ProjectMetis over SLURM. This guide gets you to the point where
you can run a campaign yourself.

## Where things are

| | |
|---|---|
| Working tree | `/blue/avery/p.chang/work/skim/NanoTools_` |
| Skim output | `/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_vNN/` |
| Metis task dirs (job state) | `/blue/avery/p.chang/tasks/` |
| Repo | `github.com:sgnoohc/NanoTools`, branch `vvh_skimmer` |

Two files carry the institutional knowledge and are worth reading before you
touch anything:

- **`skimmer/CLAUDE.md`** — the runbook: workflow, version ledger, and a §7
  list of traps that have each cost days. It auto-loads in Claude Code.
- **`skimmer/log.md`** — dated narrative history, newest first. Read the top
  few entries for current context.

## Slash commands

These package the whole workflow, including every pre-flight gate. Use them
rather than driving `submit.py` by hand.

| Command | What it does |
|---|---|
| `/skim-status` | What is running now, progress of in-flight versions, proxy state |
| `/produce <vNN> <groups> [--channels X]` | Launch a campaign with all gates enforced |
| `/validate-skim <vNN>` | Structure, weights and ROOT integrity, then update the ledger |

Start with `/skim-status` — it is read-only and orients you.

## The five things that will bite you

These are the failure modes that cost the most time. They are expanded in
`skimmer/CLAUDE.md` §7.

1. **Run heavy work on compute nodes, not login nodes.** Submit with `sbatch`.
   A 16-worker pass on a login node once held 359% CPU on a shared machine
   already at load 137. Shard long work into an array job so each task is short.

2. **`source setup.sh el9` in every shell.** It sets `USEDASGOCLIENT=1`; without
   it Metis falls back to an HTTP service that times out from HPG and
   `submit.py` crashes before submitting anything.

3. **Read completion from `io_mapping`, never from the driver log.** The Metis
   loop reprints its progress lines on every monitoring pass, so any grep
   double-counts. Use `python3 condor/v48_state.py '*_vNN_*'`. Relatedly,
   "All job finished" may never print: a DAS-invalid dataset produces a task
   with no jobs that never counts as complete, so the driver loops forever.

4. **Changing a job split requires deleting the task dir.** `io_mapping` and the
   tarball are frozen in `backup.pkl`. Re-running prints the new split and
   silently reuses the old one.

5. **`make` does not track header dependencies.** After editing any `.h` or
   anything under `rapido/src`, `touch src/main.cc` (or `make clean`) first,
   then re-run `condor/maketar.sh` — batch jobs run from `package.tar.xz`, not
   from your working tree.

## Grid proxy

Lasts 7 days. Jobs die at `xrdcp` without it, and DAS queries silently return
nothing — which reads as "dataset not found" and has caused false alarms.

```bash
hpggsetupel9 && gsetupgen        # note gsetupgen, NOT plain gsetup
voms-proxy-info -file ~/private/x509_proxy -timeleft
```

## Validating is three layers, not one

`check.py` checks structure only. It never looks inside `runs_summary_*.json`,
so a duplicated or dropped job silently corrupts the normalisation denominator.
Always also run `check_weights.py`, which asserts that summed `genEventSumw` is
identical across every channel of a dataset — they read the same inputs, so any
spread means jobs saw the wrong files.

Most `eventCount=0` errors are benign (a tight channel on a soft sample). Both
weight checks returning zero is not optional.

## Before you sum anything

Several sample sets overlap processes already present under a different
generator or mass range — DY HT- and jet-binned versus inclusive M-50, the two
`ZZTo4L` variants, 2024 W→ℓν HT versus the pT- and jet-binned sets. They are
*alternatives*, not additions. `skimmer/CLAUDE.md` lists them. Also note v30
contains alias symlinks, so an `ls` count of a channel directory is not its
real dataset count.
