# START HERE — VBS VVH Skimmer production runbook

This file auto-loads every session. It is the entrypoint: read it, then
read `log.md` (newest-first narrative history) for full context before acting.

**When the user says "produce vNN" (e.g. "produce v33"), follow §1–§4 below.**
Keep the version ledger (§5) up to date — update it the moment a job is
submitted, and again when it completes/validates.

---

## 0. Orient (do this first, every "produce" request)

1. Read `log.md` top entries — what was the last version, what state is it in.
2. Confirm the **scope** of the new version with the user (see §1) — past
   versions have differed wildly: v30 = full re-skim, v31 = one new channel,
   v32 = one new data group. Don't assume "produce vNN" means a full re-skim.
3. Check proxy + tarball freshness (§2) before launching anything.

---

## 1. Decide the scope (what does "vNN" mean this time?)

Map the user's intent to a `--samples` / `--channels` choice. The submit
command is always run from `condor/` as `python3 submit.py ... --version vNN`.

| Scope | Command tail |
|---|---|
| **Full re-skim** (all groups, all channels) | `--samples run2_sig,run3_sig,run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version vNN` |
| **One new channel** across existing data/bkg | `--samples run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version vNN --channels <TAG>` |
| **New data group only** (e.g. fresh PromptReco) | `--samples <group> --pack-size 12 --cpus-per-subjob 1 --version vNN` |

- Sample groups live in `condor/samples.py` / `SAMPLE_REGISTRY`:
  `run2_data run2_bkg run2_sig run3_data run3_data_2025 run3_bkg run3_sig`.
  List with `python3 submit.py --list-samples`.
- Channels (`ALL_CHANNELS` in `submit.py`): `4Lep 3Lep 2Lep2FJ 2Lep1FJ
  1Lep1FJ 0Lep3FJ 0Lep2FJ 0Lep1FJ 0Lep0FJ 2Lep4J`. Omit `--channels` to run all.
  Signal groups always run the `Sig` channel regardless.
- **Opt-in channels** (`EXTRA_CHANNELS`, NOT in the default matrix — must be
  requested explicitly with `--channels`):
  - `4LepLoose` = loosest ≥4 lepton skim (`VVH::IDloose4L`): e pT>5 |η_SC|<2.5
    cutBased≥1 lostHits≤1; μ pT>3 |η|<2.4 (global||tracker) isPFcand. **No isolation,
    no dxy/dz/sip3d.** `src/Analysis_4LeptonsLoose.h`, fills a SEPARATE
    `vvh_loose4l_lep_p4s` so existing channels are untouched. 7× the events and
    7× the size of 4Lep (v47: 447 GB over 519 bkg datasets). Runs on hadronic
    samples that 4Lep excludes (no matrix column → allowed everywhere), so expect
    more benign zero-yield datasets than 4Lep.
  - `2LepZ350` ⚠ **NOT IN THIS BRANCH** — reverted to branch `z350` (see v35 log).
    The description is retained for when it returns: inclusive ≥2 loose
    leptons with ≥1 opposite-sign same-flavor pair (e⁺e⁻/µ⁺µ⁻) whose **system
    pT ≥ 350 GeV** (a *boosted* Z; mass left loose). For ttZ (boosted Z +
    inclusive ttbar). `src/Analysis_2Leptons_Z.h`, uses lepton PDs. Paired MC
    groups `run2_bkg_ttz` (218) / `run3_bkg_ttz` (69) in `samples.py`.
- `--skim-name` auto-derives to `VBSVVH_skim_vNN` if omitted (leave it omitted).
- Record the exact command in `condor/my_submit.sh` (append a commented line, as
  done for every prior version).

**If anything about scope is ambiguous, ask the user before submitting.**

---

## 2. Pre-flight (must pass before launch)

1. **Proxy** (jobs die at `xrdcp` "Auth failed" without it; lasts 7 days):
   ```bash
   ls -l ~/private/x509_proxy            # must exist and be fresh
   # if stale, from a login node with grid tools (hpggsetupel9):
   gsetupgen                             # writes ~/private/x509_proxy (NOT plain gsetup)
   ```
   If the run will outlast the proxy, renew with `gsetupgen` mid-run — the
   Metis loop re-stages the newer proxy automatically.
