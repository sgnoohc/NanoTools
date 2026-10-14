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
