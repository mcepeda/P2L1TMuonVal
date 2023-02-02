//This code is for filling the step1 menu objects, for full tree go for L1AnalysisPhaseII.c
#include "L1Trigger/Phase2L1GMTNtuples/interface/L1AnalysisGMTTkMuon.h"
#include "L1Trigger/L1TMuon/interface/MicroGMTConfiguration.h"
#include "DataFormats/L1TMuonPhase2/interface/Constants.h"
#include "TMath.h"
L1Analysis::L1AnalysisGMTTkMuon::L1AnalysisGMTTkMuon() {}

L1Analysis::L1AnalysisGMTTkMuon::~L1AnalysisGMTTkMuon() {}

//tkmuon gmt
void L1Analysis::L1AnalysisGMTTkMuon::SetGmtTkMuon(const edm::Handle<std::vector<l1t::TrackerMuon> > gmtTkMuon, const edm::Handle<vector<l1t::PFCandidate>> l1pfCandidates, unsigned maxL1Extra) {

        const float lsb_pt = Phase2L1GMT::LSBpt;
        const float lsb_phi = Phase2L1GMT::LSBphi;
        const float lsb_eta = Phase2L1GMT::LSBeta;
        const float lsb_z0 = Phase2L1GMT::LSBGTz0;
        const float lsb_d0 = Phase2L1GMT::LSBGTd0;

        for (unsigned int i = 0; i < gmtTkMuon->size() && l1extra_.nGmtTkMuons < maxL1Extra; i++) {
                if (lsb_pt*gmtTkMuon->at(i).hwPt() > 0) {
                        l1extra_.gmtTkMuonPt.push_back(lsb_pt*gmtTkMuon->at(i).hwPt()); //use pT
                        l1extra_.gmtTkMuonEta.push_back(lsb_eta*gmtTkMuon->at(i).hwEta());
                        l1extra_.gmtTkMuonPhi.push_back(lsb_phi*gmtTkMuon->at(i).hwPhi());
                        l1extra_.gmtTkMuonZ0.push_back(lsb_z0*gmtTkMuon->at(i).hwZ0());
                        l1extra_.gmtTkMuonD0.push_back(lsb_d0*gmtTkMuon->at(i).hwD0());

                        l1extra_.gmtTkMuonIPt.push_back(gmtTkMuon->at(i).hwPt()); //rename?
                        l1extra_.gmtTkMuonIEta.push_back(gmtTkMuon->at(i).hwEta());
                        l1extra_.gmtTkMuonIPhi.push_back(gmtTkMuon->at(i).hwPhi());
                        l1extra_.gmtTkMuonIZ0.push_back(gmtTkMuon->at(i).hwZ0());
                        l1extra_.gmtTkMuonID0.push_back(gmtTkMuon->at(i).hwD0());

                        l1extra_.gmtTkMuonChg.push_back(gmtTkMuon->at(i).hwCharge());
                        l1extra_.gmtTkMuonIso.push_back(gmtTkMuon->at(i).hwIso());
                        l1extra_.gmtTkMuonQual.push_back(gmtTkMuon->at(i).hwQual());
                        l1extra_.gmtTkMuonBeta.push_back(gmtTkMuon->at(i).hwBeta());

                        l1extra_.gmtTkMuonNStubs.push_back(gmtTkMuon->at(i).stubs().size());

/*                      Tuning the low pt ID can only be done with a special branch by Michalis 
 *                      These are the changes needed: 
 *                      https://github.com/bachtis/cmssw/commit/8a43ca2c2a2467e09708b2086d440d0ed064af92
 *                      Ignore for now! 
 
                                l1extra_.gmtTkMuonIdLUTEta.push_back(gmtTkMuon->at(i).idLUTEta());
                                l1extra_.gmtTkMuonIdLUTPt.push_back(gmtTkMuon->at(i).idLUTPt());
                                l1extra_.gmtTkMuonIdLUTQuality.push_back(gmtTkMuon->at(i).idLUTQuality());
*/                                



                        // We do not need all of this for this check, but let's keep it for now

                        std::vector<int> RegionEta; 
                        std::vector<int> RegionPhi; 
                        std::vector<int> RegionDepth; 
                        std::vector<int> TfLayer; 
                        std::vector<int> Quality; 
                        std::vector<int> Coord1; 
                        std::vector<int> Coord2;
                        std::vector<int> Id;
                        std::vector<int> BxNumber;
                        std::vector<int> Eta1;
                        std::vector<int> Eta2;
                        std::vector<int> EtaQuality;
                        std::vector<int> Type;
                        std::vector<bool> IsBarrel;
                        std::vector<bool> IsEndcap;
                        std::vector<double> Coord1Offline;
                        std::vector<double> Coord2Offline;
                        std::vector<double> Eta1Offline;
                        std::vector<double> Eta2Offline;

                        for (unsigned int j=0; j<gmtTkMuon->at(i).stubs().size(); j++){
//                                std::cout<<"Here is a stub!"<<gmtTkMuon->at(i).stubs().at(j)->etaRegion()<<std::endl;
                                RegionEta.push_back(gmtTkMuon->at(i).stubs().at(j)->etaRegion());
                                RegionPhi.push_back(gmtTkMuon->at(i).stubs().at(j)->phiRegion());
                                RegionDepth.push_back(gmtTkMuon->at(i).stubs().at(j)->depthRegion());
                                TfLayer.push_back(gmtTkMuon->at(i).stubs().at(j)->tfLayer());
                                Quality.push_back(gmtTkMuon->at(i).stubs().at(j)->quality());
                                Coord1.push_back(gmtTkMuon->at(i).stubs().at(j)->coord1());
                                Coord2.push_back(gmtTkMuon->at(i).stubs().at(j)->coord2());
                                Id.push_back(gmtTkMuon->at(i).stubs().at(j)->id());
                                BxNumber.push_back(gmtTkMuon->at(i).stubs().at(j)->bxNum());
                                Eta1.push_back(gmtTkMuon->at(i).stubs().at(j)->eta1());
                                Eta2.push_back(gmtTkMuon->at(i).stubs().at(j)->eta2());
                                EtaQuality.push_back(gmtTkMuon->at(i).stubs().at(j)->etaQuality());
                                Type.push_back(gmtTkMuon->at(i).stubs().at(j)->type());
                                IsBarrel.push_back(gmtTkMuon->at(i).stubs().at(j)->isBarrel());
                                IsEndcap.push_back(gmtTkMuon->at(i).stubs().at(j)->isEndcap());
                                Coord1Offline.push_back(gmtTkMuon->at(i).stubs().at(j)->coord1());
                                Coord2Offline.push_back(gmtTkMuon->at(i).stubs().at(j)->coord2());
                                Eta1Offline.push_back(gmtTkMuon->at(i).stubs().at(j)->offline_eta1());
                                Eta2Offline.push_back(gmtTkMuon->at(i).stubs().at(j)->offline_eta2());
                        }

                        l1extra_.gmtTkMuonStubsEtaRegion.push_back(RegionEta);
                        l1extra_.gmtTkMuonStubsPhiRegion.push_back(RegionPhi);
                        l1extra_.gmtTkMuonStubsDepthRegion.push_back(RegionDepth);
                        l1extra_.gmtTkMuonStubsTfLayer.push_back(TfLayer);
                        l1extra_.gmtTkMuonStubsQuality.push_back(Quality);
                        l1extra_.gmtTkMuonStubsCoord1.push_back(Coord1);
                        l1extra_.gmtTkMuonStubsCoord2.push_back(Coord2);
                        l1extra_.gmtTkMuonStubsId.push_back(Id);
                        l1extra_.gmtTkMuonStubsBxNum.push_back(BxNumber);
                        l1extra_.gmtTkMuonStubsEta1.push_back(Eta1);
                        l1extra_.gmtTkMuonStubsEta2.push_back(Eta2);
                        l1extra_.gmtTkMuonStubsEtaQuality.push_back(EtaQuality);
                        l1extra_.gmtTkMuonStubsType.push_back(Type);
                        l1extra_.gmtTkMuonStubsIsBarrel.push_back(IsBarrel);
                        l1extra_.gmtTkMuonStubsIsEndcap.push_back(IsEndcap);
                        l1extra_.gmtTkMuonStubsCoord1Offline.push_back(Coord1Offline);
                        l1extra_.gmtTkMuonStubsCoord2Offline.push_back(Coord2Offline);
                        l1extra_.gmtTkMuonStubsEta1Offline.push_back(Eta1Offline);
                        l1extra_.gmtTkMuonStubsEta2Offline.push_back(Eta2Offline);


                        l1extra_.gmtTkMuonBx.push_back(0); //is this just 0 always?

                        l1extra_.nGmtTkMuons++;
                }


                double sumIsoCharged=0;
                double sumIsoEle=0;
                double sumIsoNeutral=0;
                double sumIsoPhoton=0;
                double sumIsoMuon=0;
                double sumIsoAll=0;
                double sumIsoAllNoMu=0;


                for (unsigned int part = 0; part < l1pfCandidates->size(); part++) {

                        double deltaEta=fabs(lsb_eta*gmtTkMuon->at(i).hwEta()-l1pfCandidates->at(part).eta()); // I'm assuming the eta is converted correctly to not deal with the hwEta..
                        double deltaPhi=fabs(lsb_phi*gmtTkMuon->at(i).hwPhi()-l1pfCandidates->at(part).phi()); // I'm assuming the Phi is converted correctly to not deal with the hwPhi..
                        if (deltaPhi>=M_PI) deltaPhi=2*M_PI-deltaPhi;
                        double deltaR=sqrt(deltaEta*deltaEta+deltaPhi*deltaPhi);

                        if (deltaR> 0.4) continue ; // Like in normal PF?

                        sumIsoAll+=l1pfCandidates->at(part).pt(); // careful does this have the muon? Also, I'm also assuming I can use simply pt for now
                        if(l1pfCandidates->at(part).id()==0) sumIsoCharged+=l1pfCandidates->at(part).pt();
                        else if (l1pfCandidates->at(part).id()==1) sumIsoEle+=l1pfCandidates->at(part).pt();
                        else if (l1pfCandidates->at(part).id()==2) sumIsoNeutral+=l1pfCandidates->at(part).pt();
                        else if (l1pfCandidates->at(part).id()==3) sumIsoPhoton+=l1pfCandidates->at(part).pt();
                        else if (l1pfCandidates->at(part).id()==4) sumIsoMuon+=l1pfCandidates->at(part).pt();

                        if (l1pfCandidates->at(part).id()!=4) sumIsoAllNoMu+=l1pfCandidates->at(part).pt();

                }

                l1extra_.gmtTkMuonSumPFIsoAll.push_back(sumIsoAll);
                l1extra_.gmtTkMuonSumPFIsoCharged.push_back(sumIsoCharged);
                l1extra_.gmtTkMuonSumPFIsoEle.push_back(sumIsoEle);
                l1extra_.gmtTkMuonSumPFIsoNeutral.push_back(sumIsoNeutral);
                l1extra_.gmtTkMuonSumPFIsoPhoton.push_back(sumIsoPhoton);
                l1extra_.gmtTkMuonSumPFIsoMuon.push_back(sumIsoMuon);
                l1extra_.gmtTkMuonSumPFIsoAllNoMu.push_back(sumIsoAllNoMu);


        }


//      If you want to save all the pfcandidates for further studies (this could be removed) 

        for (unsigned int i = 0; i < l1pfCandidates->size(); i++) {
                //         enum Kind { ChargedHadron=0, Electron=1, NeutralHadron=2, Photon=3, Muon=4 };
                //if (abs(l1pfCandidates->at(i).id()) != 4) {
                        //  std::cout<<"pf cand id: "<<l1pfCandidates->at(i).id()<<std::endl;
                        l1extra_.pfCandId.push_back(l1pfCandidates->at(i).id());
                        l1extra_.pfCandPt.push_back(l1pfCandidates->at(i).pt());
                        l1extra_.pfCandChg.push_back(l1pfCandidates->at(i).charge());
                        l1extra_.pfCandEta.push_back(l1pfCandidates->at(i).eta());
                        l1extra_.pfCandPhi.push_back(l1pfCandidates->at(i).phi());
                        l1extra_.pfCandzVtx.push_back(l1pfCandidates->at(i).z0());
                        l1extra_.nPFCands++;
        }


}
