# VBS VVH Skimmer — Work Log

> Running context document. Newest entry first. Update whenever production state changes.

---

## 2026-09-30 — v42 LAUNCHED (full v14: MC + data) + **v14 stays OUT of v30** (decision)

**DECISION (user, 2026-09-30): the v14 PFNano skims are NOT folded into v30.**
Consume them directly from `VBSVVH_skim_v42` (and `v40` for signal).

Two reasons, one structural and one physics:
- **Structural.** v14 output tags carry the era: `Run3_2022EE_Bkg_v14_v42_0Lep0FJ`,
  whereas v30 is flat: `Run3_Bkg_v15_v30_0Lep0FJ`. `link_into_skim.py` maps tags by
  substituting the version token, so v42 would target `Run3_2022EE_Bkg_v15_v30_*`,
  which does not exist — every link would silently skip. The era lives in the tag
  because `vbsvvh_v14.get_groups()` folds it into the `run` metadata field, which is
  what keeps the four eras separate in the first place.
- **Physics.** v14 is LPC PFNano at 2022/2023 conditions; v30 is Summer24 NanoAODv15.
  Different NanoAOD version, different campaign, different years. Merging them into one
  tree invites exactly the double-counting already flagged for the v33 DY and v41
  W+jets sets.

**v42 = the full v14 skim, replacing the abandoned v39.** 8 groups (bkg + data × 4
eras), **4,264 tasks / 16,289 jobs**, pack-size 6. All 62,494 MC + 107,965 data inputs
read from `/cmsuf` — no xrdcp, nothing written to node `/tmp`.

**Why a new version rather than resuming v39:** the `MAX_FILES_PER_JOB=100` cap
(`3b55589`) changed the job split for **119 of 567 datasets (21%)**. Metis decides
"done" by output-file existence, so resuming would have kept `output_1.root` written
under the old 193-files/job split while job 1 now means files 1–100 — some inputs
processed twice, others never, invisible in the files. v39 stays on disk as a fallback
until v42 validates.

**Three pre-launch gate failures, all caught before submitting:**
1. `.staged_<era>` marker claimed the whole era while only background MC was staged →
   every DATA url rewritten to a nonexistent `/cmsuf` path. The executable skips xrdcp
   for `/cmsuf`, so all 5,840 data jobs would have died with no fallback. Fixed with
   per-`(era, kind)` markers.
2. Per-kind was still too coarse: the data pass deliberately skips Tau/BTagMu (they
   route to no channel, so staging their ~10k files is pure cost), so
   `.staged_<era>_data` over-claimed for those two PDs. Fixed structurally with a
   **per-sample probe** — one stat per sample, fall back to xrootd for that whole
   sample if absent. 519 stats, ~17 s, versus 181,670 stats and minutes.
3. The gate itself was wrong: it tested the *first* sample of each group, which is
   alphabetically BTagMu — legitimately unstaged. Rewrote it as
   `condor/check_staged_paths.py`, asserting the real invariant: **every sample that
   will produce jobs resolves to a `/cmsuf` path that exists**. Final run: 499 checked,
   20 correctly skipped, 0 bad.

**Staging complete, 57 TB total**, zero failures across 170,459 files:
bkg 62,494 (44 TB) + data 107,965 (13 TB measured so far). Tau/BTagMu excluded
(~10k files) since they produce no jobs. Era 2022 averages ~710 MB/file, not the
1063 MB index-wide mean — the original 66 TB estimate was high.

---

## 2026-09-15 — ✅ v41 VALIDATED + folded into v30 (V+jets HT-binned, M. Mazza request)

**v41 = 46 datasets, 1,524 jobs, 4.17 TB.** `run2_bkg_znunu_ht` (28: Z→νν HT, Run2 UL,
7 bins × 4 eras) + `run3_bkg_vjets_ht` (18: 6 Z→νν HT + 12 W→ℓν HT, Summer24 v15).
Source lists on UAF `/home/users/mmazza/public/vjets_samples/`, pulled via `ssh uaf-2`;
all 46 re-verified against DAS — event/file counts match exactly. Commit `cf6eec2`.