2. **Binary + tarball current** — if any skim code changed since the last
   version, rebuild and re-tar:
   ```bash
   source setup.sh el9        # CMSSW_16_0_0_pre4 / el9_amd64_gcc13 + USEDASGOCLIENT=1
   make -j                    # builds ./skim
   cd condor && ./maketar.sh  # regenerates package.tar.xz (md5-verify it has the new binary)
   ```
   Existing Metis task dirs bake their own copy of the executable/tarball
   (`prepared_inputs` in `backup.pkl`) — code changes do NOT propagate to old
   task dirs. For a brand-new `vNN` this is moot (fresh dirs).
3. **Smoke test locally** before a big launch:
   ```bash
   sh test.sh                 # runs ./skim on a couple local SingleMuon files; expect exit 0 + sane cutflow
   ```

---

## 3. Launch

Run detached so it survives logout; log to `condor/logs_vNN/submit_vNN.log`:
```bash
source setup.sh el9          # REQUIRED: sets USEDASGOCLIENT=1 (+dasgoclient on PATH)
cd condor
export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
mkdir -p logs_vNN
setsid python3 submit.py <scope flags from §1> --version vNN \
    > logs_vNN/submit_vNN.log 2>&1 &
echo $!   # record the REAL detached pid (pgrep -f submit.py), not the setsid launcher
```
- ⚠️ **You MUST `source setup.sh el9` in the launch shell** (env does not persist
  across shells). Without `USEDASGOCLIENT=1`, Metis falls back to the UCSD DIS
  HTTP service, which times out from HPG → `do_dis_query` `KeyError: 'payload'`
  and submit.py crashes during task instantiation before submitting anything
  (seen on the v34 first launch, 2026-07-08). dasgoclient is the reliable path.
- Always **dry-run first**: append `--dry-run` to confirm the dataset/channel
  matrix before the real submit.
- Outputs land in `/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_vNN/<tag>/`.
- Dashboards: `http://login12.ufhpc/~p.chang/Run{2,3}_{Bkg,Data,Sig}_v15_vNN/<channel>`.
- The Metis loop re-walks every 600 s, resubmits dead/missing jobs, and exits
  with **"All job finished"** when complete. To stop: `kill <PID>`. To resume
  after a crash: just rerun the same command (Metis picks up from existing
  outputs).
- `MAX_SUBMITTED = 2500` throttle (avery-b QOS cap 3000); `msummary: command
  not found` in the log is harmless.
- **Black-hole nodes:** if you see a high pack FAILED rate with 0–1 s deaths and
  no logs, it's bad nodes (flaky `/blue` mount). See the `--exclude` list in
  `submit.py` (~line 406) and the 2026-06-12 `log.md` entry for how to re-derive it.

---

## 4. Validate (after "All job finished")

```bash
cd condor
# 1. structural check (metadata, pairing, cutflow, dashboard)
python3 -u check.py --skim-name VBSVVH_skim_vNN | tee check_vNN.log
# 2. regenerate any missing/0-byte runs_summary_N.json from the ROOT files
python3 regen_runs_summary.py --skim-name VBSVVH_skim_vNN --execute | tee regen_vNN.log
# 3. for indices with NO recoverable ROOT, delete the partial outputs so Metis resubmits
python3 cleanup_missing_runs_summary.py --skim-name VBSVVH_skim_vNN --execute
# 4. (optional, slow) open every ROOT file for zombie/recovery check
python3 -u check.py --skim-name VBSVVH_skim_vNN --check-root | tee check_vNN_root.log
```
Interpreting check output (see 2026-06-13 `log.md`):
- `eventCount=0` errors are usually **benign**: a tight channel × soft sample
  (e.g. 4Lep on a sample with no 4-lepton events) legitimately selects 0 events;
  confirm cutflow `AllEvents` + `genEventSumw` are intact.
- Missing `runs_summary_N.json` with a valid ROOT → fixed by step 2 (regen).
- LHE-weight warnings on pythia8-only samples are benign.
- Use `python3 -u` so output streams live.

Then update §5 and add a dated entry to `log.md`.

---

## 5. Version ledger  ← UPDATE THIS EACH SUBMISSION

Newest first. One row per version. Status: PLANNED → RUNNING (PID, log) →
COMPLETE → VALIDATED. Full narrative goes in `log.md`; keep this terse.

