#!/usr/bin/env python
from ROOT import *
import math 

#filename="DoubleMuGun_muontree"
filename="DoubleMu_GMTIso_ID"

#filename="MinBias_PU200_v10"
#filename="DY_PU200_v10"

f = TFile( '/nfs/cms/cepeda/trigger/'+filename+'.root')
#f = TFile( '/scratch/cepeda/trigger/'+filename+'.root')
#f = TFile( '/scratch/cepeda/trigger/DYMerged.root')# L1NtuplePhaseII_Step1.root' )
#tree = f.Get("l1PhaseIITree/L1PhaseIITree")
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")

tree.AddFriend("genTree/L1GenTree",f)

entries=tree.GetEntries()

print (entries)

TH1.GetDefaultSumw2()


minPt=2
maxPt= 100

etaMin=0
etaMax=2.4
name="_all_"


# ISO KIND 

name+="_Q98_"


#etaMin=0.
#etaMax=0.83
#name="_barrel_"

#etaMin=1.24 # 1.24 #0.83 # 1.24
#etaMax=2.4 #  2.4  #1.24 
#name="_endcap_"

#etaMin=0.83
#etaMax=1.24
#name="_overlap_"

branch='gmtTkMuon'
binsEta=50
bins=20
start=0
end=100
color=kRed

def formatHisto(name,title,bins,start,end, color=kBlack):
        histo = TH1F(name,title,bins,start,end)
        histo.SetLineColor(color)
        histo.SetMarkerColor(color)
        histo.SetMarkerStyle(20)
        histo.Sumw2()
        return histo

def formatHisto2D(name,title,bins,start,end, bins2,start2,end2,color=kBlack):
        histo = TH2F(name,title,bins,start,end,bins2,start2,end2)
        histo.SetLineColor(color)
        histo.SetMarkerColor(color)
        histo.SetMarkerStyle(20)
        histo.Sumw2()
        return histo




histoPt=formatHisto("genMuonPt","Gen Muon Pt",bins,start,end)
histoEta=formatHisto("genMuonEta","Gen Muon Eta",binsEta,-2.5,2.5)
histoCount=formatHisto("CountGenMuons","CountGenPt20",10,0,10)

