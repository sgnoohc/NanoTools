# VBS VVH Skimmer — Work Log

> Running context document. Newest entry first. Update whenever production state changes.

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
| **v29** | **STALLED** — only `Run2_Data_v15_v29_3Lep` (May 14). Full command saved in `condor/my_submit.sh`: `python3 submit.py --samples run2_sig,run3_sig,run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version v29` |

⚠️ **`ALL_CHANNELS` in `condor/submit.py` currently has only `3Lep` uncommented** (4Lep, 2Lep2FJ, 2Lep1FJ, 1Lep1FJ, 0Lep* are all commented out). Re-enable before a full production pass.

### New samples pending in v29 (uncommitted in `condor/vbsvvh_mc.py`)
QCD-4Jets HT-binned Summer24 NanoAODv15 added to `nanoaodv15_run3_bkg`:
HT-100to200 … HT-2000 (9 bins). **HT-40to70 and HT-70to100 intentionally skipped** (commented out).
`condor/samples.py` also has the temporary `run3_bkg_qcd4jets_test` group (just HT-100to200) — remove or keep as scratch once validated.

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

## Lepton definition update (May 21, uncommitted)

New year-agnostic **`VVH::IDskim`** WP mirroring **cmstas/run3-vbsvvh** `_looseElectrons`/`_looseMuons` (`preselection/src/selections.cpp`):
- e: pT>10, |SCη|<2.5, cutBased≥2 (Loose), barrel/endcap-split dxy/dz (0.05/0.1, 0.1/0.2)
- μ: pT>10, |η|<2.4, looseId, pfIsoId≥2, sip3d<8, dxy<0.2, dz<0.5

All 5 lepton channels' N-lepton counting cut switched from `vvh_veto_lep_p4s` → `vvh_skim_lep_p4s`. Files: `NanoCORE/Base.h`, `{Electron,Muon}Selections.{h,cc}`, `src/ObjectSelection_Leptons.h`, `src/Analysis*.h`. Binary rebuilt May 21 13:37.

⚠️ **`condor/package.tar.xz` is from May 13 — it does NOT contain the IDskim binary.** Regenerate with `condor/maketar.sh` before production. (Today's test jobs run the old definition; irrelevant for the xrdcp validation.)

Note: `vvh_lep_pt_lead/sub` (leading-lepton pT cuts) still come from the IDveto collection — counting and pT cuts use different WPs. Verify this is intended.

---

## TODO / next steps

1. ⏳ **Watch the 10 test jobs** (34384784–93). If xrdcp now works → fix validated.
2. ☐ Delete `.../tasks/SLURMTask_QCD-4Jets_..._3Lep.stale_pre_x509fix` and the test output dir + `run3_bkg_qcd4jets_test` group once validated.
3. ☐ **Regenerate `condor/package.tar.xz`** (`condor/maketar.sh`) so the IDskim lepton definition is in the shipped binary.
4. ☐ Decide channel list (`ALL_CHANNELS` in submit.py — currently 3Lep only) and **resume v29 production** via `condor/my_submit.sh` (packed, pack-size 12). The packed executable also carries the X509 fix now.
5. ☐ **Commit the uncommitted work** on `vvh_skimmer` (last commit May 13): X509 exports in both slurm executables, QCD-4Jets samples in vbsvvh_mc.py, test group in samples.py, das_nevents.py rewrite, `USEDASGOCLIENT=1` in setup.sh, submit.py tweaks, plus the NanoCORE lepton-selection / JetId.h / ObjectSelection_Leptons.h changes (separate logical commit).
6. ☐ Clean up scratch files in skimmer/ and condor/ (test*.txt, err_report*, zeroevents.txt, logger_metis.log ~2.8 GB, test.log ~1.7 GB, etc.).
