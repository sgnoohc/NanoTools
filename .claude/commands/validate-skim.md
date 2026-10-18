---
description: Validate a completed skim version — structure, weights, and ROOT integrity
argument-hint: <vNN>
---

Validate skim version: **$ARGUMENTS**

Run all three layers. They catch different failures, and the first one alone is
not sufficient. Run them on a compute node via `sbatch`, not on a login node —
`check.py` over a large version takes hours.

```bash
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer
source setup.sh el9
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
```

## 1. Completion — before validating anything

```bash
python3 v48_state.py '*_vNN_*'     # done total zero_job n_tasks
```

Validating a partially-complete version produces confident, wrong numbers.
`zero_job` tasks are normal when a dataset is INVALID in DAS — confirm with
`dasgoclient -query="dataset dataset=<DS> status=* | grep dataset.status"`
rather than treating them as failures.

## 2. Structure

```bash
python3 -u check.py --skim-name VBSVVH_skim_vNN --no-dashboard | tee check_vNN.log
python3 regen_runs_summary.py --skim-name VBSVVH_skim_vNN --execute
```

Classify every error rather than reporting a raw count:

- `eventCount=0` is usually **benign** — a tight channel on a soft sample
  legitimately selects nothing. Spot-check that the cutflow and `genEventSumw`
  are intact before calling it benign.
- LHE weight warnings on pythia8-only samples are benign.
- Missing `runs_summary_N.json` with a valid ROOT file is fixed by the regen
  step above. If no ROOT is recoverable, use
  `cleanup_missing_runs_summary.py --execute` so Metis resubmits.
- A non-zero exit means errors were *counted*, not that they are real.

## 3. Weights — the layer `check.py` does not cover

```bash
python3 check_weights.py VBSVVH_skim_vNN
```

`check.py` never looks inside `runs_summary_*.json`, so a duplicated or dropped
job silently corrupts the normalisation denominator. This asserts two things:

- summed `genEventSumw` is **identical across every channel** of a dataset —
  they read the same inputs, so any spread means jobs saw the wrong files
- summed `genEventCount` equals the cutflow `AllEvents` — different code paths,
  so agreement is a real cross-check

Both must be zero. Anything else is a genuine problem, not a benign warning.

## 4. ROOT integrity (slow, optional but worth it for a new production)

```bash
python3 -u check.py --skim-name VBSVVH_skim_vNN --check-root | tee check_vNN_root.log
```

Opens every file for zombie/recovery detection. Confirm it actually did work —
compare its runtime against the structural pass; if it returns in seconds it
did not open anything.

## 5. Report and record

Report: datasets checked, errors **by classified type**, warnings by type,
weight results, and total volume. If anything failed, say so plainly with the
evidence rather than rounding up to "validated".

Then update the ledger row in `skimmer/CLAUDE.md` to VALIDATED with the date
and the key numbers, add a narrative entry to `skimmer/log.md`, commit, and
push to `vvh_skimmer`.

## Linking into v30

Only if the user asks. v30 is the reference tree that other versions fold into
by symlink:

```bash
python3 link_into_skim.py --source VBSVVH_skim_vNN --dest VBSVVH_skim_v30 --execute
```

It refuses to link if a destination already exists, which has caught genuine
double-link attempts. Use `--tag-subst v13=v15` when the nano version in the
source tag differs. Note that **opt-in channels are not linked into v30** —
v30 has no tag for them — and v14 PFNano versions are deliberately kept
separate.
