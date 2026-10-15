#ifndef ARBUSTO_H
#define ARBUSTO_H

#include "TChain.h"
#include "TBranch.h"
#include "TLeaf.h"
#include "TObjArray.h"
#include <cstring>
#include <vector>
#include <utility>

#include "arbol.h"
#include "hepcli.h"

/**
 * Wraps Arbol object with functionality for skimming
 */
class Arbusto : public Arbol
{
protected:
    /** Invert how the branches are kept */
    bool remove_branches;
    /** Names of branches in original ROOT TTree to keep */
    std::vector<TString> branch_names;
    /** Pointer to current TTree to skim */
    TTree* orig_ttree;
    /** Input branches to rename before cloning/copying addresses (old -> new) */
    std::vector<std::pair<TString, TString>> rename_branches;
    /**
     * Rename input branches per rename_branches, so a branch the skimmer intends
     * to recompute under the same name does not end up duplicated in the output.
     * Must run before CloneTree() and before CopyAddresses() on every new tree.
     * @param tree pointer to the input TTree
     * @return none
     */
    void applyRenames(TTree* tree);
public:
    /**
     * Arbusto object constructor
     * @return none
     */
    Arbusto();
    /**
     * Arbusto object overload constructor
     * @param new_tfile pointer to output TFile
     * @param tchain pointer to TChain of input TFiles
     * @param branch_names std::vector of branch names to keep
     * @param remove_branches bool selections so branches are dropped not kept
     * @return none
     */
    Arbusto(TFile* new_tfile, TChain* tchain, std::vector<TString> branch_names, bool remove_branches,
            std::vector<std::pair<TString, TString>> rename_branches = {});
    /**
     * Arbusto object overload constructor
     * @param cli HEPCLI object
     * @param branch_names std::vector of branch names to keep
     * @return none
     */
    Arbusto(HEPCLI& cli, std::vector<TString> branch_names);
    /**
     * Arbusto object destructor
     * @return none
     */
    virtual ~Arbusto();
    /**
     * Initialize Arbusto for current file
     * @param next_ttree pointer to the next of the original TTree objects
     * @return none
     */
    void init(TTree* next_ttree);
    /**
     * Fill TTree with all current leaves
     * @param entry current entry
     * @return none
     */
    void fill(int entry);
};

#include "arbusto.icc"

#endif
