# Skimmer

## Building

```bash
cd skimmer/
make -j
./skim -h  # print help
```

## Quick Test

Run a single skim locally:

```bash
./skim \
    -d ./ \
    /cmsuf/data/store/... /path/to/some/NANOAODSIM.root
```

## Submission Workflow

All submission happens from `condor/`.

### 1. Create the tarball

```bash
cd condor/
sh maketar.sh
```

### 2. Set up VOMS proxy

```bash
voms-proxy-init -hours 168 -voms cms -rfc
```

### 3. Source MetIS

```bash
cd ProjectMetis && source setup.sh && cd ..
```

### 4. Submit jobs

```bash
python submit.py --skim-name VBSVVH_skim_v28 --samples run2_sig
```

The MetIS loop runs continuously, resubmitting failed jobs until all are complete.
Press `Ctrl+C` to stop.

### `submit.py` options

| Flag | Default | Description |
|------|---------|-------------|
| `--skim-name NAME` | *(required)* | Top-level skim directory name (e.g. `VBSVVH_skim_v28`). Output goes to `skim/<NAME>/<tag>/`. |
| `--samples GROUPS` | all | Comma-separated sample groups: `run2_data`, `run2_bkg`, `run2_sig`, `run3_data`, `run3_bkg`, `run3_sig`. Omit to submit ALL groups. |
| `--arch {el8,el9}` | `el9` | Target architecture. |
| `--scheduler {condor,slurm}` | `slurm` | Job scheduler. |
| `--version VER` | `v1` | Version suffix for the MetIS unique_key. |
| `--pack-size N` | `1` | Pack N jobs per SLURM allocation. |
| `--cpus-per-subjob N` | `1` | CPUs per sub-job within a pack. |
| `--list-samples` | | Print available sample groups and exit. |
| `--dry-run` | | Print what would be submitted without actually submitting. |

### Packed jobs

For large campaigns, use packed SLURM jobs to reduce scheduler overhead:

```bash
python submit.py --skim-name VBSVVH_skim_v28 --samples run2_bkg --pack-size 10 --cpus-per-subjob 2
```

This packs 10 jobs per SLURM allocation, each using 2 CPUs for intra-job parallelism.

## Output Structure

Output goes to `/cmsuf/data/store/user/phchang/skim/<skim-name>/`:

```
VBSVVH_skim_v28/
  Run2_Bkg_v15_v28_0Lep1FJ/
    <dataset_name>/
      output_0.root
      cutflow_0.csv
      runs_summary_0.json
      output_1.root
      cutflow_1.csv
      runs_summary_1.json
      ...
  Run2_Sig_v15_v28_0Lep1FJ/
    ...
```

Each job produces three files per index:
- `output_N.root` — skimmed NanoAOD
- `cutflow_N.csv` — cut flow table (AllEvents through TheEnd)
- `runs_summary_N.json` — run metadata (eventCount, genEventSumw, LHE/PS weights, etc.)

## Validation & Recovery

All scripts are in `condor/` and accept `--base-dir` to override the default output directory.

### `check.py` — Validate skim output

Checks JSON validity, key completeness, value sanity, file pairing, cutflow consistency, and dashboard completeness.

```bash
# Full validation
python3 check.py --skim-name VBSVVH_skim_v28

# Single subdirectory, skip dashboard
python3 check.py --skim-name VBSVVH_skim_v28 --subdir Run2_Bkg_v15_v28_0Lep1FJ --no-dashboard

# Also check ROOT file integrity (requires PyROOT)
python3 check.py --skim-name VBSVVH_skim_v28 --check-root
```

### `regen_runs_summary.py` — Regenerate 0-byte JSON metadata

Some jobs produce valid ROOT files but 0-byte `runs_summary_N.json`. This script reads the ROOT file and regenerates the JSON.

```bash
# Dry-run (default)
python3 regen_runs_summary.py --skim-name VBSVVH_skim_v28

# Actually write files
python3 regen_runs_summary.py --skim-name VBSVVH_skim_v28 --execute
```

### `cleanup_missing_runs_summary.py` — Delete incomplete job outputs

Deletes all output files for job indices that are missing `runs_summary_N.json`, forcing MetIS to resubmit them.

```bash
# Dry-run (default)
python3 cleanup_missing_runs_summary.py --skim-name VBSVVH_skim_v28

# Actually delete files
python3 cleanup_missing_runs_summary.py --skim-name VBSVVH_skim_v28 --execute
```

## Debugging

- **`kill_stuck_packed.py`** — Kill SLURM packed jobs that have been running too long.
- **`profile_jobs.py`** — Profile job runtimes and resource usage.
