#ifndef __L1Analysis_L1AnalysisGMTTkMuonDataFormat_H__
#define __L1Analysis_L1AnalysisGMTTkMuonDataFormat_H__

//-------------------------------------------------------------------------------
// Created 20/04/2010 - E. Conte, A.C. Le Bihan
//
//
// Original code : UserCode/L1TriggerDPG/L1ExtraTreeProducer - Jim Brooke
//-------------------------------------------------------------------------------

#include <vector>

namespace L1Analysis {
  struct L1AnalysisGMTTkMuonDataFormat {
    L1AnalysisGMTTkMuonDataFormat() { Reset(); };
    ~L1AnalysisGMTTkMuonDataFormat(){};

    void Reset() {

      nGmtTkMuons = 0;
      gmtTkMuonPt.clear();
      gmtTkMuonEta.clear();
      gmtTkMuonPhi.clear();
      gmtTkMuonZ0.clear();
      gmtTkMuonD0.clear();


      gmtTkMuonIPt.clear();
      gmtTkMuonIEta.clear();
      gmtTkMuonIPhi.clear();
      gmtTkMuonIZ0.clear();
      gmtTkMuonID0.clear();
      gmtTkMuonChg.clear();
      gmtTkMuonIso.clear();
      gmtTkMuonQual.clear();
      gmtTkMuonBeta.clear();
      gmtTkMuonNStubs.clear();

      gmtTkMuonStubsEtaRegion.clear();
      gmtTkMuonStubsPhiRegion.clear();
      gmtTkMuonStubsDepthRegion.clear();
      gmtTkMuonStubsTfLayer.clear();
      gmtTkMuonStubsQuality.clear();
      gmtTkMuonStubsCoord1.clear();
      gmtTkMuonStubsCoord2.clear();
      gmtTkMuonStubsId.clear();
      gmtTkMuonStubsBxNum.clear();
      gmtTkMuonStubsEta1.clear();
      gmtTkMuonStubsEta2.clear();
      gmtTkMuonStubsEtaQuality.clear();
      gmtTkMuonStubsType.clear();
      gmtTkMuonStubsIsBarrel.clear();
      gmtTkMuonStubsIsEndcap.clear();
      gmtTkMuonStubsCoord1Offline.clear();
      gmtTkMuonStubsCoord2Offline.clear();
      gmtTkMuonStubsEta1Offline.clear();
      gmtTkMuonStubsEta2Offline.clear();

      gmtTkMuonIdLUTEta.clear();
      gmtTkMuonIdLUTPt.clear();
      gmtTkMuonIdLUTQuality.clear();


      gmtTkMuonSumPFIsoAll.clear();
      gmtTkMuonSumPFIsoCharged.clear();
      gmtTkMuonSumPFIsoEle.clear();
      gmtTkMuonSumPFIsoNeutral.clear();
      gmtTkMuonSumPFIsoPhoton.clear();
      gmtTkMuonSumPFIsoMuon.clear();
      gmtTkMuonSumPFIsoAllNoMu.clear();

      gmtTkMuonBx.clear();


      nPFCands = 0;
      pfCandId.clear();
      pfCandPt.clear();
      pfCandEta.clear();
      pfCandPhi.clear();
      pfCandzVtx.clear();
      pfCandChg.clear();





    }

    unsigned int nGmtTkMuons;
    std::vector<double> gmtTkMuonPt;
    std::vector<double> gmtTkMuonEta;
    std::vector<double> gmtTkMuonPhi;
    std::vector<double> gmtTkMuonZ0;
    std::vector<double> gmtTkMuonD0;
    std::vector<double> gmtTkMuonIPt;
    std::vector<double> gmtTkMuonIEta;
    std::vector<double> gmtTkMuonIPhi;
    std::vector<double> gmtTkMuonIZ0;
    std::vector<double> gmtTkMuonID0;
    std::vector<double> gmtTkMuonChg;
    std::vector<double> gmtTkMuonIso;
    std::vector<double> gmtTkMuonQual;
    std::vector<double> gmtTkMuonBeta;
    std::vector<unsigned int> gmtTkMuonNStubs;
    
    std::vector< std::vector<int> > gmtTkMuonStubsEtaRegion;
    std::vector< std::vector<int> > gmtTkMuonStubsPhiRegion;
    std::vector< std::vector<int> > gmtTkMuonStubsDepthRegion;
    std::vector< std::vector<int> > gmtTkMuonStubsTfLayer;
    std::vector< std::vector<int> > gmtTkMuonStubsQuality;
    std::vector< std::vector<int> > gmtTkMuonStubsCoord1;
    std::vector< std::vector<int> > gmtTkMuonStubsCoord2;
    std::vector< std::vector<int> > gmtTkMuonStubsId;
    std::vector< std::vector<int> > gmtTkMuonStubsBxNum;
    std::vector< std::vector<int> > gmtTkMuonStubsEta1;
    std::vector< std::vector<int> > gmtTkMuonStubsEta2;
    std::vector< std::vector<int> > gmtTkMuonStubsEtaQuality;
    std::vector< std::vector<int> > gmtTkMuonStubsType;
    std::vector< std::vector<bool> > gmtTkMuonStubsIsBarrel;
    std::vector< std::vector<bool> > gmtTkMuonStubsIsEndcap;
    std::vector< std::vector<double> > gmtTkMuonStubsCoord1Offline;
    std::vector< std::vector<double> > gmtTkMuonStubsCoord2Offline;
    std::vector< std::vector<double> > gmtTkMuonStubsEta1Offline;
    std::vector< std::vector<double> > gmtTkMuonStubsEta2Offline;

    std::vector<unsigned int>  gmtTkMuonIdLUTEta;
    std::vector<unsigned int>  gmtTkMuonIdLUTPt;
    std::vector<unsigned int>  gmtTkMuonIdLUTQuality;


    std::vector<short int> gmtTkMuonBx;

    std::vector<double> gmtTkMuonSumPFIsoAll;
    std::vector<double> gmtTkMuonSumPFIsoCharged;
    std::vector<double> gmtTkMuonSumPFIsoEle;
    std::vector<double> gmtTkMuonSumPFIsoNeutral;
    std::vector<double> gmtTkMuonSumPFIsoPhoton;
    std::vector<double> gmtTkMuonSumPFIsoMuon;
    std::vector<double> gmtTkMuonSumPFIsoAllNoMu;

    unsigned int nPFCands;
    std::vector<int> pfCandId;
    std::vector<double> pfCandPt;
    std::vector<double> pfCandEta;
    std::vector<double> pfCandPhi;
    std::vector<double> pfCandzVtx;
    std::vector<int> pfCandChg;


  };
}  // namespace L1Analysis
#endif