histoMatchPt=formatHisto("matchGen_"+branch+"_"+name+"_Pt",name,bins,start,end,color)
histoMatchEta=formatHisto("matchGen_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color)
histoMatchPhi=formatHisto("matchGen_"+branch+"_"+name+"_Phi",name,100,-4,4,color)

histo2DPtEta=formatHisto2D("genMuon2DPtEta","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)
histoMatch2DPtEta=formatHisto2D("matchGen_"+branch+"_"+name+"_2DPtEta","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)
histoMatch2DPtEtaNStubs2=formatHisto2D("matchGen_"+branch+"_"+name+"_2DPtEta_NStubs2","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)
histoMatch2DPtEtaNStubs3=formatHisto2D("matchGen_"+branch+"_"+name+"_2DPtEta_NStubs3","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)
histoMatch2DPtEtaNStubs4=formatHisto2D("matchGen_"+branch+"_"+name+"_2DPtEta_NStubs4","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)

histoMatchPtNStubs2=formatHisto("matchGen_"+branch+"_"+name+"_Pt_NStubs2",name,bins,start,end,color)
histoMatchEtaNStubs2=formatHisto("matchGen_"+branch+"_"+name+"_Eta_NStubs2",name,binsEta,-2.5,2.5,color)
histoMatchPhiNStubs2=formatHisto("matchGen_"+branch+"_"+name+"_Phi_NStubs2",name,100,-4,4,color)

histoMatchPtNStubs3=formatHisto("matchGen_"+branch+"_"+name+"_Pt_NStubs3",name,bins,start,end,color)
histoMatchEtaNStubs3=formatHisto("matchGen_"+branch+"_"+name+"_Eta_NStubs3",name,binsEta,-2.5,2.5,color)
histoMatchPhiNStubs3=formatHisto("matchGen_"+branch+"_"+name+"_Phi_NStubs3",name,100,-4,4,color)

histoMatchPtNStubs4=formatHisto("matchGen_"+branch+"_"+name+"_Pt_NStubs4",name,bins,start,end,color)
histoMatchEtaNStubs4=formatHisto("matchGen_"+branch+"_"+name+"_Eta_NStubs4",name,binsEta,-2.5,2.5,color)
histoMatchPhiNStubs4=formatHisto("matchGen_"+branch+"_"+name+"_Phi_NStubs4",name,100,-4,4,color)

histoL1Pt=formatHisto("match_l1_"+branch+"_"+name+"_Pt",name,bins,start,end,color) 
histoL1Eta=formatHisto("match_l1_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color) 
histoL1Phi=formatHisto("match_l1_"+branch+"_"+name+"_Phi","",100,-4,4,color)
histoL1Stubs=formatHisto("match_l1_"+branch+"_"+name+"_Stubs",name,10,0,10,color)

histoNotMatchedPt=formatHisto("noMatchGen_"+branch+"_"+name+"_Pt",name,bins,start,end,color)
histoNotMatchedEta=formatHisto("noMatchGen_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color)

histoBestDeltaR = formatHisto ("bestDeltaR_"+branch+"_"+name,"best R",100,0,1,color)

histoMatchCheck = formatHisto ("matchCheck_"+branch+"_"+name,"",10,0,10,color)

histoRes = formatHisto ("ptres_"+branch+"_"+name,"ptl1-ptgen / pt gen",100,-1,1,color)

effiPt=formatHisto("effi_"+branch+"_"+name+"_Pt",name,bins,start,end,color)
effiEta=formatHisto("effi_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color)

effiPtNStubs2=formatHisto("effi_"+branch+"_"+name+"_Pt_NStubs2",name,bins,start,end,color)
effiEtaNStubs2=formatHisto("effi_"+branch+"_"+name+"_Eta_NStubs2",name,binsEta,-2.5,2.5,color)

effiPtNStubs3=formatHisto("effi_"+branch+"_"+name+"_Pt_NStubs3",name,bins,start,end,color)
effiEtaNStubs3=formatHisto("effi_"+branch+"_"+name+"_Eta_NStubs3",name,binsEta,-2.5,2.5,color)


eventNo=0

for event in tree:
                if eventNo>entries:
                        break
                eventNo+=1
                count=0
                vectorPt=getattr(event, branch+"Pt")
                vectorEta=getattr(event, branch+"Eta")
                vectorPhi=getattr(event, branch+"Phi")
                vectorStubs=getattr(event, branch+"NStubs")

                vectorIso=getattr(event, branch+"Iso")
                vectorPFIs=getattr(event, branch+"SumPFIsoAllNoMu")

                vectorGenPt=getattr(event, "partPt")
                vectorGenEta=getattr(event,"partEta")
                vectorGenPhi=getattr(event,"partPhi")
                vectorGenId=getattr(event,"partId")
                vectorGenStat=getattr(event,"partStat")

	        vectorPfCandsPt=getattr(event, "pfCandPt")
        	vectorPfCandsId=getattr(event, "pfCandId")
        	vectorPfCandsEta=getattr(event, "pfCandEta")
        	vectorPfCandsPhi=getattr(event, "pfCandPhi")

		vectorIdLUTQuality=getattr(event, branch+"IdLUTQuality")

		if vectorPt.size()<1:
			continue 

                for i in range(0,vectorGenPt.size()):
			if vectorGenStat.at(i)!=1:
				continue 
                        if abs(vectorGenId.at(i))!=13:
                                continue
                        if abs(vectorGenEta.at(i))<etaMin or abs(vectorGenEta.at(i))>etaMax:
                                continue
			if vectorGenPt.at(i)<1: #some cleaning or this takes forever...
				continue
                        if vectorGenPt.at(i)<minPt or vectorGenPt.at(i)>maxPt: #some cleaning or this takes forever...
                                continue
 

			count+=1
 
			histoPt.Fill(vectorGenPt.at(i))
                        histoEta.Fill(vectorGenEta.at(i))

                        histo2DPtEta.Fill(vectorGenPt.at(i),vectorGenEta.at(i))

			bestDeltaR=10
			matchMuon=-1
		
                	for j in range(0,vectorPt.size()):
				deltaEta=abs(vectorEta.at(j)-vectorGenEta.at(i))
				deltaPhi=TVector2.Phi_mpi_pi(vectorPhi.at(j)-vectorGenPhi.at(i))
				deltaR= math.sqrt(deltaEta*deltaEta+deltaPhi*deltaPhi)

				if deltaR<bestDeltaR:
					bestDeltaR=deltaR
					matchMuon=j

			histoBestDeltaR.Fill(bestDeltaR)


            		sumIsoDR04=0
            		sumIsoDR04With002Veto=0
            		sumIsoDR04With002VetoCharged=0


			if matchMuon!=-1:
            		 for k in range (0,vectorPfCandsPt.size()):
                        	dEta= abs(vectorPfCandsEta.at(k)-vectorEta.at(matchMuon))
                        	dPhi= abs(vectorPfCandsPhi.at(k)-vectorPhi.at(matchMuon))
                        	if dPhi>math.pi:
                              		dPhi=2*math.pi-dPhi
                        	dR=math.sqrt(dEta*dEta+dPhi*dPhi)
                        	if dR<0.4:
                            	 if vectorPfCandsId.at(k)!=4:
                               		sumIsoDR04+=vectorPfCandsPt.at(k)
                               		if dR>0.02:
                                   		sumIsoDR04With002Veto+=vectorPfCandsPt.at(k)
                                   		if vectorPfCandsId.at(k)==0:
                                      			sumIsoDR04With002VetoCharged+=vectorPfCandsPt.at(k)


			if bestDeltaR<0.1 and matchMuon!=-1:
#                          if abs(vectorEta.at(matchMuon))<etaMin or abs(vectorEta.at(matchMuon))>etaMax:
#                                continue


#				if vectorIso.at(matchMuon)< 12:    # 1,2,3 Abs  ; 4,8,12 Rel
#						continue 
#				if sumIsoDR04With002Veto/vectorPt.at(matchMuon)>0.2:
#					continue 
				

				if vectorIdLUTQuality.at(matchMuon)<98:
					continue


				histoMatchPt.Fill(vectorGenPt.at(i))
				histoMatchCheck.Fill(matchMuon)
                                histoMatchPhi.Fill(vectorGenPhi.at(i))
				histoRes.Fill((vectorPt.at(matchMuon)-vectorGenPt.at(i))/vectorGenPt.at(i))

                                histoL1Phi.Fill(vectorPhi.at(matchMuon))
                                histoL1Pt.Fill(vectorPt.at(matchMuon))
				histoL1Stubs.Fill(vectorStubs.at(matchMuon))

				histoMatch2DPtEta.Fill(vectorGenPt.at(i),vectorGenEta.at(i))
	
                                histoMatchEta.Fill(vectorGenEta.at(i))
                                histoL1Eta.Fill(vectorEta.at(matchMuon))
	
				if(vectorStubs.at(matchMuon)>=2): 
					histoMatchPtNStubs2.Fill(vectorGenPt.at(i))
					histoMatch2DPtEtaNStubs2.Fill(vectorGenPt.at(i),vectorGenEta.at(i))
                                        histoMatchEtaNStubs2.Fill(vectorGenEta.at(i))


                                if(vectorStubs.at(matchMuon)>=3):
                                        histoMatchPtNStubs3.Fill(vectorGenPt.at(i))
                                        histoMatch2DPtEtaNStubs3.Fill(vectorGenPt.at(i),vectorGenEta.at(i))
                                        histoMatchEtaNStubs3.Fill(vectorGenEta.at(i))




			else:
				histoNotMatchedPt.Fill(vectorGenPt.at(i))	
				histoNotMatchedEta.Fill(vectorGenEta.at(i))

		histoCount.Fill(count)

effiPt.Divide(histoMatchPt,histoPt,1,1,"B")
effiEta.Divide(histoMatchEta,histoEta,1,1,"B")

effiPtNStubs2.Divide(histoMatchPtNStubs2,histoPt,1,1,"B")
effiEtaNStubs2.Divide(histoMatchEtaNStubs2,histoEta,1,1,"B")

effiPtNStubs3.Divide(histoMatchPtNStubs3,histoPt,1,1,"B")
effiEtaNStubs3.Divide(histoMatchEtaNStubs3,histoEta,1,1,"B")

out=TFile("effi_example_"+name+filename+".root","RECREATE")
out.cd()

effiPt.Write()
effiEta.Write()

effiPtNStubs2.Write()
effiEtaNStubs2.Write()

effiPtNStubs3.Write()
effiEtaNStubs3.Write()

histoPt.Write() 
histoEta.Write()  
histoCount.Write()

histoMatchPt.Write()
histoMatchEta.Write()
histoMatchPhi.Write()

histo2DPtEta.Write()           
histoMatch2DPtEta.Write()       
histoMatch2DPtEtaNStubs2.Write()
histoMatch2DPtEtaNStubs3.Write()
histoMatch2DPtEtaNStubs4.Write()

histoMatchPtNStubs2.Write() 
histoMatchEtaNStubs2.Write()

histoMatchPtNStubs3.Write() 
histoMatchEtaNStubs3.Write()

histoMatchPtNStubs4.Write() 
histoMatchEtaNStubs4.Write()

histoL1Pt.Write()  
histoL1Eta.Write()  
histoL1Phi.Write()  
histoL1Stubs.Write()

histoNotMatchedPt.Write() 
histoNotMatchedEta.Write()

histoBestDeltaR.Write()

histoMatchCheck.Write()

histoRes.Write()




