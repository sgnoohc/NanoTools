#ifndef ANALYSIS_4LEPTONSLOOSENOLH_H
#define ANALYSIS_4LEPTONSLOOSENOLH_H

// RAPIDO
#include "arbusto.h"
#include "cutflow.h"
#include "hepcli.h"
// ROOT
#include "TString.h"
// NanoCORE
#include "Config.h" // gconf
#include "Nano.h"
#include "Tools/goodrun.h"

#include "Analysis.h"
#include "ObjectSelection_Jets.h"
#include "ObjectSelection_Leptons.h"

typedef std::vector<LorentzVector> LorentzVectors;

// 4LepLooseNoLH -- 4LepLoose without the electron lostHits cut.
//
// Counts VVH::IDloose4LnoLH leptons:
//    e : pT > 5,  |eta_SC| < 2.5,  cutBased >= 1 (Veto)
//    mu: pT > 3,  |eta|    < 2.4,  (isGlobal || isTracker),  isPFcand
// i.e. IDloose4L minus "lostHits <= 1". Electrons keep whatever missing hits the
// Veto ID allows (<= 2 barrel, <= 3 endcap), so an analysis whose counted
// electrons are plain Veto ID is a subset of this skim. Muons are unchanged.
//
// Every event 4LepLoose keeps is also kept here (IDloose4L is built on top of
// IDloose4LnoLH in ElectronSelections.cc).
//
// OPT-IN channel (submit.py EXTRA_CHANNELS), like 4LepLoose.
class Analysis_4LeptonsLooseNoLH : public Analysis
{
  public:
    Analysis_4LeptonsLooseNoLH(Arbusto &arbusto_ref, Nano &nt_ref, HEPCLI &cli_ref, Cutflow &cutflow_ref)
        : Analysis(arbusto_ref, nt_ref, cli_ref, cutflow_ref) {}

    void initBranches() override { Analysis::initBranches(); }

    void initCutflow() override
    {
        Cut *cut_fourleptons_loose_nolh = new LambdaCut(
            "FourLeptonsLooseNoLH",
            [&]() { return (cutflow.globals.getVal<LorentzVectors>("vvh_loose4lnolh_lep_p4s").size() >= 4); });
        vCutflowCuts_.push_back(cut_fourleptons_loose_nolh);

        finalSkimmerCut_ = "FourLeptonsLooseNoLH";
        Analysis::initCutflow();
    }
};

#endif
