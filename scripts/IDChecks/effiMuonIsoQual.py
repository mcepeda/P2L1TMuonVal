# EXAMPLE: Applying ID Cuts 
# WARNING: NOT CLEANED YET 

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
maxPt= 5

etaMin=0
etaMax=2.4

branch='gmtTkMuon'
binsEta=20
bins=20
start=0
end=10
color=kRed


# QualCut 

name="_NOCUT_Pt2-5_"



LUT98=[53, 94, 123, 125, 125, 125, 124, 125, 124, 125, 123, 125, 124, 95, 0, 179,
       31, 62, 63, 63, 63, 64, 64, 63, 64, 63, 63, 63, 62, 128, 0, 129,
       33, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 91, 125, 94,
       32, 63, 63, 63, 64, 64, 63, 63, 63, 63, 63, 64, 64, 94, 0, 124,
       32, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 62, 0, 91,
       32, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 93, 130, 125,
       32, 128, 127, 127, 126, 126, 126, 126, 126, 126, 126, 126, 129, 154, 193, 156,
       32, 157, 160, 159, 157, 158, 161, 157, 157, 157, 159, 158, 158, 157, 255, 193,
       32, 96, 95, 95, 95, 95, 95, 95, 98, 95, 95, 95, 96, 95, 130,   98,
       49, 95, 95, 95, 95, 66, 66, 94, 95, 94, 94, 95, 95, 95, 96, 125,
       32, 98, 97, 98, 97, 98, 97, 97, 98, 98, 97, 98, 98, 97, 98, 98,
       38, 96, 98, 98, 97, 98, 98, 98, 98, 97, 96, 98, 98, 98, 98, 95,
       33, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95]



constant_lt_tpsID =[ 40, 56, 64, 88, 64, 32, 60, 56, 56, 56, 56, 56, 56, 56, 56, 56,
                     28, 56, 56, 54, 36, 36, 36, 36, 36, 36, 36, 36, 32, 28, 28, 28,
                     28, 52, 56, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56,
                     28, 56, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56,
                     28, 52, 36, 36, 36, 36, 36, 36, 36, 36, 56, 56, 36, 56, 36, 36,
                     28, 60, 60, 60, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56,
                     28,120,120,120, 92, 92, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
                     28,120,152,128,100,124, 80, 80, 64,100, 64, 64, 64, 64, 64, 64,
                     28, 88, 92, 64, 92, 60, 60, 60, 92, 60, 60, 60, 60, 60, 60, 60,
                     36, 88, 88, 64, 64, 60, 60, 60, 60, 60, 60, 60, 92, 92, 92, 92,
                     28, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88,
                     28, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92,
                     28, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92,
                     64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
                     64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,
                     64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64]



NoCutsInGaps = [53, 94, 123, 125, 125, 125, 124, 125, 124, 125, 123, 125, 124, 95, 0, 179,
#       31, 62, 63, 63, 63, 64, 64, 63, 64, 63, 63, 63, 62, 128, 0, 129,
       28, 56, 56, 54, 36, 36, 36, 36, 36, 36, 36, 36, 32, 28, 28, 28,
#       33, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 91, 125, 94,
       28, 56, 56, 54, 36, 36, 36, 36, 36, 36, 36, 36, 32, 28, 28, 28,
#       32, 63, 63, 63, 64, 64, 63, 63, 63, 63, 63, 64, 64, 94, 0, 124,
       28, 56, 56, 54, 36, 36, 36, 36, 36, 36, 36, 36, 32, 28, 28, 28,
#       32, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 62, 0, 91,
       28, 52, 36, 36, 36, 36, 36, 36, 36, 36, 56, 56, 36, 56, 36, 36,

       32, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 93, 130, 125,
       32, 128, 127, 127, 126, 126, 126, 126, 126, 126, 126, 126, 129, 154, 193, 156,
       32, 157, 160, 159, 157, 158, 161, 157, 157, 157, 159, 158, 158, 157, 255, 193,
       32, 96, 95, 95, 95, 95, 95, 95, 98, 95, 95, 95, 96, 95, 130,   98,
       49, 95, 95, 95, 95, 66, 66, 94, 95, 94, 94, 95, 95, 95, 96, 125,
       32, 98, 97, 98, 97, 98, 97, 97, 98, 98, 97, 98, 98, 97, 98, 98,
       38, 96, 98, 98, 97, 98, 98, 98, 98, 97, 96, 98, 98, 98, 98, 95,
       33, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95]



