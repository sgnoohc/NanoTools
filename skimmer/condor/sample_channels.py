# Sample-channel matrix: 1 = run, 0 = skip
# Edit the flags to toggle which channels each MC sample runs on.
# Unlisted samples default to running on all channels.

CHANNELS = ["4Lep", "3Lep", "2Lep2FJ", "2Lep1FJ", "1Lep1FJ",
            "0Lep3FJ", "0Lep2FJ", "0Lep1FJ", "0Lep0FJ",
            "2Lep4J"]  # appended after the 9-bit matrix; rows lacking this column default to allowed

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
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                                : "1  0  1  1  1  1  1  1  1",
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                          : "1  0  1  1  1  1  1  1  1",
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                           : "1  0  1  1  1  1  1  1  1",
    "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                           : "1  0  1  1  1  1  1  1  1",

    #                                                                                                                                                               4L 3L 22 21 11 03 02 01 00
    # ZZTo2Q2L_mllmin4p0
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"                       : "1  1  1  1  1  1  1  1  1",
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"                                  : "1  1  1  1  1  1  1  1  1",

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

    # ================================================================================================
    # LPC PFNano NanoAODv14 (nanoindex_v14_HVV_private.json), 4 eras.
    # Same convention as the Run2 rows above: hadronic processes drop 4Lep/3Lep;
    # fully-leptonic ZZ->4L / WZ->3L drop the 0Lep (and for 4L, 1Lep) channels.
    # Generated -- see the classifier in the v14 matrix commit.
    # ================================================================================================
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                            : "1  1  1  1  1  1  1  1  1",
    "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/DYto2E_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                          : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                 : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                 : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                 : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                 : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                 : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                   : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                     : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                 : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                    : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                    : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                          : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                        : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                          : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                          : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                        : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                          : "1  1  1  1  1  1  1  1  1",
    "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                               : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                             : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                               : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                             : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                               : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                             : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # DYto2Tau_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/DYto2Tau_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                            : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                          : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                            : "1  1  1  1  1  1  1  1  1",
    "/DYto2Tau_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                        : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGluHto2Zto4L_M-125_TuneCP5_13p6TeV_powhegMiNNLO-jhugen-pythia8  [ZZ->4L, fully leptonic]
    "/GluGluHto2Zto4L_M-125_TuneCP5_13p6TeV_powhegMiNNLO-jhugen-pythia8/2022_PFNanoV14/PFNANOSIM"                             : "1  1  1  1  0  0  0  0  0",
    "/GluGluHto2Zto4L_M-125_TuneCP5_13p6TeV_powhegMiNNLO-jhugen-pythia8/2022EE_PFNanoV14/PFNANOSIM"                           : "1  1  1  1  0  0  0  0  0",
    "/GluGluHto2Zto4L_M-125_TuneCP5_13p6TeV_powhegMiNNLO-jhugen-pythia8/2023_PFNanoV14/PFNANOSIM"                             : "1  1  1  1  0  0  0  0  0",
    "/GluGluHto2Zto4L_M-125_TuneCP5_13p6TeV_powhegMiNNLO-jhugen-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                         : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8  [ZZ->4L, fully leptonic]
    "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                   : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/2023_PFNanoV14/PFNANOSIM"                                     : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8  [ZZ->4L, fully leptonic]
    "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2022_PFNanoV14/PFNANOSIM"                                    : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                  : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2023_PFNanoV14/PFNANOSIM"                                    : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8  [ZZ->4L, fully leptonic]
    "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "1  1  1  1  0  0  0  0  0",
    "/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGlutoContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8  [ZZ->4L, fully leptonic]
    "/GluGlutoContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/2022_PFNanoV14/PFNANOSIM"                                     : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8  [ZZ->4L, fully leptonic]
    "/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8  [ZZ->4L, fully leptonic]
    "/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/2022_PFNanoV14/PFNANOSIM"                                          : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                        : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/2023_PFNanoV14/PFNANOSIM"                                          : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8  [ZZ->4L, fully leptonic]
    "/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/2022_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                       : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/2023_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  0  0  0  0  0",
    "/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                     : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                         : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                         : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                  : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8  [QCD multijet]
    "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                  : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8  [all-hadronic]
    "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                             : "0  0  1  1  1  1  1  1  1",
    "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                           : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8  [single lepton]
    "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                          : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8  [single lepton]
    "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                             : "0  1  1  1  1  1  1  1  1",
    "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                             : "0  1  1  1  1  1  1  1  1",
    "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                  : "1  1  1  1  1  1  1  1  1",
    "/TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                       : "0  0  1  1  1  1  1  1  1",
    "/TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                     : "0  0  1  1  1  1  1  1  1",
    "/TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                       : "0  0  1  1  1  1  1  1  1",
    "/TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                   : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                    : "0  1  1  1  1  1  1  1  1",
    "/TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                  : "0  1  1  1  1  1  1  1  1",
    "/TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                    : "0  1  1  1  1  1  1  1  1",
    "/TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                  : "1  1  1  1  1  1  1  1  1",
    "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                                  : "1  1  1  1  1  1  1  1  1",
    "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                : "1  1  1  1  1  1  1  1  1",
    "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                                  : "1  1  1  1  1  1  1  1  1",
    "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [2+ leptons plausible]
    "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                            : "1  1  1  1  1  1  1  1  1",
    "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  1  1  1  1  1",
    "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                          : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8  [2+ leptons plausible]
    "/TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/2022_PFNanoV14/PFNANOSIM"                                       : "1  1  1  1  1  1  1  1  1",
    "/TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                     : "1  1  1  1  1  1  1  1  1",
    "/TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/2023_PFNanoV14/PFNANOSIM"                                       : "1  1  1  1  1  1  1  1  1",
    "/TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                   : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8  [2+ leptons plausible]
    "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTWZ_TuneCP5_13p6TeV_madgraph-pythia8  [2+ leptons plausible]
    "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                                         : "1  1  1  1  1  1  1  1  1",
    "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                                         : "1  1  1  1  1  1  1  1  1",
    "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                     : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                      : "1  1  1  1  1  1  1  1  1",
    "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                      : "1  1  1  1  1  1  1  1  1",
    "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTto4Q_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                         : "0  0  1  1  1  1  1  1  1",
    "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                       : "0  0  1  1  1  1  1  1  1",
    "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                         : "0  0  1  1  1  1  1  1  1",
    "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                     : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                      : "0  1  1  1  1  1  1  1  1",
    "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                    : "0  1  1  1  1  1  1  1  1",
    "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                      : "0  1  1  1  1  1  1  1  1",
    "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                  : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                 : "1  1  1  1  1  1  1  1  1",
    "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                    : "0  0  1  1  1  1  1  1  1",
    "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                  : "0  0  1  1  1  1  1  1  1",
    "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                    : "0  0  1  1  1  1  1  1  1",
    "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                 : "0  1  1  1  1  1  1  1  1",
    "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                               : "0  1  1  1  1  1  1  1  1",
    "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                 : "0  1  1  1  1  1  1  1  1",
    "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                             : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                        : "1  1  1  1  1  1  1  1  1",
    "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                        : "1  1  1  1  1  1  1  1  1",
    "/TZQB-Zto2L-4FS_MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                    : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8  [all-hadronic]
    "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                             : "0  0  1  1  1  1  1  1  1",
    "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                           : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8  [single lepton]
    "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                          : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                               : "1  1  1  1  1  1  1  1  1",
    "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                             : "1  1  1  1  1  1  1  1  1",
    "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                               : "1  1  1  1  1  1  1  1  1",
    "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                           : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                  : "0  0  1  1  1  1  1  1  1",
    "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                : "0  0  1  1  1  1  1  1  1",
    "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                  : "0  0  1  1  1  1  1  1  1",
    "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                              : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                               : "0  1  1  1  1  1  1  1  1",
    "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                             : "0  1  1  1  1  1  1  1  1",
    "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                               : "0  1  1  1  1  1  1  1  1",
    "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # VBS-SSWW_PolarizationLL_TuneCP5_13p6TeV_madgraph-pythia8  [2+ leptons plausible]
    "/VBS-SSWW_PolarizationLL_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationLL_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                    : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationLL_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationLL_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # VBS-SSWW_PolarizationTL_TuneCP5_13p6TeV_madgraph-pythia8  [2+ leptons plausible]
    "/VBS-SSWW_PolarizationTL_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationTL_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                    : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationTL_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationTL_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # VBS-SSWW_PolarizationTT_TuneCP5_13p6TeV_madgraph-pythia8  [2+ leptons plausible]
    "/VBS-SSWW_PolarizationTT_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationTT_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                    : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationTT_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                      : "1  1  1  1  1  1  1  1  1",
    "/VBS-SSWW_PolarizationTT_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8  [2+ leptons plausible]
    "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                                : "1  1  1  1  1  1  1  1  1",
    "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                              : "1  1  1  1  1  1  1  1  1",
    "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                                : "1  1  1  1  1  1  1  1  1",
    "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                            : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8  [2+ leptons plausible]
    "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  1  1  1  1  1",
    "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/2023_PFNanoV14/PFNANOSIM"                                               : "1  1  1  1  1  1  1  1  1",
    "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                     : "1  1  1  1  1  1  1  1  1",
    "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                   : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WW_TuneCP5_13p6TeV_pythia8  [2+ leptons plausible]
    "/WW_TuneCP5_13p6TeV_pythia8/2022_PFNanoV14/PFNANOSIM"                                                                    : "1  1  1  1  1  1  1  1  1",
    "/WW_TuneCP5_13p6TeV_pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                                  : "1  1  1  1  1  1  1  1  1",
    "/WW_TuneCP5_13p6TeV_pythia8/2023_PFNanoV14/PFNANOSIM"                                                                    : "1  1  1  1  1  1  1  1  1",
    "/WW_TuneCP5_13p6TeV_pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                                : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWto2L2Nu-2Jets_OS_noTop_EW_TuneCP5_13p6TeV_madgraph-madspin-pythia8  [2+ leptons plausible]
    "/WWto2L2Nu-2Jets_OS_noTop_EW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2022_PFNanoV14/PFNANOSIM"                          : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu-2Jets_OS_noTop_EW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2022EE_PFNanoV14/PFNANOSIM"                        : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu-2Jets_OS_noTop_EW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                      : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWto2L2Nu-2Jets_SS_noTop_EW_TuneCP5_13p6TeV_madgraph-pythia8  [2+ leptons plausible]
    "/WWto2L2Nu-2Jets_SS_noTop_EW_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu-2Jets_SS_noTop_EW_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu-2Jets_SS_noTop_EW_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                  : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu-2Jets_SS_noTop_EW_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                              : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                      : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                    : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                      : "1  1  1  1  1  1  1  1  1",
    "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                  : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWto4Q_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                         : "0  0  1  1  1  1  1  1  1",
    "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                       : "0  0  1  1  1  1  1  1  1",
    "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                         : "0  0  1  1  1  1  1  1  1",
    "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                     : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                      : "0  1  1  1  1  1  1  1  1",
    "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                    : "0  1  1  1  1  1  1  1  1",
    "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                      : "0  1  1  1  1  1  1  1  1",
    "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                  : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                                          : "1  1  1  1  1  1  1  1  1",
    "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                        : "1  1  1  1  1  1  1  1  1",
    "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                                          : "1  1  1  1  1  1  1  1  1",
    "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                      : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WZ_TuneCP5_13p6TeV_pythia8  [2+ leptons plausible]
    "/WZ_TuneCP5_13p6TeV_pythia8/2022_PFNanoV14/PFNANOSIM"                                                                    : "1  1  1  1  1  1  1  1  1",
    "/WZ_TuneCP5_13p6TeV_pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                                  : "1  1  1  1  1  1  1  1  1",
    "/WZ_TuneCP5_13p6TeV_pythia8/2023_PFNanoV14/PFNANOSIM"                                                                    : "1  1  1  1  1  1  1  1  1",
    "/WZ_TuneCP5_13p6TeV_pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                                : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                     : "1  1  1  1  1  1  1  1  1",
    "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                   : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8  [WZ->3L, fully leptonic]
    "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  0  0  0  0",
    "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                     : "1  1  1  1  1  0  0  0  0",
    "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  0  0  0  0",
    "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                   : "1  1  1  1  1  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                       : "0  1  1  1  1  1  1  1  1",
    "/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                     : "0  1  1  1  1  1  1  1  1",
    "/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                       : "0  1  1  1  1  1  1  1  1",
    "/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                   : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                      : "0  1  1  1  1  1  1  1  1",
    "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                    : "0  1  1  1  1  1  1  1  1",
    "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                      : "0  1  1  1  1  1  1  1  1",
    "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                  : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                  : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                     : "0  1  1  1  1  1  1  1  1",
    "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                   : "0  1  1  1  1  1  1  1  1",
    "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                     : "0  1  1  1  1  1  1  1  1",
    "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                 : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",
    "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8  [single lepton]
    "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                      : "0  1  1  1  1  1  1  1  1",
    "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                    : "0  1  1  1  1  1  1  1  1",
    "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                      : "0  1  1  1  1  1  1  1  1",
    "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                  : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/Wto2Q-3Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                          : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                        : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                          : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                        : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                                : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                                : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  [W->lnu+jets]
    "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022_PFNanoV14/PFNANOSIM"                                : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2022EE_PFNanoV14/PFNANOSIM"                              : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023_PFNanoV14/PFNANOSIM"                                : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                            : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8  [W->lnu+jets]
    "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8  [W->lnu+jets]
    "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8  [W->lnu+jets]
    "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8  [W->lnu+jets]
    "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "0  1  1  1  1  1  1  1  1",
    "/WtoLNu-4Jets_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8  [Z->nunu invisible]
    "/ZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                  : "0  0  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                           : "0  0  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                         : "0  0  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                           : "0  0  1  1  1  1  1  1  1",
    "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8  [2+ leptons plausible]
    "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2022_PFNanoV14/PFNANOSIM"                                                          : "1  1  1  1  1  1  1  1  1",
    "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                        : "1  1  1  1  1  1  1  1  1",
    "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2023_PFNanoV14/PFNANOSIM"                                                          : "1  1  1  1  1  1  1  1  1",
    "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                      : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZZ_TuneCP5_13p6TeV_pythia8  [2+ leptons plausible]
    "/ZZ_TuneCP5_13p6TeV_pythia8/2022_PFNanoV14/PFNANOSIM"                                                                    : "1  1  1  1  1  1  1  1  1",
    "/ZZ_TuneCP5_13p6TeV_pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                                  : "1  1  1  1  1  1  1  1  1",
    "/ZZ_TuneCP5_13p6TeV_pythia8/2023_PFNanoV14/PFNANOSIM"                                                                    : "1  1  1  1  1  1  1  1  1",
    "/ZZ_TuneCP5_13p6TeV_pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                                : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                     : "1  1  1  1  1  1  1  1  1",
    "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  1  1  1  1  1",
    "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                   : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZZto4L-2Jets_EW_TuneCP5_13p6TeV_madgraph-pythia8  [ZZ->4L, fully leptonic]
    "/ZZto4L-2Jets_EW_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L-2Jets_EW_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                            : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L-2Jets_EW_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                              : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L-2Jets_EW_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                          : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZZto4L-2Jets_QCD_TuneCP5_13p6TeV_madgraph-pythia8  [ZZ->4L, fully leptonic]
    "/ZZto4L-2Jets_QCD_TuneCP5_13p6TeV_madgraph-pythia8/2022_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L-2Jets_QCD_TuneCP5_13p6TeV_madgraph-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                           : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L-2Jets_QCD_TuneCP5_13p6TeV_madgraph-pythia8/2023_PFNanoV14/PFNANOSIM"                                             : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L-2Jets_QCD_TuneCP5_13p6TeV_madgraph-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZZto4L_TuneCP5_13p6TeV_powheg-pythia8  [ZZ->4L, fully leptonic]
    "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                                         : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                                       : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                                         : "1  1  1  1  0  0  0  0  0",
    "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                                     : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                 : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                   : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                               : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8  [all-hadronic]
    "/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022_PFNanoV14/PFNANOSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023_PFNanoV14/PFNANOSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/Zto2Q-4Jets_HT-800_TuneCP5_13p6TeV_madgraphMLM-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8  [2+ leptons plausible]
    "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                       : "1  1  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                         : "1  1  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                     : "1  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8  [Z->nunu invisible]
    "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                      : "0  0  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                        : "0  0  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                    : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8  [all-hadronic]
    "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022_PFNanoV14/PFNANOSIM"                                         : "0  0  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2022EE_PFNanoV14/PFNANOSIM"                                       : "0  0  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023_PFNanoV14/PFNANOSIM"                                         : "0  0  1  1  1  1  1  1  1",
    "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/2023BPix_PFNanoV14/PFNANOSIM"                                     : "0  0  1  1  1  1  1  1  1",


    # ================================================================================================
    # V+jets HT-binned (M. Mazza request 2026-09-15).
    #   Z->nunu  -> hadronic: invisible final state, no prompt leptons.
    #   W->lnu   -> single lepton, matching the existing WJetsToLNu_HT-* rows.
    # ================================================================================================
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # ZJetsToNuNu_TuneCP5_13TeV-madgraphMLM-pythia8
    "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # Zto2Nu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/Zto2Nu-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/Zto2Nu-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/Zto2Nu-4Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/Zto2Nu-4Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/Zto2Nu-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    "/Zto2Nu-4Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  0  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-40to100-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-40to100-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-100to400-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-100to400-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-400to800-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-400to800-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-800to1500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-800to1500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-1500to2500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-1500to2500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-2500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    # WtoLNu-4Jets-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8
    "/WtoLNu-4Jets_Bin-HT-2500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM" : "0  1  1  1  1  1  1  1  1",


    # ============================================================================================
    # S. Ellis request (mc_sample_request.txt), 4L section.
    #  ZZJJTo4L (plain, NOT the EWKnotop variant already present) -- ZZ->4L
    #  fully leptonic, so the same flags as the other ZZ->4L rows.
    #  ALSO above: ZZTo4Q_5f and ZZTo2Q2L flipped to ALLOW 4Lep at the
    #  requester's explicit ask. ZZTo4Q is fully hadronic, so that is a
    #  deliberate divergence from the convention that hadronic samples drop
    #  4Lep; expect most of those jobs to select zero events.
    # ============================================================================================
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    "/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"  : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    "/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"            : "1  1  1  1  0  0  0  0  0",
    #                                                                                                                                                   4L 3L 22 21 11 03 02 01 00
    "/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"             : "1  1  1  1  0  0  0  0  0",

}


def is_mc_allowed(dsname, channel):
    """Check if MC dataset is allowed for channel. Unlisted samples run everywhere."""
    if dsname not in SAMPLE_MATRIX:
        return True
    flags = SAMPLE_MATRIX[dsname].split()
    idx = CHANNELS.index(channel)
    if idx >= len(flags):
        return True  # channel added after this sample's matrix row was written -> run everywhere
    return flags[idx] == "1"

