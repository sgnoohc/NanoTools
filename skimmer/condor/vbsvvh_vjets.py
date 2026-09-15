"""
V+jets HT-binned samples (NanoAODv15), requested by M. Mazza 2026-09-15.

Source lists (UAF): /home/users/mmazza/public/vjets_samples/
    znunu_HT_nanoaodv15_run2_2024.txt
    wjets_HT_nanoaodv15_2024.txt
All 46 datasets re-verified against DAS 2026-09-15: event/file counts match.

CAVEATS carried over from the source lists -- read before combining anything:

 * HT bin edges DIFFER between Run 2 and 2024; the two sets are NOT
   bin-for-bin comparable.
       Run 2 Z->nunu : 100-200-400-600-800-1200-2500-Inf
       2024  Z->nunu : 100-200-400-800-1500-2500-Inf
       2024  W->lnu  : 40-100-400-800-1500-2500-Inf
 * NO HT<100 sample exists in any era -- this set is incomplete at low HT.
 * Do NOT combine the Z->nunu HT set with the amcatnloFXFX pT(Z)-binned
   Z->nunu samples: same process, different generator binning.
 * W->lnu 2024 is binned 2-D: 6 HT bins x 2 M(lnu) slices. BOTH slices of each
   HT bin are included below -- taking only MLNu-0to120 drops the high-mass
   tail, which is ~half the events in the three highest HT bins.
"""

from metis.Sample import DBSSample


# ------------------------------------------------------------------
# Z(->nunu)+jets, HT-binned, Run 2 UL (13 TeV, madgraphMLM LO).
# 7 HT bins x 4 eras = 28 datasets, 184.5M events.
# NEW COVERAGE: the repo had no Z->nunu+jets at all. This is an
# irreducible background for the 0Lep channels, not an alternative to
# anything already present -- no double-counting with existing groups.
# ------------------------------------------------------------------
nanoaodv15_run2_bkg_znunu_ht = [
    # --- 2016preVFP ---
    DBSSample(dataset="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    # --- 2016postVFP ---
    DBSSample(dataset="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    # --- 2017 ---
    DBSSample(dataset="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    # --- 2018 ---
    DBSSample(dataset="/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
]


# ------------------------------------------------------------------
# V+jets HT-binned, 2024 (13.6 TeV, madgraphMLM LO), Summer24 v15 --
# same campaign as v30's Run3 background.
#
# Z->nunu (6 ds): new coverage, as above.
#
# W->lnu (12 ds): *** OVERLAPS existing 2024 W+jets in run3_bkg ***
#   run3_bkg already carries, for this same campaign:
#     WtoLNu-2Jets_Bin-{1J,2J}-PTLNu-*   (10 ds, amcatnloFXFX, pT-binned)
#     WtoLNu-4Jets_Bin-{1,2,3,4}J        ( 4 ds, madgraphMLM, jet-binned)
#   Adding HT-binned makes THREE parallel descriptions of the same
#   process. Pick ONE scheme downstream -- do not sum them. Same hazard
#   as the v33 DY merge; see log.md 2026-06-27.
# ------------------------------------------------------------------
nanoaodv15_run3_bkg_vjets_ht = [
    # --- Z->nunu, 2024 (new coverage) ---
    DBSSample(dataset="/Zto2Nu-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/Zto2Nu-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/Zto2Nu-4Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Nu-4Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Nu-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Nu-4Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    # --- W->lnu, 2024 (OVERLAPS run3_bkg W+jets -- see header) ---
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-40to100-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-40to100-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-100to400-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-100to400-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-400to800-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-400to800-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-800to1500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-800to1500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-1500to2500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-1500to2500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-2500-MLNu-0to120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-HT-2500-MLNu-120_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
]