| Ver | Scope | Status | Notes |
|---|---|---|---|
| v48 | **Full `4LepLoose` campaign for the ZZZ analysis** (collaborator request): MC `run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_zz4l` + `run3_bkg,run3_bkg_hh,run3_bkg_ggzz4l,run3_bkg_hh_bbtautau,run3_bkg_zh4l`; data `run2_data,run3_data,run3_data_2026` | VALIDATING 2026-10-18 | 883 tasks / 5,611 jobs. Four tags: Run2_Bkg (442 ds), Run2_Data (86), Run3_Bkg (160+2 linked), Run3_Data (185, **2022-2026 in ONE dir** — both run3 data groups share the key). Group list chosen by set-cover against the real v30 4Lep listings: 0 uncovered. Run2 is the UNION of v30's 232 and v47's 394 = 442 (4LepLoose has no matrix column so it runs on hadronic samples 4Lep drops). **Run3 is 160 not 170: ten DY PTLL sets are INVALID in DAS.** `finalize_v48.py` links the 2 NanoAODv13 bbtautau ds into the v15 tag and writes the Summer24for2025 aliases (all Summer24 ds — v30 only has 131 of 170). |
| v47 | `run3_bkg` + `run2_bkg`, `--channels 4LepLoose` (519 ds) | ✅ VALIDATED 2026-10-14 | run3 1171/1171 + run2 818/818. check: **519 ds, 0 errors**, 288 benign LHE warnings, **0 `eventCount=0`** (loose WP selects everywhere). Weights clean (0 sumw spread, 0 cutflow mismatch). **447 GB** (Run3 262.8 + Run2 184.4), vs 0.8 TB projected. Acceptance **0.596%** overall (Run2 0.661%, Run3 0.557%) = **7× tight 4Lep**, NOT the 300-440× estimated from single DY/ttbar files — that baseline had almost no real 4L events. 10 DY PTLL datasets produced 0 jobs: **INVALID in DAS** (see below). NOT linked into v30 (opt-in channel). |
| v46 | `run2_bkg,run3_bkg,run2_data,run3_data`, `--channels 2Lep4J` (756 ds) | ✅ VALIDATED 2026-10-12 | 4692/4692. check: 746 ds, 2 benign `eventCount=0`, 288 benign LHE warns. **Weight cross-check: 348/348 datasets match v30's 0Lep0FJ `genEventSumw` exactly** — same inputs, different channel/splitting. Linked into v30 (746 links). v30 now has all 10 channel tags. |
| v45 | `run3_data_parking` (59 ds ParkingHH/HH0/HH1 2023-2026), `--channels 0Lep*` | ✅ VALIDATED 2026-10-12 | 2520/2520. check: 236 ds, **1** benign `eventCount=0` (Run2024A, only 2157 events, needs >=8 jets). 4.30e9 events selected. ⚠ **59 datasets cover only 47 DISTINCT RUN SETS** — see vbsvvh_parking.py. |
| v44 | S. Ellis request: `run2_bkg_zz4l_extra`+2 existing ZZ sets → 4Lep; `run2_bkg_vg2l`,`run3_bkg_vg2l` → 2Lep1FJ | ✅ VALIDATED 2026-10-07 | 158/158. check: 49 ds, 4 benign `eventCount=0` (all ZZTo4Q in 4Lep — fully hadronic, as predicted). Weights clean. |
| v43 | 2026 PromptReco data (44 ds: EGamma0-5, Muon0-3, MuonEG × eras A-D), `--channels 4Lep` | ✅ VALIDATED 2026-10-05 | 722/722. check: 44 ds, 233 err (all benign `eventCount=0`), 0 warn. Needed year-2026 support in **five** places (see §7) + EGamma4/5 & Muon2/3 added to LEPTON_PDS. Group is channel-agnostic — re-run with `--channels` for other channels, but note it is lepton PDs only (no JetMET) and JetId 2026 falls back to the 2024 recipe. |
| v42 | **Full v14 PFNano**: bkg + data × 4 eras (8 groups, 4264 tasks / 16294 jobs) | ✅ VALIDATED 2026-10-05 | 16294/16294. check: **4264 ds, 351 errors (all benign `eventCount=0`), 740 benign LHE warnings, 0 structural**. Replaces abandoned v39. All inputs staged on /cmsuf (57 TB, 0 transfer failures). **NOT linked into v30** — see below. Final gap was TTWW 2023 × 0Lep0FJ; see §7. |
| v41 | `run2_bkg_znunu_ht` + `run3_bkg_vjets_ht` (V+jets HT-binned, M. Mazza request; 46 ds) | ✅ VALIDATED 2026-09-15 | 1524/1524. check: 380 ds, 187 err (all benign `eventCount=0`), 0 warn, 0 OOM. Folded into v30 (334 links). ⚠ 2024 W→ℓν HT is a THIRD description of W+jets alongside the pT- and jet-binned sets in `run3_bkg` — pick one, don't sum. Z→νν is new coverage. Ran `--pack-size 6`. |
| v40 | v14 PFNano **signal**, all 4 eras (48 ds) | ✅ VALIDATED 2026-09-09 | 48/48, 0 errors, 12 benign LHE warns. 88 truth branches present. |
| v39 | v14 PFNano **background MC**, 4 eras × 9 channels | ⚠️ **95.6% — STOPPED, NOT FINISHED** | 7542 outputs; check clean (480 benign `eventCount=0`, 0 structural). **BUT 80 PARTIAL + 79 MISSING = 159 dataset-channels to redo** — partial event coverage is invisible in the files. Stopped over 407 OOM + node `/tmp` exhaustion (613-file sub-jobs). Needs a `files_per_job` cap before resuming. |
| v35 | `run3_sig_lowc2v` (8 new low-C2V signal scan points: C2V=0.25 & 0.75 @ C3=1.0 × 4 procs WWH_OS/SS/WZH/ZZH; 100 files each, main base only — AUX has no 0p25/0p75) | ✅ VALIDATED 2026-07-14 | "All job finished" 2026-07-14 01:10 UTC. **8 datasets, 40 files (5 ROOT each).** `check_v35.log`: **0 errors, 0 warnings.** ✅ **Folded into v30**: 8 relative symlinks `VBSVVH_skim_v30/Run3_Sig_v15_v30_Sig/<ds> → ../../VBSVVH_skim_v35/...` (v30 Sig now 40 = 32 real + 8 linked); brand-new datasets → **no double-counting** (unlike v33 DY). Isolated version, v32/`run3_data_2025` pattern. `cache_miss_empty` DAS warnings benign (private ceph signal not in DAS → 20 files/job default). Commits (branch `vvh_skimmer`): 0d4b251 (samples), b06588c (`run3_sig_lowc2v` group). Used existing Jul-8 tarball (Sig output identical to reverted binary; not re-tarred). |
| v34 (data) | `run2_data,run3_data` (2025 ⊂ run3_data), `--channels 2LepZ350` (lepton PDs auto-filtered: 86 + 141 = **227 unique datasets**) | ✅ VALIDATED 2026-07-08 | Folded into the v34 skim dir alongside MC. **2703 files, 1.7 GB.** check: Run2 86 datasets 0 err; Run3 141 (incl 56 Run2025) 5 benign `eventCount=0`, 0 zombie/missing. NOTE: `run3_data_2025` (72) is a FULL SUBSET of `run3_data` (190) — passing both was redundant (Metis deduped); just use `run2_data,run3_data` next time. Launch: `--samples run2_data,run3_data --version v34 --channels 2LepZ350` (source setup.sh first!). |
| v34 (MC) | `run2_bkg_ttz` + `run3_bkg_ttz`, `--channels 2LepZ350` only (ttZ boosted-Z bkg: 337 group entries → 336 unique) | ✅ VALIDATED 2026-07-08 | "All job finished". **1390 files, 97 GB.** `check_v34.log`: 336 datasets, 323 errors **all benign `eventCount=0`** (tight boosted-Z cut → 0 events in most low-rate bkg; spot-checked ggZH→Zνν: non-zombie, Runs+genEventSumw intact), 86 benign LHE warnings, 0 zombie/missing. 337→336 = duplicate `TTLL_Bin-MLL-4to50` in source run3_bkg (harmless). | Relaunched 2026-07-08 15:11 UTC to fold in W→ℓν (+36 Run2, +14 Run3; 287→337). Earlier: first launch 14:24 crashed on DIS timeout (`USEDASGOCLIENT` unset → `submit_v34.log.disfail1`); 14:28 relaunch w/ setup.sh sourced ran 287 (`submit_v34.log.pass1`). Proxy valid to Jul 15. Boosted-Z channel (pT(ℓℓ)≥350, OSSF, loose mass). Families: DY, **W→ℓν**, ttbar+ttbb, ttZ, ttW, ttWW, ttWZ, ttH, tZq, tWZ, WZ, ZZ+ggZZ, VH, VVV (hadronic W→qq/Z→qq excluded). Committed 8a00c6a, e79508d, 344864c. |
| v33 | `run2_bkg_dy_ht` + `run2_bkg_dy_jet`, all channels (high-stat DY: HT-binned 32 + jet-binned 12 = 44 datasets) | VALIDATED 2026-06-26 | Done ~08:43 UTC Jun 25 ("All job finished"). 440/440 dataset dirs, 1110 files. `check_v33.log`: 40 errors, **all benign `eventCount=0`** (tight channels × low-jet DY: 0Lep3FJ×13, 2Lep2FJ×5; spot-checked — intact ROOT + cutflow + genEventSumw), 0 real errors / 0 warnings. New groups in `vbsvvh_mc.py`/`samples.py` (**uncommitted**). DY sets are **alternatives** to inclusive M-50 in `run2_bkg` (stitch downstream). |
| v32 | `run3_data_2025`, all channels (new 2025 PromptReco Run3 data) | COMPLETE, validating | 400 datasets; check_v32 had 21 errors → 5 missing JSON regenerated, rest are benign `eventCount=0`. Logs in `condor/logs_v32/`, `condor/check_v32*.log`. **2025 data soft-linked into v30** (344 relative symlinks, 9 channels, 2Lep4J skipped) so `VBSVVH_skim_v30/Run3_Data_*` spans 2022–2025. |
| v31 | `2Lep4J` channel only, run2+run3 data+bkg | done | `--channels 2Lep4J`; signal forced to Sig. |
| v30 | **Full re-skim** all 6 groups × 9 channels | VALIDATED 2026-06-13 | 31,645 files, 38 TB; IDskim lepton WP + X509 fix + JetId fix. The reference "full production." |
| v29 | abandoned | — | only Run2_Data/3Lep partial; superseded by v30. |
| ≤v28 | older | complete | under `VBSVVH_skim_v26/27/28/`; v24 dirs sit directly under `skim/`. |