# 98%
thresholdQual98=[53,31,33,32,32,32,32,32,32,49,32,38,33]
# 95%
thresholdQual95=[59,33,53,40,47,60,58,58,53,64,41,49,38]
# 90%
thresholdQual90=[75,51,60,61,61,91,124,123,88,93,65,75,44]
# 95%
thresholdQual85=[87,60,64,63,63,95,153,156,97,104,95,95,51]

thresholdQualNoCut=[0]*13

thresholdQual=thresholdQualNoCut

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


	        vectorIdLUTEta=getattr(event, branch+"IdLUTEta")
        	vectorIdLUTPt=getattr(event, branch+"IdLUTPt")
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


            		sumIsoDR02=0
            		sumIsoDR02With002Veto=0
            		sumIsoDR02With002VetoCharged=0


			if matchMuon!=-1:
            		 for k in range (0,vectorPfCandsPt.size()):
                        	dEta= abs(vectorPfCandsEta.at(k)-vectorEta.at(matchMuon))
                        	dPhi= abs(vectorPfCandsPhi.at(k)-vectorPhi.at(matchMuon))
                        	if dPhi>math.pi:
                              		dPhi=2*math.pi-dPhi
                        	dR=math.sqrt(dEta*dEta+dPhi*dPhi)
                        	if dR<0.2:
                            	 if vectorPfCandsId.at(k)!=4:
                               		sumIsoDR02+=vectorPfCandsPt.at(k)
                               		if dR>0.02:
                                   		sumIsoDR02With002Veto+=vectorPfCandsPt.at(k)
                                   		if vectorPfCandsId.at(k)==0:
                                      			sumIsoDR02With002VetoCharged+=vectorPfCandsPt.at(k)


			if bestDeltaR<0.1 and matchMuon!=-1:
#                          if abs(vectorEta.at(matchMuon))<etaMin or abs(vectorEta.at(matchMuon))>etaMax:
#                                continue


#				if vectorIso.at(matchMuon)< 12:    # 1,2,3 Abs  ; 4,8,12 Rel
#						continue 
#				if sumIsoDR02With002Veto/vectorPt.at(matchMuon)>0.2:
#					continue 
				
			        # Check Qual:  
				qual=True

				if vectorIdLUTPt.at(matchMuon)==0:
					binEta=vectorIdLUTEta.at(matchMuon)
					if vectorIdLUTQuality.at(matchMuon)<thresholdQual[binEta]: # this is for low Ptt
						qual=False

				findBin=vectorIdLUTPt.at(matchMuon) | (vectorIdLUTEta.at(matchMuon) <<4)
#				if vectorIdLUTQuality.at(matchMuon)<NoCutsInGaps[findBin]:   # Hybrid
				if vectorIdLUTQuality.at(matchMuon)<constant_lt_tpsID[findBin]: # Michalis tune 
								#LUT98[findBin]: # Apply 98% to all 
			                         qual=False

				if qual==False:
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

			else:
				histoNotMatchedPt.Fill(vectorGenPt.at(i))	
				histoNotMatchedEta.Fill(vectorGenEta.at(i))

		histoCount.Fill(count)

effiPt.Divide(histoMatchPt,histoPt,1,1,"B")
effiEta.Divide(histoMatchEta,histoEta,1,1,"B")

effiPtNStubs2.Divide(histoMatchPtNStubs2,histoPt,1,1,"B")
effiEtaNStubs2.Divide(histoMatchEtaNStubs2,histoEta,1,1,"B")

out=TFile("effi_example_"+name+filename+".root","RECREATE")
out.cd()

effiPt.Write()
effiEta.Write()

effiPtNStubs2.Write()
effiEtaNStubs2.Write()

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




