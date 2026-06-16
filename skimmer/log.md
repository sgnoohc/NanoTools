# VBS VVH Skimmer — Work Log

> Running context document. Newest entry first. Update whenever production state changes.

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
