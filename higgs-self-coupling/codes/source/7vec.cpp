#include <stdio.h>
#include <stdlib.h>
#include <stack> 

#include "TROOT.h"
#include "TSystem.h"
#include "TApplication.h"
#include "TGClient.h"
#include "TString.h"
#include "TClonesArray.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TH1I.h"
#include "TH1D.h"
#include "TH2F.h"
#include "TH2I.h"
#include "TH2D.h"
#include "THStack.h"
#include "TLorentzVector.h"

final <int>[7] stack;
using namespace std;

int main(int argc,char* argv[]){
    gSystem->Load("libDelphes");
	TChain chain("Delphes");

    double beta = 2.0; 

    if(argc < 3){
		if(argc < 2) cout<<"INFO : The format is ./dtset input_file output_file"<<endl;
		cout << "INFO : Exiting" << endl;
        return 0;
	}

    /* Input the ROOT file that comes from Delphes for analysis */
    char *fileName = argv[1];
    chain.Add(fileName);
    cout <<"INFO : File is being processed for event level data" << endl;

    /* The name of the output CSV */
    char *outputFile = argv[2];
    std::ofstream myfile;
    myfile.open(outputFile);

    // Create class ExRootTreeReader Object
    ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
	Long64_t allEntries = treeReader->GetEntries();

    // Get pointers to branches used in this analysis
    TClonesArray *branchPhoton = treeReader->UseBranch("Photon");
    TClonesArray *branchJet = treeReader->UseBranch ("Jet");
    TClonesArray *branchMuon = treeReader->UseBranch("Muon");
    TClonesArray *branchElectron = treeReader->UseBranch("Electron");
    TClonesArray *branchMET = treeReader->UseBranch("MissingET");
    TClonesArray *branchTower = treeReader->UseBranch("Tower");

    return 0;
}