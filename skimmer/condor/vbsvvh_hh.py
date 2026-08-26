"""
Di-Higgs (HH) samples.

Kept in their own module rather than vbsvvh_mc.py because HH is a distinct
physics program from the VBS VVH backgrounds and the two should not be mixed
in the same list by accident.

The main set is RunIII2024Summer24 NanoAODv15 -- the SAME campaign and NanoAOD
version as v30's Run3 background (150X_mcRun3_2024_realistic_v2), so these fold
into Run3_Bkg_v15_v30_<channel> with no version-mismatch risk.

NOTE on naming: the Summer24 campaign uses the "Par-c2-...-kl-...-kt-..."
convention, unlike the older "kl-..._kt-..._c2-..." of the Summer22/23 v12/v13
samples. Gluon-fusion HH->4b is "GluGluHHto4B" (no "to" after GluGlu), while
every other ggHH final state is "GluGlutoHH...". Both spellings are correct on
DAS; do not "fix" them.
"""

from metis.Sample import DBSSample


_V15 = "RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2"


def _gghh(leaf):
    return DBSSample(dataset=f"/{leaf}_TuneCP5_13p6TeV_powheg-pythia8/{_V15}/NANOAODSIM")


# ------------------------------------------------------------------
# ggHH -> bb + VV / 4b, Summer24 NanoAODv15.
# kl scan (0.00, 1.00, 2.45, 5.00) at c2=0, kt=1 for every final state.
# ------------------------------------------------------------------
nanoaodv15_run3_bkg_hh = [
    # --- bbWW semi-leptonic (lvqq) ---
    _gghh("GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-0p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-1p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-2p45-kt-1p00"),
    _gghh("GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-5p00-kt-1p00"),
    # --- bbVV di-leptonic (2l2nu) ---
    _gghh("GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-0p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-1p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-2p45-kt-1p00"),
    _gghh("GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-5p00-kt-1p00"),
    # --- bbVV inclusive (covers the fully-hadronic mode; no dedicated
    #     2B2Wto4Q / 2B2Zto4Q sample exists in Summer24 v15) ---
    _gghh("GluGlutoHHto2B2V_Par-c2-0p00-kl-0p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2V_Par-c2-0p00-kl-1p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2V_Par-c2-0p00-kl-2p45-kt-1p00"),
    _gghh("GluGlutoHHto2B2V_Par-c2-0p00-kl-5p00-kt-1p00"),
    # --- bbZZ -> 2l2q ---
    _gghh("GluGlutoHHto2B2Zto2L2Q_Par-c2-0p00-kl-0p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2Zto2L2Q_Par-c2-0p00-kl-1p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2Zto2L2Q_Par-c2-0p00-kl-2p45-kt-1p00"),
    _gghh("GluGlutoHHto2B2Zto2L2Q_Par-c2-0p00-kl-5p00-kt-1p00"),
    # --- bbZZ -> 4l  (the kl=2.45 point carries an extra -LHEweights tag) ---
    _gghh("GluGlutoHHto2B2Zto4L_Par-c2-0p00-kl-0p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2Zto4L_Par-c2-0p00-kl-1p00-kt-1p00"),
    _gghh("GluGlutoHHto2B2Zto4L_Par-c2-0p00-kl-2p45-kt-1p00-LHEweights"),
    _gghh("GluGlutoHHto2B2Zto4L_Par-c2-0p00-kl-5p00-kt-1p00"),

    # --- ggHH -> 4b. Separate processing tag (PowhegBugFix); kl=0 is -v1,
    #     the rest -v2. A TrimmedSyst copy of kl=2.45 also exists on DAS and is
    #     deliberately NOT taken -- one processing per point. ---
    DBSSample(dataset="/GluGluHHto4B_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluHHto4B_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluHHto4B_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluHHto4B_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),

    # --- VHH -> 4b, SM point (C2V=1, C3=1, CV=1). Eight further C2V/C3/CV
    #     points exist per process in the same campaign if the scan is wanted. ---
    DBSSample(dataset=f"/WHH-HHto4B_Par-C2V-1p0-C3-1p0-CV-1p0_TuneCP5_13p6TeV_madgraph-pythia8/{_V15}/NANOAODSIM"),
    DBSSample(dataset=f"/ZHH-HHto4B_Par-C2V-1p0-C3-1p0-CV-1p0_TuneCP5_13p6TeV_madgraph-pythia8/{_V15}/NANOAODSIM"),
]


# ------------------------------------------------------------------
# ggHH -> bb tautau. NOT available in Summer24 NanoAODv15 -- only VBFHHto2B2Tau
# is. This is the Summer22 NanoAODv13 "ggHH_powheg_bugfix" processing, which was
# validated end-to-end against the local skim binary (branch types, year parsing
# and JetId JSON all resolve correctly for v13).
#
# TWO CAVEATS, both structural:
#   1. Different campaign/year (Summer22, 2022) from everything above (Summer24,
#      2024) -- NOT directly stackable with the rest of this set.
#   2. Only kl=0.00 and kl=5.00 exist with the bugfix; there is NO SM (kl=1)
#      point in this campaign.
# ------------------------------------------------------------------
_V13_S22 = "Run3Summer22NanoAODv13-ggHH_powheg_bugfix_133X_mcRun3_2022_realistic_ForNanov13_v1-v2"

nanoaodv13_run3_bkg_hh_bbtautau = [
    DBSSample(dataset=f"/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/{_V13_S22}/NANOAODSIM"),
    DBSSample(dataset=f"/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/{_V13_S22}/NANOAODSIM"),
]
