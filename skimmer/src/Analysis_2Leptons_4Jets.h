#ifndef ANALYSIS_2Leptons_4Jets_H
#define ANALYSIS_2Leptons_4Jets_H

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
typedef std::vector<double> Doubles;
typedef std::vector<int> Integers;
typedef std::vector<unsigned int> Indices;

class Analysis_2Leptons_4Jets : public Analysis
{
  public:
    // Constructor
    Analysis_2Leptons_4Jets(Arbusto &arbusto_ref, Nano &nt_ref, HEPCLI &cli_ref, Cutflow &cutflow_ref) : Analysis(arbusto_ref, nt_ref, cli_ref, cutflow_ref) {}

    // Initialize branches to be added to output "Events" TTree
    void initBranches() override
    {
        Analysis::initBranches();
    }

    // Define global variables and cutflow to be run in event loop
    void initCutflow() override
    {
        // Lepton selection
        Cut *cut_twoleptons = new LambdaCut("TwoLeptons", [&]() { return (cutflow.globals.getVal<LorentzVectors>("vvh_skim_lep_p4s").size() >= 2); });
        vCutflowCuts_.push_back(cut_twoleptons);

        Cut *cut_leadinglepton_pt = new LambdaCut("LeadingLeptonPT", [&]() { return (cutflow.globals.getVal<double>("vvh_lep_pt_lead") >= 20); });
        vCutflowCuts_.push_back(cut_leadinglepton_pt);

        // Resolved: >=4 AK4 jets (pt>15, no b-tag; b-tagging applied offline)
        Cut *cut_atleast4jets = new LambdaCut("AtLeast4Jets", [&]() { return (cutflow.globals.getVal<int>("n_vvh_veto_jets") >= 4); });
        vCutflowCuts_.push_back(cut_atleast4jets);

        finalSkimmerCut_ = "AtLeast4Jets";
        Analysis::initCutflow();
    }
};

#endif