**Validated:** 1,524/1,524 outputs; `check_v41`: 380 datasets, **187 errors, 0 warnings**,
all errors the benign `eventCount=0` class, **0 structural**. `regen_runs_summary`: nothing
to do. **0 OUT_OF_MEMORY** (contrast v39's 407). 66 FAILED were 1–2 s exit-1:0 deaths =
the known black-hole-node signature; Metis resubmitted and every output landed.
**Folded into v30:** 334 symlinks, 0 collisions, 0 broken (2Lep4J skipped as usual).

**⚠ Z→νν is new coverage; W→ℓν is NOT.** The repo had no Z(→νν)+jets at all — a genuinely
missing irreducible 0Lep background. But the 2024 W→ℓν HT set is the **third** parallel
description of 2024 W+jets already in `run3_bkg`, alongside `WtoLNu-2Jets_Bin-*J-PTLNu-*`
(pT-binned) and `WtoLNu-4Jets_Bin-*J` (jet-binned). **Pick one scheme; do not sum.**
Same hazard as the v33 DY merge. Further caveats in `vbsvvh_vjets.py`: HT bin edges differ
between Run 2 and 2024 (not bin-for-bin comparable), no HT<100 sample exists in any era,
and both MLNu slices of each W→ℓν HT bin are included because MLNu-0to120 alone drops
~half the events in the three highest HT bins.

**Error pattern confirms the matrix is conservative:** Z→νν produces ~nothing in the 2Lep
channels (14/28 Run2 zero in 2Lep2FJ) yet the matrix still runs them, following the existing
convention that hadronic samples keep 2Lep for heavy-flavour leptons. Those combinations are
mostly wasted; revisit as a convention change across all years, not a v41-only divergence.

**Two infrastructure bugs found and fixed while running this:**
- `cf6eec2` — **sub-job scratch was never deleted.** Inputs are xrdcp'd to
  `${SETUP_DIR}/subjob_${LABEL}` and nothing removed them; since `SLURM_TMPDIR` is `/tmp`
  here (not a per-job dir), every pack left its inputs behind. Measured during v39 at
  **1.5–1.6 TB per node, one node 100% full** — which broke our own jobs and squeezed other
  users. Now a `trap ... EXIT` removes the scratch on every exit path.
- `b349840` — **empty-channel dashboard crash.** A group with zero tasks in a channel
  (v41's all-hadronic Z→νν has none in 4Lep/3Lep) gave `StatsParser` empty data, which it
  treats as "load from disk", dying on a `summary.json` never written. The driver crashed
  **after** submitting 380 tasks, leaving 254 packs running unsupervised. Latent since the
  dashboard loop was written; only reachable once a group is excluded from a channel entirely.

---

## 2026-09-14 — 🟡 v39/v40 = NanoAODv14 LPC PFNano (partial; see caveats)

**v40 = v14 signal, ✅ COMPLETE.** 48/48 outputs (4 processes × 3 coupling points × 4 eras),
`check_v40`: 48 datasets, **0 errors**, 12 benign LHE warnings. 88 truth branches confirmed
(`--is_signal --dump_truth` works). Cutflow `AllEvents 50,000 → TheEnd 50,000` — signal is
unfiltered by design.

**v39 = v14 background MC, ⚠ 95.6% COMPLETE — STOPPED DELIBERATELY, NOT FINISHED.**
7,542 outputs across 36 tags (4 eras × 9 channels). Final `check_v39`: 3,606 datasets,
**480 errors, all benign `eventCount=0`, 0 structural**; 239 missing `runs_summary`
regenerated 239/239.

**BUT structurally clean ≠ complete.** Of 3,627 target dataset-channels:
**3,468 COMPLETE, 80 PARTIAL, 79 MISSING — 159 to redo.** The partial ones have only some
of their jobs done, i.e. **partial event coverage with nothing in the files to indicate it**
(e.g. TTto4Q 2022EE 1Lep1FJ at 2/13 jobs). Anyone globbing v39 today silently gets ~20% of
TTto4Q statistics in those channels. **Do not treat v39 as a finished sample.**

**Why it was stopped:** two compounding problems in the same giant-QCD/TT datasets —
(1) **407 OUT_OF_MEMORY** kills (24 GB/pack ÷ 12 sub-jobs = 2 GB each, against ~1 GB files
with 2,292 branches), and (2) **node `/tmp` exhaustion** from the never-deleted scratch
above, `files_per_job` targeting 12M events with no file-count cap giving **613 files ≈
650 GB for a single sub-job**. Also 9 TIMEOUTs at the 8 h wall.

**Fixes landed since:** scratch-cleanup trap (`cf6eec2`) and `/cmsuf` staging (`e7c2849`).
**Still open before any v14 re-run: a `files_per_job` file-count cap.** Staging removes the
disk pressure but not the wall-clock risk from 613-file sub-jobs.

**Staging status:** era 2022 fully staged and verified (9,305/9,305 files, 6.6 TB, 0 missing
/ 0 zero-byte / 0 failures) and `vbsvvh_v14.py` now emits `/cmsuf` paths for it, so those
jobs skip xrdcp entirely. **2022EE / 2023 / 2023BPix not yet staged** — they keep their
xrootd URLs, gated on a `.staged_<era>` marker the verifier writes only after a clean check.
Era 2022 averages ~710 MB/file, not the 1063 MB index-wide mean, so full background staging
should land near **44 TB, not the 66 TB first estimated**.

**Data groups deliberately excluded** from the campaign per user decision — 52 datasets /
117,976 files / ~612 TB, i.e. 54% of the transfer bill for 4% of the work units.

---

## 2026-08-27 — ✅ v38 VALIDATED + folded into v30 (di-Higgs — FIRST HH in this production)

**v38 = 28 HH datasets × all 10 channels = 280 jobs.** Launched 2026-08-26 17:07 ET,
"All job finished" overnight, **280/280 output files**. Commit `621fce5`.
**HH had never been in this production** — zero HH in any sample list or any skim v24–v37,
so there is NO overlap with anything pre-existing in v30.

Two groups (new module `condor/vbsvvh_hh.py`):
- **`run3_bkg_hh`** (26 ds, key `Run3_Bkg_v15_v38`) — **RunIII2024Summer24 NanoAODv15**, the
  *same campaign and nano version as v30's Run3 Bkg*, so it folds in with zero version risk:
  ggHH→bb+VV kl scan (0/1/2.45/5, c2=0, kt=1) × {2B2WtoLNu2Q (SL), 2B2Vto2L2Nu (DL), 2B2V
  (inclusive), 2B2Zto2L2Q, 2B2Zto4L} = 20; `GluGluHHto4B` same kl scan (PowhegBugFix) = 4;
  `WHH-HHto4B` + `ZHH-HHto4B` at the SM point (C2V=C3=CV=1) = 2.
- **`run3_bkg_hh_bbtautau`** (2 ds, key `Run3_Bkg_v13_v38`) — ggHH→bbττ does NOT exist in
  Summer24 v15 (only `VBFHHto2B2Tau` does), so this is **Summer22 NanoAODv13**
  `ggHH_powheg_bugfix`, kl=0 and kl=5.

**Supersedes the user's original list**, which mixed v13/v12 and two Run2 **NanoAODv2** VHH
samples. A DAS sweep found v15 equivalents for everything — *including VHH→4b in Run3*, which
was believed Run2-only. That matters: NanoAODv2/v9 are **unreadable** by this binary
(`Electron_cutBased` is `Int_t` there vs NanoCORE's `UChar_t` buffer → overrun + garbage
electron IDs, silent). v13 readability WAS verified end-to-end against the local skim binary
first (branch types, `Year: 2022`, correct `2022_Summer22` JetId JSON, sane cutflows).

**Validation.** `check_v38`: **280 datasets, 3 errors, 0 warnings**; `--check-root` identical
(0 zombie / 0 recovered). All 3 errors are `eventCount=0` on **4Lep × GluGluHHto4B** — HH→4b
has no prompt leptons. **Verified benign, not broken jobs:** all four kl points read their full
~1.96–1.99 M events; kl=1.00 selects 2 events (rare leptonic b-decays faking 4 loose leptons,
~1e-6 — right order of magnitude), the other three select 0. Flagged file is non-zombie,
`Runs`=113 entries, `genEventSumw`=197 intact. Same class as v30's 1,481 benign flags.

**Folded into v30**: **252 symlinks** — 234 from the v15 group (26 ds × 9 shared channels) plus
18 from the v13 group (2 ds × 9) using the new `--tag-subst v13=v15`. `2Lep4J` skipped both
times (not a v30 channel). 0 collisions, 0 broken.
**v30 now = 1,011 symlinks** (v32 344 + v33 396 + v35 8 + v36 10 + v37 1 + **v38 252**), 0 broken.
Reversible: `find VBSVVH_skim_v30 -maxdepth 2 -type l -lname '*v38*' -delete`.

**⚠ Caveats on the HH set, all structural:**
- **bbττ is NOT stackable with the rest** — Summer22/2022 vs Summer24/2024, different campaign
  *and* different nano version. It also has **no SM kl=1 point** in that campaign (only 0 and 5).
- **No dedicated fully-hadronic bbWW/bbZZ exists** in Summer24 v15. `GluGlutoHHto2B2V` is the
  inclusive bbVV sample and covers that phase space; treat it as such, do not sum it with the
  SL/DL samples (it contains them).
- **VBF HH deliberately excluded** (21 final states × ~10 points ≈ 210 ds), as were the 94
  `VBF-XtoHHto4B-SingletModel` resonant BSM datasets. Eight further C2V/C3/CV points per VHH
  process exist in the same campaign if the scan is ever wanted.

**`condor/link_into_skim.py` gained two flags**, both needed here: `--tag-subst OLD=NEW`
(fold a group whose nano version differs from the target's) and `--tag-filter SUBSTR` (scope a
pass to one group when a version holds several). The collision guard proved itself twice —
it refused to re-link v37, and refused the v15 tags on the second v38 pass.

---

## 2026-08-21 — ✅ v36 + v37 VALIDATED + folded into v30 (ZZ→4L set for the 4Lep study)

**Two versions, one session**, both **4Lep-only** (user's call — these are 4L final states; the
hadronic/1Lep channels would select ~0 anyway):

- **v36** = the ZZ→4L pair. `run2_bkg_zz4l` (qq→ZZ→4L powheg NLO, 4 UL eras) +
  `run3_bkg_ggzz4l` (gg→ZZ→4L mcfm Summer24, all 6 final states) = **10 datasets, 30 jobs, 3 packs**.
  Commit `89047e5`. Launched 13:03 ET, "All job finished" ~13:5x. **30/30 output files.**
- **v37** = `run3_bkg_zh4l`, the single `ZH-Hto2Z_Fil-4L` Summer24 sample (1.54M evt, 35 files,
  **1 job**). Commit `5113727`. Added mid-flight, so it needed its own version — the v36 driver had
  already imported `samples.py` and does not re-read it per loop iteration.

**Validation.** `check_v36`: **10 datasets, 0 errors, 12 warnings**; `check_v37`: **1 dataset, 0/0**.
Both passed `--check-root` (0 zombie / 0 recovered). The 12 warnings are `LHEScaleSumw has 0 entries`
+ `LHEPdfSumw is empty` on the 6 gg samples — **benign, and verified so**: the `GluGlu*Continto2Zto*`
samples *already in v30* show the identical `nLHEScaleSumw=0` (branch present, array empty). It's a
property of these mcfm gg→ZZ samples, not a skim defect. `genEventSumw` intact everywhere.
v37 cutflow: 1,541,582 → **164,335** pass 4Lep (10.7%, expected for a 4L-filtered sample).

**Folded into v30** via the new `condor/link_into_skim.py` (see below): 10 links from v36 + 1 from
v37 into `Run2_Bkg_v15_v30_4Lep` / `Run3_Bkg_v15_v30_4Lep`. 0 collisions, 0 broken.
**v30 now = 759 symlinks** (v32 344 + v33 396 + v35 8 + v36 10 + v37 1), 0 broken.
Reversible: `find VBSVVH_skim_v30 -maxdepth 2 -type l \( -lname '*v36*' -o -lname '*v37*' \) -delete`.

**⚠ Overlap — read before building a 4L stack.** Two of the three additions overlap what v30 already has:
- `ZZTo4L_TuneCP5` (v36) vs **`ZZTo4L_M-1toInf`** already in `run2_bkg` — same process, different
  gen-level m(ll) range. **Pick ONE.**
- `GluGlu2Zto*` (v36, 6 states) vs **`GluGlu{To,to}Contin{,t}o2Zto*`** already in v30 (also 6 states,
  mcfm/mcfm701) — 6-for-6. Likely continuum-only vs full gg→ZZ; **check before summing**.
- `ZH-Hto2Z_Fil-4L` (v37) vs `GluGluH-Hto2Zto4L` in v30 — **NOT an overlap**, different production
  modes (ZH vs ggH). Both belong in the stack.

Dir names differ in every case, so nothing collided on disk — the double-counting risk is purely
downstream, same shape as the v33 DY merge.

**Asymmetry note:** 4Lep-only means these 11 datasets exist in the 4Lep channel and nowhere else in
v30. A per-channel `ls`-driven stack builder will see a different bkg list in 4Lep than in the other
8 channels. Intentional, but it will bite anything that assumes a uniform sample list per channel.

**New: `condor/link_into_skim.py`** — the v32/v33/v35/v36/v37 merge, scripted instead of retyped.
Substitutes the version token to map tags (`Run3_Bkg_v15_v37_4Lep` → `..._v30_4Lep`), refuses to run
on any destination-name collision, skips empty sources and tags the target lacks, verifies all links
resolve. Dry-run by default; `--execute` writes.

**Also this session:** one-off **local** 4Lep skim of a single ZZZ UL18 file
(`c7813198-…root`, xrdcp'd from FNAL to `skimmer/local_zzz/`) → 618,000 → **2,892** pass 4Lep,
output validated (not a zombie, `genEventSumw` present, sweeproot OK). **Gotcha:** `Nano::parseYear()`
reads the year from the *file path*, so a renamed local copy (`input.root`) aborts with "Failed to
recognize which year". Keep the campaign keyword (`RunIISummer20UL18`) in the path. Note this exact
dataset is *already* fully skimmed in v30 `Run2_Bkg_v15_v30_4Lep` (all 46 files) — the local run was
a spot-check, not new coverage. The 2,892 `HLT_IsoMu22_eta2p1 branch/address missing` lines (one per
selected event) are a 2016-only trigger probed on a 2018 file — benign here.

---

## 2026-07-14 — ✅ v35 VALIDATED + folded into v30 (low-C2V Run3 signal points)

**Done.** "All job finished" 2026-07-14 01:10 UTC. All **8 dataset dirs** present under
`VBSVVH_skim_v35/Run3_Sig_v15_v35_Sig/`, 5 ROOT (output_0..4) + cutflow + runs_summary each.
`check_v35.log`: **8 datasets, 0 errors, 0 warnings** — clean (signal is high-acceptance, so
no `eventCount=0` flags unlike tight-channel bkg).

**Folded into v30** (v32/v33 mechanism): 8 relative dataset-dir symlinks
`VBSVVH_skim_v30/Run3_Sig_v15_v30_Sig/<ds> → ../../VBSVVH_skim_v35/Run3_Sig_v15_v35_Sig/<ds>`.
Pre-check 0 collisions; post-check 0 broken, all resolve to 5 real `output_*.root`. **v30 Sig
now = 40 entries (32 real + 8 linked).** **NO double-counting** — brand-new coupling points, not
alternative descriptions of existing phase space (contrast the v33 DY merge). Reversible:
`find VBSVVH_skim_v30/Run3_Sig_v15_v30_Sig -maxdepth 1 -type l \( -name '*c2v0p25*' -o -name '*c2v0p75*' \) -delete`.

---

## 2026-07-13 — 🟡 v35 RUNNING (new low-C2V Run3 signal scan points)

**v35 = 8 new Run3 signal coupling points** added to the C2V/C3 scan: **C2V=0.25** and
**C2V=0.75**, both at **C3=1.0**, each covering all 4 VBS VVH processes (VBSWWH_OS,
VBSWWH_SS, VBSWZH, VBSZZH). Source: aaarora's `run3-vbs-signal-shared/signal_4f_Inclusive`
(**main** base) Run3Summer24, leaf `VBS{proc}_C2V_{0p25,0p75}_C3_1p0_13p6TeV_4f_LO_TuneCP5`,
100 files each (verified on uaf-2 ceph). The **AUX base has NO 0p25/0p75** points, so no
`_ext1` variants (unlike the 1p0/1p5/2p0/10p0 grid).

**How added:** 8 `_make_run3_sig(...)` lines in `nanoaodv15_run3_sig` (`vbsvvh_mc.py`,
commit 0d4b251), then an isolated group `run3_sig_lowc2v` in `samples.py` (filtered from
run3_sig by `c2v0p25`/`c2v0p75`, commit b06588c) so a dedicated version skims ONLY these 8
— the v32/`run3_data_2025` pattern. Plan: after "All job finished" + check.py, **fold into
v30 via symlink** (like v32 data / v33 DY) into `Run3_Sig_v15_v30_Sig/` (these are brand-new
datasets — NO double-counting, unlike the v33 DY merge). v30 already has the other 32
run3_sig points.

**Launch:** `submit.py --samples run3_sig_lowc2v --version v35 --pack-size 12
--cpus-per-subjob 1`, detached 2026-07-13 20:59 UTC (PID 815421, `logs_v35/submit_v35.log`).
Dry-run first confirmed 8 datasets × 5 jobs = 40 jobs → 4 packs, tag `Run3_Sig_v15_v35_Sig`.
`cache_miss_empty` DAS warnings benign (private ceph signal not in DAS → 20 files/job default).
Used existing Jul-8 `package.tar.xz` (Sig-channel output identical to the reverted binary; not
re-tarred). Proxy valid to ~Jul 15.

**Branch note:** done on `vvh_skimmer`, which was reset back to 7e9f7cf (pre-2LepZ350) earlier
this session per user — the whole 2LepZ350 feature (4 commits + the uncommitted pT-cut fix,
incl. the v34 log entry) was parked on branch `z350` (tip 83401c7). The `skim` binary was
rebuilt from the reverted tree. (v34 production on disk is unaffected/validated; only its log
narrative now lives on `z350`.)

---

## 2026-06-26 — ✅ v33 VALIDATED (high-stat DY for Run2)

**v33 = high-statistics DY alternatives for Run2 Bkg**, two new sample groups skimmed across all 10 channels:
- `run2_bkg_dy_ht` — `DYJetsToLL_M-50_HT-*` madgraphMLM LO, 8 HT bins × 4 UL eras = **32 datasets**
- `run2_bkg_dy_jet` — `DYJetsToLL_{0,1,2}J` amcatnloFXFX NLO, 3 bins × 4 eras = **12 datasets**

Motivation: the inclusive `M-50` madgraphMLM in `run2_bkg` has almost no stats in the high-jet / multi-b-jet tail. HT-binned (and jet-binned) populate that phase space ~10–100× better. **These are ALTERNATIVES to inclusive M-50 (same process)** — must stitch / pick one scheme downstream; do not add on top of inclusive without handling double-counting. No b-enriched DY exists in the UL NanoAODv15 campaign (no `BGenFilter`/`DYBBJets`); `BTVNanoV15` variants are different NanoAOD content, not for this.

Added the two list vars to `condor/vbsvvh_mc.py` and registered groups `run2_bkg_dy_ht` / `run2_bkg_dy_jet` in `condor/samples.py` (**uncommitted**). Launched 2026-06-25 01:52 ET (05:52 UTC) detached, log `condor/logs_v33/submit_v33.log`; "All job finished" ~04:43 ET (08:43 UTC) Jun 25. **440/440 dataset dirs, 1110 output files.**

Validation (`condor/check_v33.log`): 440 datasets, **40 errors — all benign `eventCount=0`**, 0 real errors, 0 warnings. Flags concentrate in tight channels for low-jet DY (0Lep3FJ ×13, 2Lep2FJ ×5). Spot-checked one (0Lep3FJ × DY HT-70to100 preVFP): cutflow `AllEvents=6.72M → AtLeast3FatJets=0 → TheEnd=0`, ROOT non-zombie, `Events`=0 / `Runs`=9 entries, `genEventSumw` + LHE/PS weights intact — genuine 0-selected, not a broken job. **v33 is analysis-ready.**

Open: commit the `vbsvvh_mc.py` + `samples.py` group additions (on branch `vvh_skimmer`).

---

## 2026-06-27 — v33 DY soft-linked into v30 (⚠ overlaps inclusive DY)

Linked v33's high-stat DY (HT-binned + jet-binned) into the v30 tree, same mechanism as the v32 merge: **396 relative symlinks** (`../../VBSVVH_skim_v33/...`), 44 datasets × the **9 channels shared by v30 and v33** (`2Lep4J` skipped — not a v30 channel). Precheck 0 collisions / 0 empty; post-check 0 broken, all resolve to real `output_*.root`.

**⚠ Double-counting, unlike the v32 merge:** `Run2_Bkg_v15_v30_*` already holds the inclusive `DYJetsToLL_M-50` (madgraphMLM). It now ALSO holds the HT-binned (`DYJetsToLL_M-50_HT-*`) and jet-binned (`DYJetsToLL_{0,1,2}J_*`) alternatives — three overlapping DY descriptions of the same phase space. Downstream must stitch or pick ONE scheme; globbing all DY in v30 triple-counts. GenXSecAnalyzer cross sections for the binned sets: `condor/xsec_dy.json`. Reversible: `find VBSVVH_skim_v30 -maxdepth 2 -type l \( -name 'DYJetsToLL_*HT-*' -o -name 'DYJetsToLL_[012]J_*' \) -delete`.

---

## 2026-06-25 — v32 2025-data soft-linked into v30

Merged v32's new 2025 PromptReco Run3 data into the v30 tree so `VBSVVH_skim_v30/Run3_Data_*` spans 2022–2025: **344 relative symlinks** (`../../VBSVVH_skim_v32/...`), one per v32 dataset dir, across the **9 channels shared by v30 and v32** (hadronic 16 + leptonic 56 each). `2Lep4J` skipped (exists in v32 but not v30; its 2022–24 data lives in v31). Precheck clean: 0 collisions (different run eras), 0 empty targets; post-check 0 broken links, all resolve to real `output_*.root`. Reversible: `find VBSVVH_skim_v30 -maxdepth 2 -type l -delete`. Note: a future `check.py`/dashboard walk of v30 will now include the linked 2025 data.

---

## 2026-06-13 — ✅ v30 VALIDATED (both check passes clean)

`check.py --skim-name VBSVVH_skim_v30` (metadata) + `--check-root` (opens every file):
- **0 zombie / 0 recovered** across all 31,645 ROOT files; all Data + Sig channels fully OK.
- 21 missing `runs_summary_N.json` found → **regenerated** via `regen_runs_summary.py --execute` (rebuilds from the ROOT Runs tree); re-verified 0 missing.
- 1,481 `eventCount=0` flags = **benign**: tight channel × soft sample (e.g. QCD × 4Lep) where 0 selected events is expected; cutflow `AllEvents` and `genEventSumw` intact in every case. (check.py improvement idea: only flag when `eventCount != cutflow TheEnd`.)
- 2,209 LHE-weight warnings = benign (pythia8-only samples carry no LHEScale/LHEPdf weights; 8-vs-9 scale entries = aMC@NLO quirk).
- Logs: `condor/check_v30.log`, `condor/check_v30_root.log`. Note: `python3 -u` needed for live output; the first `--check-root` attempt died silently ~15 min in (cause unknown, not reproduced — second run flat at 0.6 GB RSS).

**v30 is analysis-ready.**

---

## 2026-06-12 — ✅ **v30 PRODUCTION COMPLETE**

**All 31,645 jobs done (100%, 0 incomplete tasks)** — "All job finished", loop exited cleanly. **31,645 output files (1:1 with jobs), 38 TB** in `VBSVVH_skim_v30/`. Wall-clock: ~19 h (launched Jun 11 11:41). The black-hole node exclusion (below) cleared the retry tail within ~1 h of the restart.

Post-production checklist:
- ☐ Commit `das_nevents.py` cache additions + final `log.md` + node-exclusion in submit.py; **push** everything (parent + ProjectMetis submodule)
- ☐ Remove/revisit the 17-node `exclude` list in submit.py before the *next* production (nodes may be fixed by then); consider reporting the list to UFRC
- ☐ Delete QCD-4Jets test artifacts + `run3_bkg_qcd4jets_test` group
- ☐ Truncate `logger_metis.log` (3.1 GB) + scratch cleanup
- ☐ Proxy renewal Jun 18 no longer needed for v30

---

## 2026-06-12 — Black-hole nodes: 49% pack failure rate; excluded 17 nodes, loop restarted

Overnight v30 stats: **1,618 packs COMPLETED vs 1,558 FAILED** (+41 OUT_OF_MEMORY). ~30.8k output files already on disk (bulk of production done!), but ~1,250 jobs stuck in retry loops (732 at 5 retries).

**Diagnosis:** failed packs die in 0–1 s, exit 1, no logs. That's the packed executable's startup filesystem health check (`timeout 120 ls <logdir>`) failing *instantly* — `/blue` not mounted / autofs flaky on specific nodes. Instant failure frees the node → scheduler feeds it the next pack → "black hole": c0703a-s21 alone consumed 194 packs (91% fail), c0703a-s6 106/106 (100%). ~17 nodes at ≥70% failure rate (c0702a/c0703a/c0704a/c0705a/c0707a racks). No Metis retry cap, so nothing lost — just wasted submissions.

**Fix applied:** `--exclude` of the 17 nodes via `extra_directives={"exclude": ...}` in submit.py's `PackedSLURMSubmitter` (plumbing already existed in Metis `Utils.slurm_submit_packed`). Old loop killed, log rotated to `submit_v30.log.1`, loop relaunched (same command). **Remove the exclusion once UFRC fixes the nodes** — and consider reporting the node list to UFRC.

How to re-derive the bad-node list:
```bash
sacct -u p.chang -S <start> -X --noheader -o State,NodeList%30 \
 | awk '{t[$2]++; if($1=="FAILED")f[$2]++} END{for(n in f) if(f[n]>=15 && f[n]/t[n]>=0.70) print n}' | sort | paste -sd,
```
Retry counts per job: parse `~/public_html/Run*_v15_v30/*/web_summary.json` → `tasks[].bad.jobs_not_done[].retries`.

Watch item: the 41 OOM packs (24 GB / 12 sub-jobs is tight for some samples) — if the same jobs keep OOMing, bump `memory` or repack them with smaller pack-size.

---

## 2026-06-11 (pm) — Test complete; **v30 PRODUCTION LAUNCHED**

**v30 launched 11:41** — all 6 groups, all 9 channels, packed (pack-size 12):
- Process: detached `python3 submit.py ... --version v30` (setsid, survives logout), log: `condor/submit_v30.log`
- Smoke tests passed first: 2Lep1FJ (3.35M evts → 125,839 ≥2 IDskim leptons → 688 final) and 0Lep1FJ (1.48M → 27,670) on local UL2016 SingleMuon files, fixed binary, sane cutflows, exit 0.
- Tarball md5-verified to contain the tested binary.
- Outputs: `/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_v30/`; dashboards: `http://login12.ufhpc/~p.chang/Run{2,3}_{Bkg,Data,Sig}_v15_v30/<channel>`
- To stop: `kill <pid of python3 submit.py --version v30>`; to resume after a crash: rerun `condor/my_submit.sh` (Metis picks up where outputs left off).

**QCD-4Jets test: DONE.** 10/10 outputs on `/cmsuf`, Metis monitor exited "All job finished". X509 fix fully validated end-to-end. v29 final tally: only Run2_Data/3Lep complete (86/86 datasets, 635 files) = ~13% of its 3Lep-only scope; superseded by v30.

**v30 production (all channels):**
- `ALL_CHANNELS` in `condor/submit.py`: all 9 channels re-enabled (was 3Lep-only).
- `condor/my_submit.sh` bumped to `--version v30` (packed, pack-size 12).
- Rebuilt `skim` binary (el9 / CMSSW_16_0_0_pre4) + regenerated `condor/package.tar.xz` via `condor/maketar.sh` — now ships the IDskim lepton definition and JetId updates.
- Proxy: `~/private/x509_proxy` refreshed today, valid to Jun 18. **Renew with `gsetupgen` before it expires — production will run past that.**
- Smoke test: local 2-file SingleMuon run via `test.sh` before launch.

**Committed (not pushed), 2026-06-11:**
- `dec87a8` — IDskim lepton WP + channel counting switch + Nano.h `Electron_cutBased` UChar_t fix
- `2840d43` — JetId bitmask convention fix (0/2/6, matches NanoAOD `Jet_jetId`)
- `8efc947` — X509 CA exports in SLURM executables, QCD-4Jets HT samples, das_nevents rewrite, `USEDASGOCLIENT=1`, my_submit.sh + log.md tracked, submodule bump
- `a5b3a4d` (in `condor/ProjectMetis`, branch `slurm-support-py3`) — packed-status scan speedups, shared-FS proxy preference

Note: `das_nevents.py` re-dirties itself while production runs (live DAS cache appends) — commit the accumulated entries at the end.

**🐛 Bug found & fixed by the smoke test:** the new `electronIDskim()` crashed (`std::out_of_range`) on the first event with an electron. Root cause: `Electron_cutBased` is **UChar_t** on disk since NanoAODv12, but `NanoCORE/Nano.h` declared the read buffer `int[]` — `bytes/sizeof(int)` undercounts 4× (0 elements for <4 electrons → empty vector). The May 21 binary had this latent crash and was never locally tested. Fix: buffer type → `UChar_t` in `Nano.h:304` (public `vector<int>` API unchanged, values convert on copy). Audited the other skim-path branches: `Muon_pfIsoId` (UChar_t), `Muon_looseId` (bool), and the custom Jet/FatJet multiplicity readers in `ObjectSelection_Jets.h` (UChar_t/Short_t) all already match the file types. Rebuilt + re-tarred after the fix.

---

## 2026-06-11 — Resubmitted QCD-4Jets test with X509 fix (**FIX VALIDATED**)

**Update 10:45:** first job (34384789) passed the xrdcp stage cleanly — "After XRootD copy" reached with **0 auth failures and 0 retries across all 10 jobs**. Previously every job died on xrdcp attempt 1 with "Auth failed". The X509_CERT_DIR fix works. Remaining: let the skims finish (monitor loop will resubmit any unrelated failures), then proceed with TODO list below.

### What is running right now

- **10 test skim jobs** for `/QCD-4Jets_Bin-HT-100to200.../RunIII2024Summer24NanoAODv15.../NANOAODSIM`, tag `Run3_Bkg_v15_test_qcd4jets_3Lep`, SLURM job IDs **34384784–34384793** (submitted 2026-06-11 10:21, unpacked mode, 17 files/job).
- The `submit.py` monitor loop is running in the background, logging to
  `skimmer/condor/resubmit_test_qcd4jets_20260611.log`.
- Dashboard: http://login12.ufhpc/~p.chang/Run3_Bkg_v15_test_qcd4jets/3Lep
- Outputs land in `/cmsuf/data/store/user/phchang/skim/VBSVVH_skim_test_qcd4jets/Run3_Bkg_v15_test_qcd4jets_3Lep/...`

**Purpose of this test:** validate the X509_CERT_DIR fix (see 2026-05-28 entry). The previous attempt of these exact 10 jobs died 6–7 times each at `xrdcp` with "Auth failed" / ztn fallback.

**How to check success:** once jobs run, look at
`/blue/avery/p.chang/tasks/SLURMTask_QCD-4Jets_..._test_qcd4jets_3Lep/logs/std_logs/` —
xrdcp should copy inputs cleanly (no "Auth failed", no "ztn"). Output ROOT files appearing in the `/cmsuf` output dir = success.

### What was done today

1. Found a **fresh VOMS proxy** at `/tmp/x509up_u130049` (made 09:38 today via `gsetup`, valid to Jun 18, full `/cms` attributes). `~/private/x509_proxy` (what Metis actually uses) had **expired Jun 3**. Copied tmp proxy → `~/private/x509_proxy`.
2. Moved the stale failed task dir aside (it had the **unpatched** executable baked in, and `prepared_inputs=True` persisted in `backup.pkl` means Metis would NOT re-copy the patched one — `recopy_inputs` is commented out in submit.py):
   `/blue/avery/p.chang/tasks/SLURMTask_QCD-4Jets_..._test_qcd4jets_3Lep.stale_pre_x509fix`
   (safe to delete once the test passes)
3. Dry-run, then resubmitted:
   ```bash
   cd skimmer/condor
   export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH
   python3 submit.py --samples run3_bkg_qcd4jets_test --version test_qcd4jets
   ```
4. Verified the regenerated task dir: `executable.sh` now exports `X509_CERT_DIR` (line 24) and `logs/x509up_proxy` is today's proxy.

---

## 2026-05-28 — Root-caused the xrdcp auth failures, patched executables

**Symptom:** all 10 QCD-4Jets test jobs died repeatedly (6–7 resubmissions by May 26) at `xrdcp`, with "Auth failed": the xrootd 5.x client fell back to `ztn` ("non-TLS" auth rejected).

**Root cause:** worker jobs had a valid proxy (Metis stages `~/private/x509_proxy` → `<taskdir>/logs/x509up_proxy` → worker) but **no grid CA bundle** — `X509_CERT_DIR` was unset on SLURM workers, so GSI server-cert verification failed. The interactive `hpggsetup*` aliases in `~/dot/mybashrc` set these, but batch jobs never got them.

**Fix (applied, uncommitted):** both `condor/slurm_executable.sh` and `condor/slurm_packed_executable.sh` now export, right after the staged-proxy block:
```bash
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir
```

**Gotcha to remember:** each Metis task dir bakes its own copy of `executable.sh` at first `process()`, and `prepared_inputs` is persisted in `backup.pkl` — so executable changes do NOT propagate to existing task dirs. Either delete/move the task dir, or enable `recopy_inputs=True` in submit.py's `common_kwargs`.

---

## Production state

| Version | Status |
|---|---|
| v24 | Run3 Bkg/Data/Sig complete (March 2026), dirs like `Run3_Bkg_v15_v24_<channel>` directly under `/cmsuf/.../skim/` |
| v26, v27 | older, under `VBSVVH_skim_v26/27` |
| v28 | complete: Run2+Run3 × Bkg(9ch)/Data(9ch)/Sig under `VBSVVH_skim_v28/` |
| v29 | abandoned — only `Run2_Data_v15_v29_3Lep` (86/86 datasets, May 14; ran with a *local-only* 3Lep channel restriction and the old IDveto-counting binary). Superseded by v30. |
| **v30** | **IN PROGRESS** (launched 2026-06-11 11:41) — all 6 groups × all 9 channels, packed (pack-size 12), IDskim binary, X509 fix. Loop: detached `submit.py` PID logged in `condor/submit_v30.log`. |

(Resolved 2026-06-11: `ALL_CHANNELS` is back to all 9 channels — turns out HEAD always had them; the 3Lep restriction was an uncommitted local edit. The QCD-4Jets HT samples are committed in `8efc947`; HT-40to70 and HT-70to100 intentionally skipped. The temporary `run3_bkg_qcd4jets_test` group in samples.py can be removed now that the fix is validated.)

---

## How the submission machinery works (ProjectMetis)

Everything runs through the **ProjectMetis fork** at `condor/ProjectMetis` (submodule, branch `slurm-support-py3`); launch with `PYTHONPATH=$PWD/ProjectMetis` from `condor/`. `submit.py` is only a thin driver (sample registry, channel/PD filtering, DAS-cache job splitting, 2500-job throttle) — Metis does the rest:

1. **Task instantiation** — each dataset × channel becomes a `SLURMTask` (extends `CondorTask`): builds the input-files → output-file `io_mapping`, creates the task dir under `/blue/avery/p.chang/tasks/SLURMTask_*`, bakes `executable.sh` + `package.tar.gz` + staged proxy into it (state persisted in `backup.pkl`).
2. **Submission** — with `--pack-size 12`, tasks don't submit themselves; `PackedSLURMSubmitter` collects all pending sub-jobs across tasks, bundles 12 per SLURM allocation (one `sbatch` each: account `avery`, QOS `avery-b`, partition `hpg-default`, 8h, 2 GB/sub-job), and writes `packed_<jobid>.manifest` in each task's logdir mapping sub-jobs back to tasks.
3. **Monitoring/recovery loop** — every 600 s the driver re-walks all tasks: Metis checks `squeue` (one cached query) + output existence on `/cmsuf`, marks done outputs, **resubmits anything missing or dead** (this is what re-stages a renewed proxy automatically), and exits only when every task is complete ("All job finished").
4. **Dashboards** — `StatsParser` writes `web_summary.json` per channel under `~/public_html/<unique_key>/<channel>` → `http://login12.ufhpc/~p.chang/...`.

---

## Skim selection overview (v30 binary)

Object collections built once per event (`src/Analysis.h`):

| Collection | Definition | Used for |
|---|---|---|
| `vvh_skim_lep_p4s` | e/μ passing `VVH::IDskim` (mirrors run3-vbsvvh loose) | N-lepton counting cut |
| `vvh_veto_lep_p4s` | e/μ passing year-specific `VVH::IDveto` | only `vvh_lep_pt_lead/sub` |
| `n_vvh_veto_jets` | AK4 jets pT > 15 (no η cut / jet ID / overlap removal) | N-jet cuts |
| `n_vvh_veto_fatjets` | AK8 jets pT > 200, m_softdrop > 20 (no η cut) | N-fatjet cuts |

Per-channel cuts (all "≥", no vetoes; each channel = separate skim pass via `-a <tag>`):

| Channel | N(IDskim lep) | lead-lep pT | N(AK8) | N(AK4) |
|---|---|---|---|---|
| 4Lep | ≥4 | — | — | — |
| 3Lep | ≥3 | ≥20 | — | — |
| 2Lep2FJ | ≥2 | ≥20 | ≥2 | — |
| 2Lep1FJ | ≥2 | ≥20 | ≥1 | — |
| 1Lep1FJ | ≥1 | ≥20 | ≥1 | — |
| 0Lep3FJ | — | — | ≥3 | — |
| 0Lep2FJ | — | — | ≥2 | — |
| 0Lep1FJ | — | — | ≥1 | ≥5 |
| 0Lep0FJ | — | — | — | ≥8 |
| Sig | dummy cut (all events kept) | | | |

Cross-WP quirk (known, unresolved): counting uses IDskim but lead-lep pT comes from the IDveto collection; neither WP is a strict superset of the other (IDskim μ has looser dxy/dz but requires looseId+pfIsoId).

---

## Key infrastructure notes

- **Proxy:** Metis (`ProjectMetis/metis/Utils.py:get_proxy_file`) prefers `~/private/x509_proxy`, falls back to `/tmp/x509up_u$(id -u)`. Alias `gsetupgen` writes to `~/private/x509_proxy` (use this one!); plain `gsetup` only writes `/tmp`. Staged task proxy auto-refreshes at submit time if `~/private/x509_proxy` is newer. Proxies last 168h = 7 days.
- **Grid tools on HPG login nodes:** `voms-proxy-info` etc. need
  `source /cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.6/current/el9-x86_64/setup.sh` (= `hpggsetupel9` alias).
- **Submission env:** `cd skimmer/condor && export PYTHONPATH=$PWD/ProjectMetis:$PYTHONPATH`; system python3 works. `setup.sh` (repo root of skimmer/) sets CMSSW + `USEDASGOCLIENT=1` (DAS via dasgoclient instead of flaky-from-HPG UCSD DIS).
- **DAS file counts** cached in `condor/das_nevents.py` (rewritten/slimmed, uncommitted); cache misses query dasgoclient live and append to the file.
- **Job splitting:** 12M events/job target for SLURM (`MIN_EVENTS_PER_JOB_SLURM`), 3M for condor.
- **Throttle:** `MAX_SUBMITTED = 2500` (avery-b QOS limit is 3000).
- **Task dirs:** `/blue/avery/p.chang/tasks/SLURMTask_*`. Worker std logs in `<taskdir>/logs/std_logs/`.
- **`msummary: command not found`** in submit logs is harmless (dashboard summary helper not in PATH); dashboards still update.

---

## Lepton definition update (May 21; committed `dec87a8` 2026-06-11)

New year-agnostic **`VVH::IDskim`** WP mirroring **cmstas/run3-vbsvvh** `_looseElectrons`/`_looseMuons` (`preselection/src/selections.cpp`):
- e: pT>10, |SCη|<2.5, cutBased≥2 (Loose), barrel/endcap-split dxy/dz (0.05/0.1, 0.1/0.2)
- μ: pT>10, |η|<2.4, looseId, pfIsoId≥2, sip3d<8, dxy<0.2, dz<0.5

All 5 lepton channels' N-lepton counting cut switched from `vvh_veto_lep_p4s` → `vvh_skim_lep_p4s`. Files: `NanoCORE/Base.h`, `{Electron,Muon}Selections.{h,cc}`, `src/ObjectSelection_Leptons.h`, `src/Analysis*.h`.

(Resolved 2026-06-11: binary + `package.tar.xz` rebuilt with the IDskim definition and the `Electron_cutBased` UChar_t fix; v30 ships it. The May 21 binary was never tested and carried a latent crash — see the bug note in the v30 entry.)

Note: `vvh_lep_pt_lead/sub` (leading-lepton pT cuts) still come from the IDveto collection — counting and pT cuts use different WPs. Verify this is intended.

---

## TODO / next steps

1. ✅ Test jobs validated (10/10 complete, X509 fix works).
2. ✅ Tarball regenerated with IDskim binary (+ UChar_t fix).
3. ✅ All channels enabled; **v30 launched** (supersedes v29 resume).
4. ✅ Pending work committed (`dec87a8`, `2840d43`, `8efc947` + submodule `a5b3a4d`).
5. ⏳ **Babysit v30**: watch `condor/submit_v30.log` + dashboards; **renew proxy with `gsetupgen` before Jun 18**.
6. ☐ **Push** the four commits (parent repo + ProjectMetis submodule) when ready.
7. ☐ Commit the `das_nevents.py` cache entries accumulated during v30.
8. ☐ Delete test artifacts: `.../tasks/SLURMTask_QCD-4Jets_..._3Lep{,.stale_pre_x509fix}`, `/cmsuf/.../VBSVVH_skim_test_qcd4jets/`, and the `run3_bkg_qcd4jets_test` group in samples.py.
9. ☐ Clean up scratch files in skimmer/ and condor/ (test*.txt, err_report*, zeroevents.txt, logger_metis.log ~2.8 GB, test.log ~1.7 GB, etc.).
10. ☐ Decide whether lead-lep pT should also use IDskim (cross-WP quirk above).
