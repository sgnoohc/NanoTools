# Sample-channel matrix: 1 = run, 0 = skip
# Edit the flags to toggle which channels each MC sample runs on.
# Unlisted samples default to running on all channels.

CHANNELS = ["4Lep", "3Lep", "2Lep2FJ", "2Lep1FJ", "1Lep1FJ",
            "0Lep3FJ", "0Lep2FJ", "0Lep1FJ", "0Lep0FJ"]

SAMPLE_MATRIX = {
    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTToHadronic
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"                                             : "0  0  1  1  1  1  1  1  1",
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"                                              : "0  0  1  1  1  1  1  1  1",
    "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"                                              : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTToSemiLeptonic
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"                                         : "0  1  1  1  1  1  1  1  1",
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"                                          : "0  1  1  1  1  1  1  1  1",
    "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"                                          : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT50to100
    "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                      : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                 : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT100to200
    "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT200to300
    "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT300to500
    "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT500to700
    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT700to1000
    "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                    : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT1000to1500
    "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                   : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                             : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                              : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                              : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT1500to2000
    "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                   : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                             : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                              : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                              : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # QCD_HT2000toInf
    "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                    : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ttHTobb
    "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                   : "1  1  1  1  1  1  1  1  1",
    "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                              : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ttHToNonbb
    "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                : "1  1  1  1  1  1  1  1  1",
    "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                          : "1  1  1  1  1  1  1  1  1",
    "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                           : "1  1  1  1  1  1  1  1  1",
    "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                           : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTWJetsToQQ
    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                      : "1  1  1  1  1  1  1  1  1",
    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                : "1  1  1  1  1  1  1  1  1",
    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTWW
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                         : "1  1  1  1  1  1  1  1  1",
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                   : "1  1  1  1  1  1  1  1  1",
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTWZ
    "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                         : "1  1  1  1  1  1  1  1  1",
    "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                   : "1  1  1  1  1  1  1  1  1",
    "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ST_t-channel_top_4f_InclusiveDecays
    "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"    : "1  1  1  1  1  1  1  1  1",
    "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"              : "1  1  1  1  1  1  1  1  1",
    "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"               : "1  1  1  1  1  1  1  1  1",
    "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"               : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ST_t-channel_antitop_4f_InclusiveDecays
    "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM": "1  1  1  1  1  1  1  1  1",
    "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"          : "1  1  1  1  1  1  1  1  1",
    "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"           : "1  1  1  1  1  1  1  1  1",
    "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"           : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ST_tW_top_5f_inclusiveDecays
    "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                             : "1  1  1  1  1  1  1  1  1",
    "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                              : "1  1  1  1  1  1  1  1  1",
    "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                              : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ST_tW_antitop_5f_inclusiveDecays
    "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"               : "1  1  1  1  1  1  1  1  1",
    "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                         : "1  1  1  1  1  1  1  1  1",
    "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                          : "1  1  1  1  1  1  1  1  1",
    "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                          : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToQQ_HT-200to400
    "/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToQQ_HT-400to600
    "/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToQQ_HT-600to800
    "/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToQQ_HT-800toInf
    "/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZJetsToQQ_HT-200to400
    "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZJetsToQQ_HT-400to600
    "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZJetsToQQ_HT-600to800
    "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZJetsToQQ_HT-800toInf
    "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WWTo4Q_4f
    "/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                          : "0  0  1  1  1  1  1  1  1",
    "/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                           : "0  0  1  1  1  1  1  1  1",
    "/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                           : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WWTo1L1Nu2Q_4f
    "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                     : "0  1  1  1  1  1  1  1  1",
    "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                      : "0  1  1  1  1  1  1  1  1",
    "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                      : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZTo2Q2L_mllmin4p0
    "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                       : "0  1  1  1  1  1  1  1  1",
    "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "0  1  1  1  1  1  1  1  1",
    "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "0  1  1  1  1  1  1  1  1",
    "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZTo1L1Nu2Q_4f
    "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                     : "0  1  1  1  1  1  1  1  1",
    "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                      : "0  1  1  1  1  1  1  1  1",
    "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                      : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZTo2Nu2Q_5f
    "/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                             : "0  0  1  1  1  1  1  1  1",
    "/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                        : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZTo4Q_5f
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                          : "0  0  1  1  1  1  1  1  1",
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                           : "0  0  1  1  1  1  1  1  1",
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                           : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZTo2Q2L_mllmin4p0
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                       : "0  1  1  1  1  1  1  1  1",
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "0  1  1  1  1  1  1  1  1",
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "0  1  1  1  1  1  1  1  1",
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WWW_4F
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                                            : "1  1  1  1  1  1  1  1  1",
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WWZ_4F
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                                            : "1  1  1  1  1  1  1  1  1",
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZZ
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"                                     : "1  1  1  1  1  1  1  1  1",
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZZ
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"                                     : "1  1  1  1  1  1  1  1  1",
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # VHToNonbb
    "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                             : "1  1  1  1  1  1  1  1  1",
    "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                              : "1  1  1  1  1  1  1  1  1",
    "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                              : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WminusH_HToBB_WToLNu
    "/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "0  1  1  1  1  1  1  1  1",
    "/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",
    "/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "0  1  1  1  1  1  1  1  1",
    "/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WplusH_HToBB_WToLNu
    "/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                      : "0  1  1  1  1  1  1  1  1",
    "/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                : "0  1  1  1  1  1  1  1  1",
    "/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                 : "0  1  1  1  1  1  1  1  1",
    "/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                 : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZH_HToBB_ZToQQ
    "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                           : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                      : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKWplus2Jets_WToQQ_dipoleRecoilOn
    "/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"           : "0  0  1  1  1  1  1  1  1",
    "/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                      : "0  0  1  1  1  1  1  1  1",
    "/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                      : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKWminus2Jets_WToQQ_dipoleRecoilOn
    "/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"          : "0  0  1  1  1  1  1  1  1",
    "/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                    : "0  0  1  1  1  1  1  1  1",
    "/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",
    "/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                     : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKZ2Jets_ZToLL
    "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"        : "1  1  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                  : "1  1  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                   : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKZ2Jets_ZToNuNu
    "/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"      : "0  0  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                : "0  0  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                 : "0  0  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                 : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKZ2Jets_ZToQQ_dipoleRecoilOn
    "/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"               : "0  0  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                         : "0  0  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                          : "0  0  1  1  1  1  1  1  1",
    "/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                          : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZJJ_EWK_InclusivePolarization
    "/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"       : "1  1  1  1  1  1  1  1  1",
    "/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                 : "1  1  1  1  1  1  1  1  1",
    "/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                  : "1  1  1  1  1  1  1  1  1",
    "/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                  : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTTo2L2Nu
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"                                                 : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ST_s-channel_4f_leptonDecays
    "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                 : "1  1  1  1  1  1  1  1  1",
    "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                           : "1  1  1  1  1  1  1  1  1",
    "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                            : "1  1  1  1  1  1  1  1  1",
    "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                            : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-70To100
    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"                : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                          : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                           : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-100To200
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"               : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                          : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                          : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-200To400
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"               : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"                          : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"                          : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-400To600
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                    : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-600To800
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                    : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-800To1200
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                   : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                             : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                              : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-1200To2500
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                  : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                             : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                             : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu_HT-2500ToInf
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext2-v1/NANOAODSIM"              : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext2-v1/NANOAODSIM"                        : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext2-v1/NANOAODSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext2-v1/NANOAODSIM"                         : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WJetsToLNu
    "/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                         : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                          : "0  1  1  1  1  1  1  1  1",
    "/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                          : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # DYJetsToLL
    "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                       : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v5/NANOAODSIM"                           : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                     : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKWMinus2Jets_WToLNu
    "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"  : "0  1  1  1  1  1  1  1  1",
    "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"            : "0  1  1  1  1  1  1  1  1",
    "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"             : "0  1  1  1  1  1  1  1  1",
    "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"             : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # EWKWPlus2Jets_WToLNu
    "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"   : "0  1  1  1  1  1  1  1  1",
    "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"             : "0  1  1  1  1  1  1  1  1",
    "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"              : "0  1  1  1  1  1  1  1  1",
    "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"              : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTWJetsToLNu
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "1  1  1  1  1  1  1  1  1",
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "1  1  1  1  1  1  1  1  1",
    "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TTZToLLNuNu
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                             : "1  1  1  1  1  1  1  1  1",
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                       : "1  1  1  1  1  1  1  1  1",
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                        : "1  1  1  1  1  1  1  1  1",
    "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                        : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ttWJets
    "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                              : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ttZJets
    "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                              : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # VBFWH_HToBB_WToLNu
    "/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"      : "0  1  1  1  1  1  1  1  1",
    "/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                : "0  1  1  1  1  1  1  1  1",
    "/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                 : "0  1  1  1  1  1  1  1  1",
    "/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                 : "0  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WWJJToLNuLNu_EWK_noTop
    "/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                       : "1  1  1  1  1  1  1  1  1",
    "/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WWTo2L2Nu
    "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                 : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZTo1L3Nu_4f
    "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                             : "1  1  1  1  1  1  1  1  1",
    "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                       : "1  1  1  1  1  1  1  1  1",
    "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                        : "1  1  1  1  1  1  1  1  1",
    "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                        : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZTo3LNu
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                 : "1  1  1  1  1  0  0  0  0",
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                           : "1  1  1  1  1  0  0  0  0",
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                            : "1  1  1  1  1  0  0  0  0",
    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                            : "1  1  1  1  1  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WminusH_HToBB_WToQQ
    "/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                      : "0  0  1  1  1  1  1  1  1",
    "/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                : "0  0  1  1  1  1  1  1  1",
    "/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                 : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WplusH_HToBB_WToQQ
    "/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                       : "0  0  1  1  1  1  1  1  1",
    "/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "0  0  1  1  1  1  1  1  1",
    "/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZH_HToBB_ZToLL
    "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                           : "1  1  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                     : "1  1  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZH_HToBB_ZToBB
    "/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                           : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                      : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZH_HToBB_ZToNuNu
    "/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                         : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                    : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZJJTo4L_EWKnotop
    "/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                            : "1  1  1  1  0  0  0  0  0",
    "/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                      : "1  1  1  1  0  0  0  0  0",
    "/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                       : "1  1  1  1  0  0  0  0  0",
    "/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                       : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZTo2L2Nu
    "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                 : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZTo4L
    "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                : "1  1  1  1  0  0  0  0  0",
    "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                          : "1  1  1  1  0  0  0  0  0",
    "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                           : "1  1  1  1  0  0  0  0  0",
    "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                           : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ggZH_HToBB_ZToLL
    "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                         : "1  1  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                   : "1  1  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                    : "1  1  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                    : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ggZH_HToBB_ZToBB
    "/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                         : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                    : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ggZH_HToBB_ZToNuNu
    "/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                       : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ggZH_HToBB_ZToQQ
    "/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                         : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                    : "0  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WZ
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                              : "1  1  1  1  1  1  1  1  1",
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                               : "1  1  1  1  1  1  1  1  1",
    "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                               : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # WW
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                              : "1  1  1  1  1  1  1  1  1",
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                               : "1  1  1  1  1  1  1  1  1",
    "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                               : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZ
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                              : "1  1  1  1  1  1  1  1  1",
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                               : "1  1  1  1  1  1  1  1  1",
    "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                               : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluHToZZTo4L
    "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"              : "1  1  1  1  0  0  0  0  0",
    "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                        : "1  1  1  1  0  0  0  0  0",
    "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                         : "1  1  1  1  0  0  0  0  0",
    "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                         : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # SSWW
    "/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                         : "1  1  1  1  1  1  1  1  1",
    "/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                                   : "1  1  1  1  1  1  1  1  1",
    "/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                                    : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # TWZToLL_tlept_Wlept_5f_DR
    "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                    : "1  1  1  1  0  0  0  0  0",
    "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "1  1  1  1  0  0  0  0  0",
    "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "1  1  1  1  0  0  0  0  0",
    "/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                               : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # tZq_ll_4f_ckm_NLO
    "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                            : "1  1  1  1  1  1  1  1  1",
    "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                       : "1  1  1  1  1  1  1  1  1",
    "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                       : "1  1  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluToContinToZZTo2e2mu
    "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                     : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                               : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluToContinToZZTo2e2tau
    "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                    : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                               : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluToContinToZZTo2mu2tau
    "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                   : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                             : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                              : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                              : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluToContinToZZTo4e
    "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                        : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                   : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                   : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluToContinToZZTo4mu
    "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                       : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluToContinToZZTo4tau
    "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"                      : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # HZJ_HToWWTo2L2Nu_ZTo2L
    "/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                   : "1  1  1  1  0  0  0  0  0",
    "/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                    : "1  1  1  1  0  0  0  0  0",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # GluGluZH_HToWWTo2L2Nu
    "/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                               : "0  1  1  1  1  1  1  1  1",
}


def is_mc_allowed(dsname, channel):
    """Check if MC dataset is allowed for channel. Unlisted samples run everywhere."""
    if dsname not in SAMPLE_MATRIX:
        return True
    flags = SAMPLE_MATRIX[dsname].split()
    return flags[CHANNELS.index(channel)] == "1"