**Next version: v49.** Confirm scope with the user (§1) before submitting.

### §7. Traps that have each cost ~2 days — read before resubmitting anything

**(a) Changing a job split requires DELETING the task dir.**
`io_mapping` (which files go in which job) is persisted in the task's
`backup.pkl`, exactly like the executable/tarball. Re-running `submit.py` with a
different `--max-files-per-job` against an existing task dir prints the new
split in the log — "6 jobs expected" — and then silently reuses the old one.
Verify on disk, not from the log:
```bash
python3 -c "import pickle; io=pickle.load(open('<taskdir>/backup.pkl','rb'))['io_mapping']; print(len(io),'jobs')"
```
This is why TTWW 2023 × 0Lep0FJ retried the same oversized job seven times over
~50 h. Deleting the task dir made the resplit take effect and all 6 jobs
finished in ~3 h.

**(b) `MAX_FILES_PER_JOB` bounds INPUT, not OUTPUT.**
A high-acceptance channel can make a job unschedulable at a perfectly modest
file count. TTWW 2023 in `0Lep0FJ` keeps **78 %** of events, so one 52-file job
had to write **~65 GB** into a single output — it hit the 8 h wall, then
SIGSEGV'd. The 100-file cap never engaged (its split was 60 < 100). When a
dataset×channel fails repeatedly, check the acceptance before assuming the cap
covers you, and split on expected OUTPUT size.

