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
