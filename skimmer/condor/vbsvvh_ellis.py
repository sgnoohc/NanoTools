"""
Samples requested by S. Ellis for the 4L and 2L1FJ channels.
Source list: /home/sellis9.brown/mc_sample_request.txt (2026-09-28).

The request file is split into two channel sections and they are kept separate
here, because the channel matrix routing differs:

  run2_bkg_zz4l_extra   -> 4Lep     (ZZJJTo4L; the other 4L-section entries
                                     already exist, see note below)
  run2_bkg_vg2l         -> 2Lep1FJ  (Run 2: WWJJ, W/Z+gamma, TTGJets)
  run3_bkg_vg2l         -> 2Lep1FJ  (Run 3 Summer24 v15: WWJJ/WZJJ, V+gamma,
                                     TTG, DYG, EWK-2L2J)

NOT added here, deliberately:
 * ZZTo4L_TuneCP5 x4 -- the file marks these "NEW SAMPLE" but they are already
   `run2_bkg_zz4l` (added for v36) and already skimmed in 4Lep AND 3Lep, and
   linked into v30. Re-adding would duplicate them.
 * ZZTo2Q2L_mllmin4p0 x4 and ZZTo4Q_5f x4 -- already in `run2_bkg` in
   vbsvvh_mc.py. They only need a 4Lep *submission*, not a new list entry.
   NOTE ZZTo4Q is a fully-hadronic final state; the channel matrix excludes it
   from 4Lep by convention, so running it there needs an explicit matrix row.
   That is the requester's call, not an oversight.
"""

from metis.Sample import DBSSample


# ------------------------------------------------------------------
# ZZ -> 4L via VBS-like jj topology, Run 2 UL v15. 2017 has no v15
# (v9 only), so three eras, not four -- per the request file.
# ------------------------------------------------------------------
nanoaodv15_run2_bkg_zz4l_extra = [
    # --- 2016preVFP ---
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    # --- 2016postVFP ---
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    # --- 2018 ---
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
]


# ------------------------------------------------------------------
# Run 2 UL v15, for the 2Lep1FJ channel: WWJJ->lvlv (EWK+QCD and QCD-only),
# W+gamma, Z+gamma, ttbar+gamma.
# ------------------------------------------------------------------
nanoaodv15_run2_bkg_vg2l = [
    # WWJJToLNuLNu_OS_EWK_QCD_noTop
    DBSSample(dataset="/WWJJToLNuLNu_OS_EWK_QCD_noTop_TuneCP5_13TeV_madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_OS_EWK_QCD_noTop_TuneCP5_13TeV_madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_OS_EWK_QCD_noTop_TuneCP5_13TeV_madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_OS_EWK_QCD_noTop_TuneCP5_13TeV_madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WWJJToLNuLNu_QCD_noTop
    DBSSample(dataset="/WWJJToLNuLNu_QCD_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_QCD_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_QCD_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_QCD_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WGToLNuG_01J_5f
    DBSSample(dataset="/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZGToLLG_01J_5f
    DBSSample(dataset="/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTGJets
    DBSSample(dataset="/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
]


# ------------------------------------------------------------------
# Run 3 Summer24 NanoAODv15, for the 2Lep1FJ channel. Same campaign as v30's
# Run3 background. The V+gamma sets are PTG-binned: take the inclusive sample
# AND its PTG bins together only if you stitch them -- they overlap.
# ------------------------------------------------------------------
nanoaodv15_run3_bkg_vg2l = [
    # EWK-2L2J
    DBSSample(dataset="/EWK-2L2J_Bin-MLL-50-MJJ-120_TuneCH3_13p6TeV_madgraph-herwig7/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # WWJJto2L2Nu-SS-noTop-QCD
    DBSSample(dataset="/WWJJto2L2Nu-SS-noTop-QCD_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # WWJJto2L2Nu-OS-noTop-QCD
    DBSSample(dataset="/WWJJto2L2Nu-OS-noTop-QCD_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # WZJJto3LNu-EWK
    DBSSample(dataset="/WZJJto3LNu-EWK_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # WZJJto3LNu-QCD
    DBSSample(dataset="/WZJJto3LNu-QCD_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # WGtoLNuG-1Jets
    DBSSample(dataset="/WGtoLNuG-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WGtoLNuG-1Jets_Bin-PTG-100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WGtoLNuG-1Jets_Bin-PTG-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WGtoLNuG-1Jets_Bin-PTG-400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WGtoLNuG-1Jets_Bin-PTG-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # TTG-1Jets
    DBSSample(dataset="/TTG-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTG-1Jets_Bin-PTG-100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTG-1Jets_Bin-PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    # DYGto2LG-1Jets
    DBSSample(dataset="/DYGto2LG-1Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYGto2LG-1Jets_Bin-MLL-50-PTG-100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYGto2LG-1Jets_Bin-MLL-50-PTG-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYGto2LG-1Jets_Bin-MLL-50-PTG-400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYGto2LG-1Jets_Bin-MLL-50-PTG-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
]