**(c) Read completion from `io_mapping`, NEVER from the driver log.**
The Metis loop REPRINTS `jobs expected` and `Job N submitted` on every
monitoring pass (244 passes on v46), so any `grep`/`tail` over the log
double-counts and any `tac | grep -m N` can surface hours-old lines as if they
were current. This produced two false alarms: a phantom 104-job shortfall on
v46, and "10 tasks being resubmitted" that were not. The authoritative check:
```bash
python3 - <<'EOF'
import pickle, os, glob
for D in glob.glob("/blue/avery/p.chang/tasks/*_vNN_<CHANNEL>"):
    io = pickle.load(open(f"{D}/backup.pkl","rb"))["io_mapping"]
    done = sum(os.path.isfile(str(getattr(o,'name',o))) for _,o in io)
    if done < len(io): print(done, len(io), D)
EOF
```
Related: when comparing coverage, a v30 tag's `ls` count is NOT its real
dataset count — it mixes real dirs, cross-version symlinks and
`Summer24for2025` aliases. Decompose with `find -type d` vs `-type l` first.
A "195 missing datasets" claim on v30 Run3_Bkg turned out to be 135 real dirs
+ 195 links; the true gap was one dataset.

**Corollary on event counts:** `v14_nevents.py` holds *sampled estimates*
extrapolated from 2 files per sample, not DAS truth. Measured against the real
totals over 423 datasets they are off by a **median 29 %, mean 35 %, worst
170 %**. Fine for choosing a job split — that is all they are for — but never
use them for normalisation. The truth is the summed `genEventCount` /
`genEventSumw` in `runs_summary_*.json`.

