# START HERE — VBS VVH Skimmer production runbook

This file auto-loads every session and is the operational entrypoint: setup,
workflow, channel definitions, the version ledger and known failure modes.

`log.md` holds the newest-first narrative history. It is deliberately NOT in
the repo (see `.gitignore`) — read it locally for full context if present.

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
  - `4LepLooseNoLH` = `4LepLoose` WITHOUT the electron `lostHits <= 1` cut
    (`VVH::IDloose4LnoLH`); electrons keep what the Veto cutBased ID allows
    (<= 2 barrel, <= 3 endcap). `IDloose4L` is built on top of it, so the two
    differ ONLY by that cut and 4LepLooseNoLH is a strict superset (+0.6-1.9%
    events). Fills `vvh_loose4lnolh_lep_p4s`. `src/Analysis_4LeptonsLooseNoLH.h`.
  - `4LepExtra` = the **standard 4Lep selection, unchanged** (`Analysis_4Leptons`), writing
    three extra whole NanoAOD collections: `IsoTrack*`, `Photon*`, `TrigObj*` (+ counters).
    Only the keep-list in `src/main.cc` differs. It reads the **4Lep matrix column**
    (`COLUMN_ALIAS` in `sample_channels.py`) and the lepton PDs, so it selects exactly the
    samples and events 4Lep does. Opt-in because TrigObj alone is tens of objects per event.
    v30 has no `4LepExtra` tag, so `link_into_skim.py` can never fold it into v30 (v54).
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
| v54 | **v30's 4Lep skim + IsoTrack/Photon/TrigObj** via NEW opt-in channel `4LepExtra` (same selection, 4Lep matrix column, lepton PDs; only the `main.cc` keep-list differs). Groups reproduce v30's four 4Lep tags: `run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_ttz_lowmass,run2_bkg_zh4l,run2_bkg_zz4l,run2_data,run3_bkg,run3_bkg_ggzz4l,run3_bkg_hh,run3_bkg_hh_bbtautau,run3_bkg_twz,run3_bkg_zh4l,run3_data`. **SEPARATE campaign, NOT linked into v30** (user request) | ✅ VALIDATED 2026-11-25 (NOT linked into v30, by request) | **Result** (`logs_v54/validate_v54.log`): 4,424/4,424 jobs, 646 tasks, 12 zero-job (INVALID in DAS: 10 DY PTLL + Summer24 single-top t-channel `TBbarQtoLNu`/`TbarBQtoLNu`, invalidated after v48; all 12 still in v30). check.py 634 ds: 691 `eventCount=0` jobs (100 ds) + 300 LHE warns, all benign; `--check-root` (225 s vs 119 s) adds nothing; check_weights 407 MC groups 0/0. **Per-dataset vs v30 4Lep (`local_v54/v30_compare.py`): 626 identical** in Events entries, genEventCount and genEventSumw, branches = v30 + IsoTrack_/Photon_/TrigObj_/nTrigObj only (45 with 0 events in both); 8 new (ZZTo4Q/ZZTo2Q2L); 0 entries/sumw/branch differences. v30 4Lep cut re-derived: 634/634 pass. **118 GB** (Run2 Bkg 56, Run3 Bkg 62, data 1). `finalize_v48.py --skim VBSVVH_skim_v54 --channel 4LepExtra`: 2 v13 bbtautau linked into the v15 tag + 157 `Summer24for2025` aliases, 0 broken. **Run 1** (launcher 52772177) stopped at 4,421/4,424: `nTrigObj` 513/522/597 > `NTRIGOBJ_MAX` 512 in Run2 UL EGamma 2018D + DoubleEG 2016G data (harmless while TrigObj was never read; `Nano::CheckBufferSizes` checks every event of every ACTIVE branch, so no finished output overflowed). Fix `3e607f6`: `NTRIGOBJ_MAX` 2048, `make cleanall` rebuild (Nano class layout changes; NanoCORE objects don't track Nano.h) -> binary `bc0fbfe8` / tarball `05555134`, bit-identical on all 8 smoke outputs. Those 2 datasets re-run whole in **run 2** (launcher 52847915, `avery-b` because `avery` was flooded by another user); old task dirs/outputs in `tasks/_moved_trigobj-v54-20261125/` and `skim/_trigobj_old-v54-20261125/` (deletable). | Dry run: **646 tasks / 4,431 jobs** (Run2 Bkg 248 = v30's 240 + 8 ZZTo4Q/ZZTo2Q2L the matrix allows but v30's 4Lep never ran; Run2 Data 86; Run3 Bkg 171; Run3 Data 141 = 2022-2025). The 10 DY PTLL sets are still INVALID in DAS -> **10 zero-job tasks expected** (the dry run shows 111 jobs for them from the stale `das_nevents.py` cache; the task build lists valid files only). New binary `3d491c77` / tarball `9ef6dcb5`. **Smoke** (3-file chains: TTZ UL18, TWZ Summer24, DoubleMuon 2018D, Muon0 2024F; `local_v54/cmp.log`): 4LepExtra vs 4Lep = identical events, 0/1210-1333 common branches differ (per-branch sums), +70-73 branches all IsoTrack_/Photon_/TrigObj_ (+nTrigObj; nIsoTrack/nPhoton were already kept via `*PV*`); new-binary 4Lep == v53 production-binary 4Lep. Requested branches all present; `Photon_pfRelIso03_chg` in Run2, `_quadratic` in Run3. Size x1.13 (Run2 MC) - x1.22 (Run3 MC); v30 4Lep is ~100 GB -> expect ~120 GB. |
| v53 | `run2_bkg_ttz_lowmass` (NEW: 4 UL eras of `TTZToLL_M-1to10` = low-mass complement of v30's `TTZToLLNuNu_M-10`) x **all 10 channels** + `run3_bkg_twz` (NEW: Summer24 `TWZ-TtoLNu-WtoLNu-Zto2L-DR1`; matrix row copied from Run2 `TWZToLL_tlept_Wlept` -> 4Lep/3Lep/2Lep2FJ/2Lep1FJ/2Lep4J); both for linking into v30 (user request) | ✅ VALIDATED + LINKED into v30 2026-11-23 | **Result:** 45/45 jobs, 0 zero-job; check.py 0 err / 0 warn (structure + `--check-root`); check_weights 0 cross-channel genEventSumw disagreements, 0 genEventCount-vs-AllEvents mismatches; branch sets identical to same-era v30 references in all 45; v30 cuts re-derived on every output pass 100%. 87 GB total (TTZ 11 GB; TWZ 2Lep4J 36 GB / 8.74M of 10.99M evts, 3Lep 23 GB, 2Lep1FJ 7.9 GB, 4Lep 8.4 GB, 2Lep2FJ 1.7 GB). `link_into_skim.py --src VBSVVH_skim_v53` -> 45 links (40 Run2_Bkg, 5 Run3_Bkg), 0 collisions, 0 broken; +5 TWZ `Summer24for2025` aliases (`fill_aliases.py`). **Gotcha:** `v48_state.py` read 45/45 while the TWZ 2Lep4J output (37.6 GB) was still being copied with no runs_summary yet -- wait for the `packed__*` jobs to exit before validating. | Dry run: 4x10 + 1x5 = **45 tasks / 45 jobs**; TTZ 2,311,000 evts (8 files), TWZ 10,992,000 evts (98 files, 1 job per channel = v30's own split for Summer24 TZQB). Same tarball as v52. **Smoke:** TTZ UL18 (3 files) x 10 ch + TWZ (3 files) x 5 ch, all rc 0, ~570 MB RSS; branch sets identical to v30 references (TTZToLLNuNu UL18 / Summer24 TZQB, same channel); re-derived v30 cuts pass 100%. Streaming smoke over xrootd stalled in 5/10 TTZ tasks (~20 s CPU in 58 min) -> re-run from xrdcp'd local copies as production does (`local_v53_inputs/`). Projection: TWZ 2Lep4J keeps 80% -> ~38 GB / ~2 h for the one job; v53 total ~93 GB. |
| v52 | `run2_bkg_zh4l` (same 4 Run2 UL `ZH_HToZZ_4LFilter_M125` ds as v50) x the **standard v30 `4Lep`** channel only (user: "v30 4 lepton skim, same setup, link back to v30") | ✅ VALIDATED 2026-11-20 | 4/4 jobs, 4 tasks, 0 zero-job, "All job finished". check: **4 ds, 0 errors, 0 warnings**; regen nothing to do; weights 4 groups 0/0; `--check-root` clean. AllEvents **2,087,361 = DAS total**; kept **197,515 (9.5%)**: UL16APV 49,990 / UL16 46,693 / UL17 49,235 / UL18 51,597. **725 MB.** Same tarball as v51 (built after `2fecfbe`, `skim` md5 identical). Smoke (UL16APV, 3 chained files) reproduced exactly by production (536,247 -> 49,990). **v30 equivalence** (`logs_v52/equiv_v52.log`): branch set identical, names+types, to v30's GluGluHToZZTo4L 4Lep output of the SAME era in all 4 eras (Events 1230/1230/1198/1280; Runs 10) -- comparing across eras falsely flags ~400 `HLT_*` (menus differ by year); re-derived v30 4Lep cut (skim-ID e+mu >= 4) passes 100%, min nSkim = 4. **Linked into v30** 2026-11-20 (`link_into_skim.py --src VBSVVH_skim_v52 --dst VBSVVH_skim_v30`): 4 relative symlinks in `Run2_Bkg_v15_v30_4Lep` (now 184 real + 52 linked = 236), 0 collisions, 0 broken. Packed job sat ~80 min PENDING (Priority) on the hard-coded `avery-b`; `scontrol update JobId=... QOS=avery` -> ran in 2 min, done in 3.5 min. |
| v51 | v14 PFNano samples added AFTER v42 (2026-11-06 index): `v14_<era>_{bkg,data}_since42` = 66 V+jets HT (W→ℓν MLNu × HT, Z→νν HT) + 28 QCD_Mu + 9 MuonEG; all default channels (MC 10, MuonEG 6 lepton) = **994 tasks / 3,792 jobs** (dry run; **4,086** after the straggler re-split) | ✅ VALIDATED 2026-11-08 — **1 known upstream exception** (QCD_PT-470to600 2022EE norm. +0.30%, see notes; **left as-is by user decision 2026-11-12**) | **Validation (`validate_v51.sbatch`, log `logs_v51/validate_v51.log`):** 4086/4086 jobs, 994/994 tasks, "All job finished". Input audit (`local_v51/dedup_leak_check.py`, from the frozen io_mappings): every task read exactly its sample's deduplicated list — 186,522 file reads, 0 missing/extra/doubled, 0 of the 29,462 dropped files. check: 994 ds, **494 benign `eventCount=0`** (117 Bkg dataset-channels, all tight channels: 4Lep 276, 2Lep2FJ 101, 2Lep1FJ 58, 0Lep3FJ 33, 3Lep 25, 2Lep4J 1; none in data; cutflows + sumw intact), 1657 jobs × 2 benign LHE warns (only the 7 pythia8 QCD_Mu bins). Weights: 0 cross-channel sumw disagreements; **10 genEventCount ≠ AllEvents = ONE bad upstream input**: `lzygala/.../QCD_PT-470to600_MuEnrichedPt5.../260921_134925/0000/MC_postEE2022_295.root` has 3 run-1 `Runs` entries (108,522 + 109,558 stale + 141,160 real; Events and LuminosityBlocks match only the last; FNAL source is the same size, so not staging) → 2022EE QCD_PT-470to600_MuEnriched genEventSumw is **+218,080 / 72,420,678 = +0.30%** in all 10 channels (job 5). **Left as-is by user decision (2026-11-12), outputs not patched.** To make it exact downstream, subtract **218,080.018** (= 108,522.009 + 109,558.009, the two stale entries) from that sample's summed genEventSumw in any channel. **Cleanup 2026-11-12:** re-split holding dirs deleted (1.7 TB outputs + 26 GB task dirs); v51 task logs stripped of the debug print, **96.7 → 0.38 GB** (`local_v51/nodebug/trim_logs.sbatch`: 602 files, 0 failures; v42–v49 logs still carry ≈ 836 GB of it). **Linked into v42** 2026-11-12 (`link_into_skim.py --src VBSVVH_skim_v51 --dst VBSVVH_skim_v42`): 994 relative symlinks in v42's matching tags, 0 collisions, 0 broken. `--check-root` (621 s vs 169 s structural, so it opened files): 0 zombie/recovered/entry-truncation errors; largest output 99.7 GB with entries == `TheEnd`. **18 TiB** (0Lep1FJ 8.6 TiB). **Stragglers 2026-11-08:** all 31 unfinished jobs were 0Lep1FJ (and one 0Lep2FJ) on high-pT QCD_Mu + 2 Z→νν HT ≥ 1500: 8 h TIMEOUTs and 12 GB pack OOMs, with 12-23M-event jobs whose outputs would pass 100 GB (§7 (k)). Moved aside + re-split at 20 files/job, `--time 24:00:00 --mem-per-subjob 4`. The 95 finished outputs > 50 GB all have entries == `TheEnd`. Also found the per-event `HLT_IsoMu22_eta2p1` debug print (since d869954) wrote 119 GB of v51 logs; removed in `2fecfbe` (A/B: outputs identical, 2.6% faster) but **v51 keeps tarball `aef0dee9`** throughout — the next version picks up `65057598`. Staged 27,292 files / 33.9 TB to `/cmsuf` via `stage_v14_par.sbatch` (60 slices, 0 failures; every destination verified present + non-empty). Dedup `v14_dedup.json` = data 22,309 + MC 7,153 drops (67 samples; MC audit: 61 samples with repeated tasks, 17,353 files read, 0 unreadable; 12 partial files in 2023 W→ℓν MLNu-0to120 HT-100to400 moved to drop = 4,493 lumis / 2.4% of that sample, the rest of that task already covered). `v14_nevents.py`: +103 probed, 0 failed; worst job ≈ 2.35× the 12M target by file size (≈4.6 h at the smoke rate). **New binary `24c45b0`** (tarball md5 `aef0dee9`): Nano.h limits raised (QCD_Mu `nGenPart` 746 > 602 aborted the smoke test; `nSV`, `nTrigObj`, `nboostedTau` also over) + **Arbusto absent-branch fix** (see §7 (j)). Smoke: MuonEG/W→ℓν/QCD_Mu/W HT-2500 worst cases all rc 0; MC outputs bit-identical across builds; MuonEG HLT bits verified per event vs inputs. Duplicate-CRAB-task files dropped via `v14_dedup.json` (`v14_dup_audit.py`). Tags line up with v42 (`Run3_<era>_<Kind>_v14_v51_<ch>`). |
| v50 | `run2_bkg_zh4l` (NEW group: 4 UL eras of `ZH_HToZZ_4LFilter_M125` powheg2-minlo-HZJ+JHUGen = Run2 counterpart of `run3_bkg_zh4l`), `--channels 4LepLooseNoLH` only (user: 4L skim with the loosest lepton ID) | ✅ VALIDATED 2026-11-02 | 4/4 jobs in ~10 min ("All job finished", 0 zero-job tasks). check: **4 ds, 0 errors, 0 warnings**; weights: 4 groups, 0 sumw disagreements, 0 cutflow mismatches; `--check-root` clean (also re-verified by hand: Events entries == cutflow pass in all 4). AllEvents **2,087,361 = DAS total**; kept **446,301 (21.4%)**, per era 20.9-21.8%. **1.6 GB.** Same tarball as v49 (`3eacd1d`, md5 verified). Smoke (UL16APV, 3 chained files) reproduced exactly by production (536,247 → 112,111); branch set identical to v49 output. ZH production ≠ the ggH `GluGluHToZZTo4L` already in v49 → complementary, no overlap. **Linked into v49** 2026-11-02 (`link_into_skim.py --src VBSVVH_skim_v50 --dst VBSVVH_skim_v49`): 4 relative symlinks in `Run2_Bkg_v15_v49_4LepLooseNoLH` (now 442 real + 4 linked), 0 collisions, 0 broken. |
| v49 | v48's 12 groups, `--channels 4LepLooseNoLH` (= 4LepLoose minus electron `lostHits <= 1`; ZZZ analysis, so counted plain-Veto electrons with 2-3 lost hits are a subset of the skim) | ✅ VALIDATED 2026-10-18 | 5611/5611 (+10 zero-job tasks = the DAS-INVALID DY PTLL sets, confirmed). check: **1033 ds** (873 + 158 era aliases + 2 v13), **1 benign `eventCount=0`** (EGamma3_Run2026C job 32: a 1-event input), 520 benign LHE warns. Weights: 762 groups, 0 sumw disagreements, 0 cutflow mismatches. `--check-root`: 0 zombie/recovered/entry mismatches. **939 GB.** **Superset of v48 verified at full scale:** identical AllEvents (62.4e9) in all 871 datasets, v49 never keeps fewer; kept 382.1M vs 375.6M = **+1.73%** (per-dataset 0.05-11.8%, median 2.3%). Code `dfd3ce2` + fat-jet fix `3eacd1d` (see v48). NOT linked into v30 (opt-in). **+4 v50 symlinks** (Run2 ZH→ZZ→4L) in `Run2_Bkg_v15_v49_4LepLooseNoLH`. |
| v48 | **Full `4LepLoose` campaign for the ZZZ analysis** (collaborator request): MC `run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_zz4l` + `run3_bkg,run3_bkg_hh,run3_bkg_ggzz4l,run3_bkg_hh_bbtautau,run3_bkg_zh4l`; data `run2_data,run3_data,run3_data_2026` | ✅ VALIDATED 2026-10-18 | 883 tasks / 5,611 jobs. Four tags: Run2_Bkg (442 ds), Run2_Data (86), Run3_Bkg (160+2 linked), Run3_Data (185, **2022-2026 in ONE dir** — both run3 data groups share the key). Group list chosen by set-cover against the real v30 4Lep listings: 0 uncovered. Run2 is the UNION of v30's 232 and v47's 394 = 442 (4LepLoose has no matrix column so it runs on hadronic samples 4Lep drops). **Run3 is 160 not 170: ten DY PTLL sets are INVALID in DAS.** `finalize_v48.py` links the 2 NanoAODv13 bbtautau ds into the v15 tag and writes the Summer24for2025 aliases (all Summer24 ds — v30 only has 131 of 170). **Validation:** 5611/5611, check 1033 ds / 1 benign `eventCount=0` (EGamma3_Run2026C job 32, 1-event input) / 520 LHE warns; weights 762 groups 0/0; `--check-root` clean; 924 GB, 375.6M events kept. **Last job (`Muon1_Run2025B`, 77 files) segfaulted on every retry:** a 44-fat-jet event overflowed JetSelection's private `JETID_NFATJET_MAX=40` (Nano.h had been bumped to 128). Fixed in `3eacd1d`; that ONE dataset was rerun with the new tarball (4LepLoose logic unchanged), old task dir in `tasks/_moved_fatjetfix_20261018/`. |
| v47 | `run3_bkg` + `run2_bkg`, `--channels 4LepLoose` (519 ds) | ✅ VALIDATED 2026-10-14 | run3 1171/1171 + run2 818/818. check: **519 ds, 0 errors**, 288 benign LHE warnings, **0 `eventCount=0`** (loose WP selects everywhere). Weights clean (0 sumw spread, 0 cutflow mismatch). **447 GB** (Run3 262.8 + Run2 184.4), vs 0.8 TB projected. Acceptance **0.596%** overall (Run2 0.661%, Run3 0.557%) = **7× tight 4Lep**, NOT the 300-440× estimated from single DY/ttbar files — that baseline had almost no real 4L events. 10 DY PTLL datasets produced 0 jobs: **INVALID in DAS** (see below). NOT linked into v30 (opt-in channel). |
| v46 | `run2_bkg,run3_bkg,run2_data,run3_data`, `--channels 2Lep4J` (756 ds) | ✅ VALIDATED 2026-10-12 | 4692/4692. check: 746 ds, 2 benign `eventCount=0`, 288 benign LHE warns. **Weight cross-check: 348/348 datasets match v30's 0Lep0FJ `genEventSumw` exactly** — same inputs, different channel/splitting. Linked into v30 (746 links). v30 now has all 10 channel tags. |
| v45 | `run3_data_parking` (59 ds ParkingHH/HH0/HH1 2023-2026), `--channels 0Lep*` | ✅ VALIDATED 2026-10-12 | 2520/2520. check: 236 ds, **1** benign `eventCount=0` (Run2024A, only 2157 events, needs >=8 jets). 4.30e9 events selected. ⚠ **59 datasets cover only 47 DISTINCT RUN SETS** — see vbsvvh_parking.py. |
| v44 | S. Ellis request: `run2_bkg_zz4l_extra`+2 existing ZZ sets → 4Lep; `run2_bkg_vg2l`,`run3_bkg_vg2l` → 2Lep1FJ | ✅ VALIDATED 2026-10-07 | 158/158. check: 49 ds, 4 benign `eventCount=0` (all ZZTo4Q in 4Lep — fully hadronic, as predicted). Weights clean. |
| v43 | 2026 PromptReco data (44 ds: EGamma0-5, Muon0-3, MuonEG × eras A-D), `--channels 4Lep` | ✅ VALIDATED 2026-10-05 | 722/722. check: 44 ds, 233 err (all benign `eventCount=0`), 0 warn. Needed year-2026 support in **five** places (see §7) + EGamma4/5 & Muon2/3 added to LEPTON_PDS. Group is channel-agnostic — re-run with `--channels` for other channels, but note it is lepton PDs only (no JetMET) and JetId 2026 falls back to the 2024 recipe. |
| v42 | **Full v14 PFNano**: bkg + data × 4 eras (8 groups, 4264 tasks / 16294 jobs) | ✅ VALIDATED 2026-10-05 | 16294/16294. check: **4264 ds, 351 errors (all benign `eventCount=0`), 740 benign LHE warnings, 0 structural**. Replaces abandoned v39. All inputs staged on /cmsuf (57 TB, 0 transfer failures). **NOT linked into v30** — see below. Final gap was TTWW 2023 × 0Lep0FJ; see §7. **+994 v51 symlinks** (2026-11-12: W→ℓν/Z→νν HT, QCD_Mu, MuonEG), so v42 now holds 4264 real + 994 linked dataset-channel dirs. |
| v41 | `run2_bkg_znunu_ht` + `run3_bkg_vjets_ht` (V+jets HT-binned, M. Mazza request; 46 ds) | ✅ VALIDATED 2026-09-15 | 1524/1524. check: 380 ds, 187 err (all benign `eventCount=0`), 0 warn, 0 OOM. Folded into v30 (334 links). ⚠ 2024 W→ℓν HT is a THIRD description of W+jets alongside the pT- and jet-binned sets in `run3_bkg` — pick one, don't sum. Z→νν is new coverage. Ran `--pack-size 6`. |
| v40 | v14 PFNano **signal**, all 4 eras (48 ds) | ✅ VALIDATED 2026-09-09 | 48/48, 0 errors, 12 benign LHE warns. 88 truth branches present. |
| v39 | v14 PFNano **background MC**, 4 eras × 9 channels | ⚠️ **95.6% — STOPPED, NOT FINISHED** | 7542 outputs; check clean (480 benign `eventCount=0`, 0 structural). **BUT 80 PARTIAL + 79 MISSING = 159 dataset-channels to redo** — partial event coverage is invisible in the files. Stopped over 407 OOM + node `/tmp` exhaustion (613-file sub-jobs). Needs a `files_per_job` cap before resuming. |
| v35 | `run3_sig_lowc2v` (8 new low-C2V signal scan points: C2V=0.25 & 0.75 @ C3=1.0 × 4 procs WWH_OS/SS/WZH/ZZH; 100 files each, main base only — AUX has no 0p25/0p75) | ✅ VALIDATED 2026-07-14 | "All job finished" 2026-07-14 01:10 UTC. **8 datasets, 40 files (5 ROOT each).** `check_v35.log`: **0 errors, 0 warnings.** ✅ **Folded into v30**: 8 relative symlinks `VBSVVH_skim_v30/Run3_Sig_v15_v30_Sig/<ds> → ../../VBSVVH_skim_v35/...` (v30 Sig now 40 = 32 real + 8 linked); brand-new datasets → **no double-counting** (unlike v33 DY). Isolated version, v32/`run3_data_2025` pattern. `cache_miss_empty` DAS warnings benign (private ceph signal not in DAS → 20 files/job default). Commits (branch `vvh_skimmer`): 0d4b251 (samples), b06588c (`run3_sig_lowc2v` group). Used existing Jul-8 tarball (Sig output identical to reverted binary; not re-tarred). |
| v34 (data) | `run2_data,run3_data` (2025 ⊂ run3_data), `--channels 2LepZ350` (lepton PDs auto-filtered: 86 + 141 = **227 unique datasets**) | ✅ VALIDATED 2026-07-08 | Folded into the v34 skim dir alongside MC. **2703 files, 1.7 GB.** check: Run2 86 datasets 0 err; Run3 141 (incl 56 Run2025) 5 benign `eventCount=0`, 0 zombie/missing. NOTE: `run3_data_2025` (72) is a FULL SUBSET of `run3_data` (190) — passing both was redundant (Metis deduped); just use `run2_data,run3_data` next time. Launch: `--samples run2_data,run3_data --version v34 --channels 2LepZ350` (source setup.sh first!). |
| v34 (MC) | `run2_bkg_ttz` + `run3_bkg_ttz`, `--channels 2LepZ350` only (ttZ boosted-Z bkg: 337 group entries → 336 unique) | ✅ VALIDATED 2026-07-08 | "All job finished". **1390 files, 97 GB.** `check_v34.log`: 336 datasets, 323 errors **all benign `eventCount=0`** (tight boosted-Z cut → 0 events in most low-rate bkg; spot-checked ggZH→Zνν: non-zombie, Runs+genEventSumw intact), 86 benign LHE warnings, 0 zombie/missing. 337→336 = duplicate `TTLL_Bin-MLL-4to50` in source run3_bkg (harmless). | Boosted-Z channel (pT(ℓℓ)≥350, OSSF, loose mass). Families: DY, **W→ℓν**, ttbar+ttbb, ttZ, ttW, ttWW, ttWZ, ttH, tZq, tWZ, WZ, ZZ+ggZZ, VH, VVV (hadronic W→qq/Z→qq excluded). Committed 8a00c6a, e79508d, 344864c. |
| v33 | `run2_bkg_dy_ht` + `run2_bkg_dy_jet`, all channels (high-stat DY: HT-binned 32 + jet-binned 12 = 44 datasets) | VALIDATED 2026-06-26 | Done ~08:43 UTC Jun 25 ("All job finished"). 440/440 dataset dirs, 1110 files. `check_v33.log`: 40 errors, **all benign `eventCount=0`** (tight channels × low-jet DY: 0Lep3FJ×13, 2Lep2FJ×5; spot-checked — intact ROOT + cutflow + genEventSumw), 0 real errors / 0 warnings. New groups in `vbsvvh_mc.py`/`samples.py` (**uncommitted**). DY sets are **alternatives** to inclusive M-50 in `run2_bkg` (stitch downstream). |
| v32 | `run3_data_2025`, all channels (new 2025 PromptReco Run3 data) | COMPLETE, validating | 400 datasets; check_v32 had 21 errors → 5 missing JSON regenerated, rest are benign `eventCount=0`. Logs in `condor/logs_v32/`, `condor/check_v32*.log`. **2025 data soft-linked into v30** (344 relative symlinks, 9 channels, 2Lep4J skipped) so `VBSVVH_skim_v30/Run3_Data_*` spans 2022–2025. |
| v31 | `2Lep4J` channel only, run2+run3 data+bkg | done | `--channels 2Lep4J`; signal forced to Sig. |
| v30 | **Full re-skim** all 6 groups × 9 channels | VALIDATED 2026-06-13 | 31,645 files, 38 TB; IDskim lepton WP + X509 fix + JetId fix. The reference "full production." |
| v29 | abandoned | — | only Run2_Data/3Lep partial; superseded by v30. |
| ≤v28 | older | complete | under `VBSVVH_skim_v26/27/28/`; v24 dirs sit directly under `skim/`. |

**Next version: v55.** Confirm scope with the user (§1) before submitting.

### §7. Known failure modes — read before resubmitting anything

**(a) Changing a job split requires DELETING the task dir.**
`io_mapping` (which files go in which job) is persisted in the task's
`backup.pkl`, exactly like the executable/tarball. Re-running `submit.py` with a
different `--max-files-per-job` against an existing task dir prints the new
split in the log — "6 jobs expected" — and then silently reuses the old one.
Verify on disk, not from the log:
```bash
python3 -c "import pickle; io=pickle.load(open('<taskdir>/backup.pkl','rb'))['io_mapping']; print(len(io),'jobs')"
```
Symptom when missed: the same oversized job is resubmitted repeatedly with no
progress. Deleting the task dir makes the new split take effect.

**(b) `MAX_FILES_PER_JOB` bounds INPUT, not OUTPUT.**
A high-acceptance channel can make a job unschedulable at a modest file count.
At 78 % acceptance a 52-file job must write ~65 GB into one output, which
exceeds the 8 h wall even though a 100-file cap never engages. When a
dataset×channel fails repeatedly, check the acceptance before assuming the cap
covers you, and split on expected OUTPUT size.

**(c) Read completion from `io_mapping`, NEVER from the driver log.**
The Metis loop REPRINTS `jobs expected` and `Job N submitted` on every
monitoring pass, so any `grep`/`tail` over the log double-counts and any
`tac | grep -m N` can surface hours-old lines as if they were current.
The authoritative check:
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

**Corollary on event counts:** `v14_nevents.py` holds *sampled estimates*
extrapolated from 2 files per sample, not DAS truth. Measured against the real
totals over 423 datasets they are off by a **median 29 %, mean 35 %, worst
170 %**. Fine for choosing a job split — that is all they are for — but never
use them for normalisation. The truth is the summed `genEventCount` /
`genEventSumw` in `runs_summary_*.json`.

### (d) "All job finished" is NOT a reliable completion signal
A dataset that is INVALID in DAS yields a task with an EMPTY `io_mapping`
(zero jobs). Metis never counts such a task as complete, so the driver loops
forever even when every real job has finished — a driver can stay alive
indefinitely after its work is complete. Stop it with `scancel --name=<job>`.

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
production, where jobs routinely chain 50-100 files. A per-tree fault can
appear only after dozens of trees, and because the wrapper still exits 0 Metis
logs COMPLETED-with-no-output and retries indefinitely. Always smoke-test with
several input files, not one.

### (f) Never run heavy work on a login node
Login nodes are shared and kill long processes. Use `sbatch`. Sharding keeps
each task short -- a 16k-file maintenance pass split 20 ways runs in ~40 s per
task. The
repo now carries sbatch wrappers (`*.sbatch`) for the driver, validation and
maintenance scripts; prefer QOS `avery` over `avery-b` for small jobs (the
burst queue sat 100% pending for 9 h while regular `avery` ran).

### (g) `pkill -f` matches the shell that runs it
`pkill -f <pattern>` matches its own command line and will kill the shell that
issued it. Resolve PIDs with `pgrep` and kill them explicitly, or use
`scancel --name=<jobname>` for SLURM jobs.

### (i) Private fixed-size branch buffers must use Nano.h's `*_MAX`
`Nano::CheckBufferSizes()` only guards Nano's own arrays. A private copy of a
limit in skimmer code drifts silently: `ObjectSelection_Jets.h` kept
`JETID_NFATJET_MAX 40` after Nano.h went to 128, and one 44-fat-jet 2025 event
overwrote the adjacent `jetIdBranches_` vector. The crash came dozens of files
later, the wrapper exited 0, and Metis retried forever (v48/v49 stuck at
5610/5611). Size any new `SetAddress` buffer with `NJET_MAX`/`NFATJET_MAX`/etc.

### (j) Arbusto: a branch missing from one file of a chain read garbage (fixed 25276d6)
An output branch cloned from the input but ABSENT from a later file in the job's
TChain kept the address shared from the previous input tree, which TChain frees on
file switch. The d869954 "reset" memset freed memory; `Fill()` then wrote whatever
reused it. Data is where this bites: HLT menus change between runs, so a job chain
crosses files with different `HLT_*` sets (158 paths differ on one 3-file MuonEG
chain). The production binary `3eacd1d` (v42–v50) wrote **695 nonzero values** for
absent paths on that chain; present paths were always correct. **Existing data skims
built before 25276d6 can carry spurious `True` for a path absent from part of a job's
run range** — not yet quantified. Fix: absent cloned branches point at an
Arbusto-owned zeroed buffer. Verify with the per-event checker pattern in log.md
2026-11-07.

### (k) A job's OUTPUT must stay well under 100 GB — ROOT's default TTree limit (v51)
`TTree::fgMaxTreeSize` defaults to 100 GB; past it `TTree::Fill` switches to a new file
`<name>_1.root`, which the wrapper never copies (it copies only `${OUTPUTNAME}.root`), so the
overflow events would be lost and Arbusto's `tfile` would point at a closed file. Not yet
observed: v51's largest outputs reached **99.7 GB** with Events entries == cutflow `TheEnd`
(0Lep1FJ on high-pT QCD_Mu keeps ~65-84%, ~12 kB/event, so a 12M-event job writes ~100 GB
and needs ~8 h). Packs also share node `/tmp` (1.6 TB) — six 150 GB outputs would fill it.
**Size jobs by expected output** (`--max-files-per-job`, now with `--time` and
`--mem-per-subjob` in `submit.py`). A truncated output is caught by `check.py --check-root`
(Events entries vs `runs_summary` eventCount vs cutflow `TheEnd`) — run it on any version
with outputs near 100 GB. v51 recovery: the 16 incomplete tasks were moved to
`tasks/_moved_resplit_v51-20261108` (outputs to `skim/_resplit_old_v51-20261108`, 1.7 TB; both
deleted 2026-11-12 after validation) and re-split at 20 files/job — see `launch_v51.sbatch`. Holding-dir names must NOT contain
`_v51_`, or the `*_v51_*` globs count them as tasks.

### (h) `make` does not track header dependencies
Editing `rapido/src/*` or any `.h` does NOT trigger recompilation of
`src/main.o`, so a header-only fix is silently not compiled in and the batch
jobs keep running the old binary. `touch src/main.cc` (or `make
clean`) after any header-only change, and re-run `maketar.sh`.

### Waiting for a campaign to finish, correctly
Two conditions, not one: the expected number of TASK DIRS must exist AND all
their jobs must be done. Waiting only on "jobs complete" races against
resubmission -- a task dir deleted for resubmission is not counted as
outstanding, so the campaign reads as finished when it is not.
Use `condor/v48_state.py`, which prints
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
Missing any one aborts every job at runtime.
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
  **Bkg alias set completed 2026-11-21** (user request): the Summer24 datasets linked in after the original
  aliasing never got one (30 per 0Lep*/1Lep1FJ/2Lep1FJ/2Lep2FJ tag, 37 in 3Lep/4Lep incl. the six ggZZ
  `GluGlu2Zto*`, all 169 in 2Lep4J). 453 added (ZH-Hto2Z 4Lep by hand + 452 via
  `local_v30_alias_fill/fill_aliases.py`; undo list `created.txt`). Every `Run3_Bkg_v15_v30_*` tag now has
  exactly one alias per `RunIII2024Summer24` dataset, 0 broken, all bare relative sibling links -- now
  1,782 aliases in v30 (counted; 1,329 before this fill -- the 1,191 above is stale); 1,787 after v53's TWZ (+5, 2026-11-23). **`Run3_Sig_v15_v30_Sig` deliberately NOT filled:** only the 3 benchmark
  couplings (c2v1p0_c3_1p0, c2v1p0_c3_10p0, c2v1p5_c3_1p0) x 4 processes are aliased, and 20 other points
  present in the same base run were skipped at the time -> a choice, not the 'added later' gap.

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
