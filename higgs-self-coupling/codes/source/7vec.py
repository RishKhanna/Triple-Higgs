#!/usr/bin/env python
import sys
import ROOT
import pandas as pd

ROOT.gSystem.Load("~/apps/Madgraphs/Delphes/libDelphes.so")
ROOT.gInterpreter.Declare('#include "~/apps/Madgraphs/Delphes/classes/DelphesClasses.h"')
ROOT.gInterpreter.Declare('#include "~/apps/Madgraphs/ExRootAnalysis/ExRootAnalysis/ExRootTreeReader.h"')


inputFile = sys.argv[1]
# inputFile = "../../../mpnnvec/hh_2/Events/run_01/tag_1_delphes_events.root"

# Create chain of root trees
chain = ROOT.TChain("Delphes")
chain.Add(inputFile)

# Create object of class ExRootTreeReader
treeReader = ROOT.ExRootTreeReader(chain)
numberOfEntries = treeReader.GetEntries()

# Get pointers to branches used in this analysis
branchPhoton = treeReader.UseBranch("Photon")
branchElectron = treeReader.UseBranch("Electron")
branchMuon = treeReader.UseBranch("Muon")
branchJet = treeReader.UseBranch("Jet")
branchMET = treeReader.UseBranch("MissingET")

Final = []

for entry in range(0,numberOfEntries):
    treeReader.ReadEntry(entry)
    
    # Photon
    if branchPhoton.GetEntries() > 0:
        ph = branchPhoton.At(0)
        Final.append([1,0,0,0,ph.PT,ph.E,0])
    
    # Leptons
    if (branchElectron.GetEntriesFast()>0) :
        e = [ branchElectron.At(i) for i in range(branchElectron.GetEntries()) ]
        for i in e:
            Final.append([0,i.Charge, 0,0,i.PT,i.P4().E(), i.P4().M()])
    if (branchMuon.GetEntriesFast()>0) :
        m = [ branchMuon.At(i) for i in range(branchMuon.GetEntries()) ]
        for i in m:
            Final.append([0,i.Charge, 0,0,i.PT,i.P4().E(), i.P4().M()])
    
    #Jets
    if (branchJet.GetEntriesFast()>0) :
        j = [ branchJet.At(i) for i in range(branchJet.GetEntries()) ]
        for i in j:
            Final.append([0,0,int(2*(i.BTag-0.5)),0,i.PT,i.P4().E(), i.P4().M()])
            
    #Missing ET
    if (branchMET.GetEntriesFast()>0):
        met = [ branchMET.At(i) for i in range(branchMET.GetEntries()) ]
        for i in met:
            Final.append([0,0,0,1,i.MET,i.P4().E(), i.P4().M()])


fin_df = pd.DataFrame(Final,columns=["I1", "I2", "I3", "I4", "PT", "E", "M"])
fin.to_csv("/share1/rishabh/")