### (d) "All job finished" is NOT a reliable completion signal
A dataset that is INVALID in DAS yields a task with an EMPTY `io_mapping`
(zero jobs). Metis never counts such a task as complete, so the driver loops
forever even when every real job has finished. v47's run3 driver had all
1171/1171 jobs done and still never printed "All job finished"; it had to be
killed by PID. A v46 driver was found still spinning **4 days 18 hours** after
that version was logged VALIDATED.

Poll `io_mapping` instead (see §7c for the snippet) and treat
`done == total` as the completion condition. When a watcher script waits on
the driver process to exit, it will wait forever -- poll the outputs, not the
process.

### Datasets can be INVALIDATED after you have already skimmed them
v47 found 10 DY sets producing zero jobs:
`DYto2L-2Jets_Bin-{1J,2J}-MLL-50-PTLL-{40to100,100to200,200to400,400to600,600}`
-- all now `INVALID` in DAS, yet all present with real outputs in **v30**.
Zero jobs here is correct Metis behaviour, not a failure.

Two consequences: (1) a shrinking dataset count between versions is not
automatically a bug -- check DAS status before investigating;
(2) **v30 carries events from 10 datasets that no longer exist in DAS**, which
matters for anything normalising against its DY stack. Check status with:
```bash
dasgoclient -query="dataset dataset=<DS> status=* | grep dataset.status"
```

### (e) Test with MULTI-FILE input, or per-tree bugs stay hidden
`initPerTTree` / `JetSelection::initTree` run once per input file. A fix
validated only on single-file inputs can pass every local test and then fail in
production, where jobs routinely chain 50-100 files. The jet-ID reader fix
(5a1d279) did exactly that: it segfaulted after 55 of 77 trees, and still
exited 0, so Metis logged COMPLETED-with-no-output and retried it seven times.
Always smoke-test with several input files, not one.

### (f) Never run heavy work on a login node
A 16-worker maintenance pass on `login12` held 359% CPU for 9 minutes on a
machine already at load 137 with 69 users. Use `sbatch`. Sharding keeps each
task short -- the same 16k-file pass split 20 ways ran in ~40 s per task. The
repo now carries sbatch wrappers (`*.sbatch`) for the driver, validation and
maintenance scripts; prefer QOS `avery` over `avery-b` for small jobs (the
burst queue sat 100% pending for 9 h while regular `avery` ran).

### (g) `pkill -f` matches the shell that runs it
It killed the controlling shell four times in one session. Resolve PIDs with
`pgrep` and kill them explicitly, or use `scancel --name=<jobname>`.

### (h) `make` does not track header dependencies
Editing `rapido/src/*` or any `.h` does NOT trigger recompilation of
`src/main.o`. Two separate fixes were silently not compiled in, and the
resulting debugging chased a stale binary. `touch src/main.cc` (or `make
clean`) after any header-only change, and re-run `maketar.sh`.

### Waiting for a campaign to finish, correctly
Two conditions, not one: the expected number of TASK DIRS must exist AND all
their jobs must be done. Waiting only on "jobs complete" raced badly on v48 --
a task dir had just been deleted for resubmission, so it was not counted as
outstanding, the finalize job declared victory and `scancel`'d the driver five
seconds into its dry run. Use `condor/v48_state.py`, which prints
`done total zero_job n_tasks` and **aborts loudly** if `PYTHONPATH` is missing
rather than reporting a false `0 0`.

### Validating weights, not just structure
`check.py` never looks inside `runs_summary_*.json`, so a duplicated or dropped
job silently corrupts the normalisation denominator. Run:
```bash
python3 check_weights.py VBSVVH_skim_vNN
```
It asserts (a) summed `genEventSumw` is identical across every channel of a
dataset — they read the same input files, so any spread means jobs saw the
wrong inputs — and (b) summed `genEventCount` equals the cutflow `AllEvents`.
v42: 467 MC dataset groups, 0 disagreements.

