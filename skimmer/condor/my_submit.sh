# python3 submit.py --samples run2_sig,run3_sig,run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version v28

# python3 submit.py --samples run2_sig,run3_sig,run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version v29
# python3 submit.py --samples run2_sig,run3_sig,run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version v30

# v31: 2Lep4J channel only (>=2 leptons + >=4 AK4 jets). Signal groups excluded (forced to Sig channel).
# python3 submit.py --samples run2_data,run3_data,run2_bkg,run3_bkg --pack-size 12 --cpus-per-subjob 1 --version v31 --channels 2Lep4J

# v32: new 2025 PromptReco Run3 data only, all channels.
python3 submit.py --samples run3_data_2025 --pack-size 12 --cpus-per-subjob 1 --version v32

# v47 (2026-10-13/14) — 4LepLoose opt-in channel, full background campaign. VALIDATED.
# python3 submit.py --samples run3_bkg --version v47 --channels 4LepLoose --pack-size 6 --cpus-per-subjob 1
# python3 submit.py --samples run2_bkg --version v47 --channels 4LepLoose --pack-size 6 --cpus-per-subjob 1

# v48 (2026-10-18) — full 4LepLoose campaign for the ZZZ analysis (collaborator request).
# Four tags; Run3 data covers 2022-2026 in ONE directory. Submitted via sbatch, not login node.
#   MC2="run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_zz4l"
#   MC3="run3_bkg,run3_bkg_hh,run3_bkg_ggzz4l,run3_bkg_hh_bbtautau,run3_bkg_zh4l"
#   DATA="run2_data,run3_data,run3_data_2026"
#   python3 submit.py --samples "${MC2},${MC3},${DATA}" --version v48 \
#       --channels 4LepLoose --pack-size 6 --cpus-per-subjob 1
# See launch_v48.sbatch (dry-run gated) and finalize_validate_v48.sbatch.

# v49 (2026-10-18) — v48's groups with the opt-in 4LepLooseNoLH channel
# (4LepLoose minus the electron lostHits <= 1 cut; ZZZ analysis, so counted
# Veto-ID electrons with 2-3 lost hits are a subset of the skim).
#   python3 submit.py --samples "${MC2},${MC3},${DATA}" --version v49 \
#       --channels 4LepLooseNoLH --pack-size 6 --cpus-per-subjob 1
# See launch_v49.sbatch (dry-run gated) and finalize_validate_v49.sbatch.

# v50 (2026-11-02) — run2_bkg_zh4l (Run2 UL ZH_HToZZ_4LFilter, 4 eras; Run2
# counterpart of run3_bkg_zh4l) x the loosest 4L skim only (4LepLooseNoLH, the v49 channel).
#   python3 submit.py --samples run2_bkg_zh4l --version v50 \
#       --channels 4LepLooseNoLH --pack-size 6 --cpus-per-subjob 1
# See launch_v50.sbatch (dry-run gated). 4 datasets / 4 jobs.

# v52 (2026-11-20) -- run2_bkg_zh4l (same 4 Run2 UL ZH_HToZZ_4LFilter ds as v50) x the
# standard v30 4Lep channel, then linked into VBSVVH_skim_v30 (Run2_Bkg_v15_v30_4Lep).
#   python3 submit.py --samples run2_bkg_zh4l --version v52 \
#       --channels 4Lep --pack-size 6 --cpus-per-subjob 1
# See launch_v52.sbatch (dry-run gated). 4 datasets / 4 jobs.

# v53 (2026-11-23) -- run2_bkg_ttz_lowmass (Run2 UL TTZToLL_M-1to10, 4 eras; low-mass complement
# of v30's TTZToLLNuNu_M-10) x ALL default channels, + run3_bkg_twz (Summer24
# TWZ-TtoLNu-WtoLNu-Zto2L-DR1; matrix row = Run2 TWZToLL_tlept_Wlept -> 5 channels).
# Both linked into VBSVVH_skim_v30.
#   python3 submit.py --samples run2_bkg_ttz_lowmass,run3_bkg_twz --version v53 --pack-size 6 --cpus-per-subjob 1
# See launch_v53.sbatch (dry-run gated). 4x10 + 1x5 = 45 tasks / 45 jobs.

# v54 (2026-11-25) -- the v30 4Lep skim re-run with IsoTrack/Photon/TrigObj added, via the
# opt-in channel 4LepExtra (same selection, 4Lep matrix column, lepton PDs). SEPARATE
# campaign, NOT linked into v30. Groups reproduce v30's four 4Lep tags (+8 ZZTo4Q/ZZTo2Q2L).
#   python3 submit.py --samples run2_bkg,run2_bkg_dy_ht,run2_bkg_dy_jet,run2_bkg_ttz_lowmass,run2_bkg_zh4l,run2_bkg_zz4l,run2_data,run3_bkg,run3_bkg_ggzz4l,run3_bkg_hh,run3_bkg_hh_bbtautau,run3_bkg_twz,run3_bkg_zh4l,run3_data \
#       --channels 4LepExtra --version v54 --pack-size 6 --cpus-per-subjob 1
# See launch_v54.sbatch (dry-run gated). 646 tasks (10 = INVALID DY PTLL -> 0 jobs) / 4431 jobs.

# v51 (2026-11-07) — v14 PFNano samples added to the index AFTER v42 (2026-11-06 index):
# QCD_Mu + W->lnu 4Jets MLNu x HT + Z->nunu 4Jets HT (bkg), MuonEG (data); all default
# channels. Duplicate-CRAB-task files dropped via v14_dedup.json (v14_dup_audit.py).
#   python3 submit.py --samples v14_2022_bkg_since42,v14_2022EE_bkg_since42,v14_2023_bkg_since42,v14_2023BPix_bkg_since42,v14_2022_data_since42,v14_2022EE_data_since42,v14_2023_data_since42,v14_2023BPix_data_since42 \
#       --version v51 --pack-size 6 --cpus-per-subjob 1
# See launch_v51.sbatch (staging + dry-run gated). 994 tasks / 3792 jobs.