### v14 PFNano: consumed SEPARATELY, not via v30
**Decision 2026-09-30.** Read v14 from `VBSVVH_skim_v42` (signal: `v40`). It is NOT
folded into v30 and should not be: v14 tags carry the era
(`Run3_2022EE_Bkg_v14_v42_0Lep0FJ`) while v30 is flat (`Run3_Bkg_v15_v30_0Lep0FJ`), so
`link_into_skim.py` would silently skip every link; and v14 is LPC PFNano 2022/2023
while v30 is Summer24 NanoAODv15 — mixing them invites the double-counting already
flagged for v33 DY and v41 W+jets.

Staged inputs live under `/cmsuf/data/store/user/phchang/v14stage`, gated by
`.staged_<era>_<kind>` markers. Verify before any launch with
`python3 check_staged_paths.py` — it asserts every job-producing sample resolves to a
`/cmsuf` path that exists. A mis-scoped marker is silent: the executable skips xrdcp
for `/cmsuf` inputs, so a missing file kills the job with no fallback.

### Adding a new data year — FIVE places, all silent if missed
Year handling is spread across five independent spots. Missing any one still
parses the year correctly and then aborts later, so the logs show
`Year: 20NN` immediately before the failure and look unrelated:
1. `NanoCORE/Nano.cc` `Nano::ParseYear()` — campaign keywords
2. `NanoCORE/Config.cc` `GetConfigsFromDatasetName()` — the *other* year parser
3. `NanoCORE/Config.cc` `GetConfigs()` — upper bound (now removed; was `> 2025`)
4. `NanoCORE/MuonSelections.cc` `VVH::muonID()` — switch `default:` throws
5. `NanoCORE/ElectronSelections.cc` `VVH::electronID()` — same
Plus `skimmer/src/JetId.h` `getJsonPath()` (returns "" → jet IDs silently
skipped) and `LEPTON_PDS`/`HADRONIC_PDS` in `submit.py` for any new PD streams.
**Always smoke-test one real file locally before submitting a new year.**

### Open items
- **DELETE v39.** Superseded by v42. It is 95.6 % complete with 159 dataset-channels
  partial or missing, and partial event coverage is INVISIBLE to `check.py` — globbing it
  silently returns wrong statistics (e.g. ~20 % of TTto4Q in the affected channels).
- **v14 staging is complete**: all 4 eras, bkg + data, 170,459 files / 57 TB under
  `/cmsuf/data/store/user/phchang/v14stage`, gated by `.staged_<era>_<kind>` markers.
  Verify with `python3 check_staged_paths.py` before any launch.
- **v30 contains 1,191 intra-tree alias symlinks** created 2026-09-08 (`<dataset>` →
  `<dataset>Summer24for2025`), origin unknown and not from `link_into_skim.py`. A naive
  glob over a v30 channel dir double-counts those datasets.

---

## 6. Key facts (don't relearn these)

- **Submit env:** from `condor/`, `export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH`;
  system `python3` works. Must run **outside** any singularity container.
- **Metis fork:** `condor/ProjectMetis` (submodule, branch `slurm-support-py3`).
  `submit.py` is a thin driver; Metis builds task dirs under
  `/blue/avery/p.chang/tasks/SLURMTask_*`, packs sub-jobs (`--pack-size 12`),
  monitors via `squeue` + output existence, and resubmits. Worker std logs:
  `<taskdir>/logs/std_logs/`.
- **Arch:** default `--arch el9` (CMSSW_16_0_0_pre4 / el9_amd64_gcc13).
- **DAS file counts** cached in `condor/das_nevents.py`; misses query dasgoclient
  live and append (commit accumulated entries after a campaign).
- **Job splitting:** 12M events/job (SLURM). Per-sub-job: 8h, 2 GB.
- **Proxy mechanics:** Metis prefers `~/private/x509_proxy` (write it with
  `gsetupgen`), falls back to `/tmp/x509up_u$(id -u)`. X509 CA bundle is exported
  inside `slurm_executable.sh` / `slurm_packed_executable.sh` (the xrdcp-auth fix).
- **Recall related history:** memory dir has `skim-xrdcp-x509-cert-dir` and
  `metis-proxy-and-task-dir-gotchas`.

For everything else — selection definitions, the IDskim lepton WP, the
submission-machinery deep dive, past bugs — see `log.md` and `README.md`.
