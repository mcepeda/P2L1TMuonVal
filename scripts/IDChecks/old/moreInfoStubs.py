#!/usr/bin/env python
from ROOT import *
import math

filename="Merged_DoubleMu_GMTRev_2"

f = TFile('/scratch/cepeda/trigger/'+filename+'.root')
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")
tree.AddFriend("genTree/L1GenTree",f)

gStyle.SetOptStat(0)

print ("Got the tree!")

entries=tree.GetEntries()

branch="gmtTkMuon"

checkMatching=   False

if filename=="DoubleMuGun_muontree":
	checkMatching=  True

Check2Stubs =  True

PtMin=2
PtMax=1000 #10

filename=filename
if checkMatching==True:
  filename+="_Matched"
if Check2Stubs==True:
  filename+="_2STUBS"

#+"_2STUBS" #+"_Matched"#+"_Pt2To10"



eventNo=0


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

stubQuality=formatHisto("stubQuality","stubQuality",5,-0.5,4.5)
stubQuality2D=formatHisto2D("stubQuality2D","stubQuality vs NStubs",5,-0.5,4.5,5,-0.5,4.5)
pos2D=formatHisto2D("pos2D","eta Region vs phi Region",13,-6.5,6.5,40,-1,39)

depth=formatHisto("depth","depth",6,-0.5,5.5)
NStations=formatHisto("NStations","Stations Crossed",6,0,6)

NStationsPt=formatHisto2D("NStations2D","Stations Crossed",6,0,6,100,0,100)


stubQualityEta2D=formatHisto2D("stubQualityEta2D","stubQuality vs Eta Region",5,-0.5,4.5,13,-6.5,6.5)
stubQualityPhi2D_Barrel=formatHisto2D("stubQualityPhi2D_Barrel","stubQuality vs Phi Region (Barrel) ",5,-0.5,4.5,40,-1,39)
stubQualityPhi2D_Endcap=formatHisto2D("stubQualityPhi2D_Endcap","stubQuality vs Phi Region (Endcap) ",5,-0.5,4.5,40,-1,39) 
stubQualityDepth2D=formatHisto2D("stubQualityDepth2D","stubQuality vs Depth",5,-0.5,4.5,6,-0.5,5.5)

depthEta2D=formatHisto2D("depthEta2D","depth vs Eta Region",6,-0.5,5.5,13,-6.5,6.5)
depthPhi2D_Barrel=formatHisto2D("depthPhi2D_Barrel","depth vs Phi Region (Barrel)",6,-0.5,5.5,40,-1,39)
depthPhi2D_Endcap=formatHisto2D("depthPhi2D_Endcap","depth vs Phi Region (Endcap)",6,-0.5,5.5,40,-1,39)

depthNStubs2D=formatHisto2D("depthNStubs2D","depth of stubs vs total NStubs",6,-0.5,5.5,5,-0.5,4.5)

depthNStubsV22D=formatHisto2D("depthNStubsV22D","NStubs in each Station per event",6,-0.5,5.5,5,-0.5,4.5)

depthNStubsV22D_2to5=formatHisto2D("depthNStubsV22D_2to5","NStubs in each Station per event (2-5 GeV)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_5to10=formatHisto2D("depthNStubsV22D_5to10","NStubs in each Station per event (5-10 GeV)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_Over10=formatHisto2D("depthNStubsV22D_Over10","NStubs in each Station per event (>10 GeV)",6,-0.5,5.5,5,-0.5,4.5)

depthNStubsV22D_2to5_B=formatHisto2D("depthNStubsV22D_2to5_B","NStubs in each Station per event (2-5 GeV, Barrel)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_5to10_B=formatHisto2D("depthNStubsV22D_5to10_B","NStubs in each Station per event (5-10 GeV, Barrel)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_Over10_B=formatHisto2D("depthNStubsV22D_Over10_B","NStubs in each Station per event (>10 GeV, Barrel)",6,-0.5,5.5,5,-0.5,4.5)

depthNStubsV22D_2to5_E=formatHisto2D("depthNStubsV22D_2to5_E","NStubs in each Station per event (2-5 GeV, Endcap)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_5to10_E=formatHisto2D("depthNStubsV22D_5to10_E","NStubs in each Station per event (5-10 GeV, Endcap)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_Over10_E=formatHisto2D("depthNStubsV22D_Over10_E","NStubs in each Station per event (>10 GeV, Endcap)",6,-0.5,5.5,5,-0.5,4.5)

depthNStubsV22D_2to5_O=formatHisto2D("depthNStubsV22D_2to5_O","NStubs in each Station per event (2-5 GeV, Overlap)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_5to10_O=formatHisto2D("depthNStubsV22D_5to10_O","NStubs in each Station per event (5-10 GeV, Overlap)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_Over10_O=formatHisto2D("depthNStubsV22D_Over10_O","NStubs in each Station per event (>10 GeV, Overlap)",6,-0.5,5.5,5,-0.5,4.5)



depthNStubsV22D_2to5_NStubs2=formatHisto2D("depthNStubsV22D_2to5_NStubs2","NStubs in each Station per event (2-5 GeV)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_5to10_NStubs2=formatHisto2D("depthNStubsV22D_5to10_NStubs2","NStubs in each Station per event (5-10 GeV)",6,-0.5,5.5,5,-0.5,4.5)
depthNStubsV22D_Over10_NStubs2=formatHisto2D("depthNStubsV22D_Over10_NStubs2","NStubs in each Station per event (>10 GeV)",6,-0.5,5.5,5,-0.5,4.5)


MuonPtAll=formatHisto("MuonPtAll","MuonPtAll",50,0,50)
MuonPtNStubs2=formatHisto("MuonPtNStubs2","MuonPtNStubs2",50,0,50)
MuonPtStubQual2=formatHisto("MuonPtStubsQual2","MuonPtStubQual2",50,0,50)
MuonPtStubQual2Or3Stubs=formatHisto("MuonPtStubsQual2or3Stubs","MuonPtStubQual2or3Stubs",50,0,50)

MuonEtaAll=formatHisto("MuonEtaAll","MuonEtaAll",50,-2.5,2.5)
MuonEtaNStubs2=formatHisto("MuonEtaNStubs2","MuonEtaNStubs2",50,-2.5,2.5)
MuonEtaStubQual2=formatHisto("MuonEtaStubsQual2","MuonEtaStubQual2",50,-2.5,2.5)
MuonEtaStubQual2Or3Stubs=formatHisto("MuonEtaStubsQual2or3Stubs","MuonEtaStubQual2or3Stubs",50,-2.5,2.5)

pos2DMuon=formatHisto2D("pos2DMuon","Eta vs Phi, Global",50,-2.5,2.5,100,-3.14,3.14)
eta2D = formatHisto2D("etavsRegionEta","Muon Eta vs Stub Eta",50,-2.5,2.5,13,-6.5,6.5)
phi2D_Barrel = formatHisto2D("phivsRegionPhi_Barrel","Muon Phi vs Stub Phi Region (Barrel) ",100,-3.14,3.14,40,-1,39)
phi2D_Endcap = formatHisto2D("phivsRegionPhi_Endcap","Muon Phi vs Stub Phi (Endcap)",100,-3.14,3.14,40,-1,39)

pos2DMuonUgly=formatHisto2D("pos2DMuonUgly","Eta vs Phi, Global",50,-2.5,2.5,100,-3.14,3.14)
MuonPtAllUgly=formatHisto("MuonPtAllUgly","MuonPtAll",50,0,50)
MuonEtaAllUgly=formatHisto("MuonEtaAllUgly","MuonEtaAll",50,-2.5,2.5)
PtEta2DMuonUgly=formatHisto2D("PtEta2DMuonUgly","Eta vs Pt, Global",50,-2.5,2.5,100,0,100)

pos2DMuonClean=formatHisto2D("pos2DMuonClean","Eta vs Phi, Global",50,-2.5,2.5,100,-3.14,3.14)
MuonPtAllClean=formatHisto("MuonPtAllClean","MuonPtAll",50,0,50)
MuonEtaAllClean=formatHisto("MuonEtaAllClean","MuonEtaAll",50,-2.5,2.5)
PtEta2DMuonClean=formatHisto2D("PtEta2DMuonClean","Eta vs Pt, Global",50,-2.5,2.5,100,0,100)



for event in tree:
        if eventNo>entries:
                break
        if eventNo%100000 == 0:
                        print ("....%d" %eventNo)

        eventNo+=1

        vectorPt=getattr(event, branch+"Pt")
        vectorEta=getattr(event, branch+"Eta")
        vectorPhi=getattr(event, branch+"Phi")
        vectorD0=getattr(event, branch+"D0")
        vectorZ0=getattr(event, branch+"Z0")
        vectorChg=getattr(event, branch+"Chg")
        vectorIso=getattr(event, branch+"Iso")
        vectorQual=getattr(event, branch+"Qual")
        vectorBeta=getattr(event, branch+"Beta")
        vectorNStubs=getattr(event, branch+"NStubs")

        vectorStubsEtaRegion=getattr(event, branch+"StubsEtaRegion")
        vectorStubsPhiRegion=getattr(event, branch+"StubsPhiRegion")
        vectorStubsDepthRegion=getattr(event, branch+"StubsDepthRegion")
        vectorStubsQuality=getattr(event, branch+"StubsQuality")
        vectorStubsEtaQuality=getattr(event, branch+"StubsEtaQuality")
        vectorStubsTfLayer=getattr(event, branch+"StubsTfLayer")

        vectorStubsType=getattr(event, branch+"StubsType")

        for i in range(0,vectorPt.size()):

		if vectorPt.at(i)<PtMin:

			continue

                if vectorPt.at(i)>PtMax:

                        continue




  		if checkMatching==True:
	 
                   bestDeltaR=10
                   trueMuon=-1
   
                   for j in range(0,event.partPt.size()):
                           if event.partStat.at(j)!=1:
                                   continue # intermediate muon
                           if abs(event.partId.at(j))!=13:
                                   continue # not a muon 
                           if event.partPt.at(j)<1:
                                   continue # this one could go?
                           if abs(event.partEta.at(j))>2.5:
                                   continue # not in acceptance  
   
                           deltaEta=abs(vectorEta.at(i)-event.partEta.at(j))
                           deltaPhi=TVector2.Phi_mpi_pi(vectorPhi.at(i)-event.partPhi.at(j))
                           deltaR= math.sqrt(deltaEta*deltaEta+deltaPhi*deltaPhi)
   
                           if deltaR<bestDeltaR:
                               bestDeltaR=deltaR
                               trueMuon=j
   
                   #if  abs(vectorEta.at(i))<etaMin or abs(vectorEta.at(i))>etaMax:
                   #        continue
   
     		   if bestDeltaR>0.1 or trueMuon==-1:
   			continue
   
		


                if vectorNStubs.at(i)!=vectorStubsEtaRegion.at(i).size():
                        print ("THIS SHOULDNT HAPPEN!")

 #               print (i,vectorPt.at(i),vectorEta.at(i),vectorPhi.at(i),vectorNStubs.at(i),vectorStubsEtaRegion.at(i).size())

		stubsWithQual23=0


		pos2DMuon.Fill(vectorEta.at(i),vectorPhi.at(i))

		MuonPtAll.Fill(vectorPt.at(i))
                MuonEtaAll.Fill(vectorEta.at(i))


		muonsInSt1=0
                muonsInSt2=0
                muonsInSt3=0
                muonsInSt4=0

		if Check2Stubs==True and vectorNStubs.at(i)<2:
			continue

		MuonPtNStubs2.Fill(vectorPt.at(i))
                MuonEtaNStubs2.Fill(vectorEta.at(i))


		stubsStr=""

                for j in range(0,vectorNStubs.at(i)):
#                        print ("....",j,vectorStubsEtaRegion.at(i).at(j),vectorStubsPhiRegion.at(i).at(j),vectorStubsDepthRegion.at(i).at(j),vectorStubsQuality.at(i).at(j),event.gmtTkMuonStubsType.at(i).at(j))
			stubQuality2D.Fill(vectorStubsQuality.at(i).at(j),vectorNStubs.at(i))
                        stubQuality.Fill(vectorStubsQuality.at(i).at(j))
			depth.Fill(vectorStubsDepthRegion.at(i).at(j))
			stubQualityEta2D.Fill(vectorStubsQuality.at(i).at(j),vectorStubsEtaRegion.at(i).at(j))
                        stubQualityDepth2D.Fill(vectorStubsQuality.at(i).at(j),vectorStubsDepthRegion.at(i).at(j))
			eta2D.Fill(vectorEta.at(i),vectorStubsEtaRegion.at(i).at(j))
			depthEta2D.Fill(vectorStubsDepthRegion.at(i).at(j),vectorStubsEtaRegion.at(i).at(j))
			pos2D.Fill(vectorStubsEtaRegion.at(i).at(j),vectorStubsPhiRegion.at(i).at(j))

			depthNStubs2D.Fill(vectorStubsDepthRegion.at(i).at(j),vectorNStubs.at(i))

			if vectorStubsDepthRegion.at(i).at(j)==1: 
				muonsInSt1+=1
                        if vectorStubsDepthRegion.at(i).at(j)==2:
                                muonsInSt2+=1
                        if vectorStubsDepthRegion.at(i).at(j)==3:
                                muonsInSt3+=1
                        if vectorStubsDepthRegion.at(i).at(j)==4:
                                muonsInSt4+=1

			if vectorStubsType.at(i).at(j)==1:
				depthPhi2D_Barrel.Fill(vectorStubsDepthRegion.at(i).at(j),vectorStubsPhiRegion.at(i).at(j))
                        	stubQualityPhi2D_Barrel.Fill(vectorStubsQuality.at(i).at(j),vectorStubsPhiRegion.at(i).at(j))
                        	phi2D_Barrel.Fill(vectorPhi.at(i),vectorStubsPhiRegion.at(i).at(j))
			else:
                                depthPhi2D_Endcap.Fill(vectorStubsDepthRegion.at(i).at(j),vectorStubsPhiRegion.at(i).at(j))
                                stubQualityPhi2D_Endcap.Fill(vectorStubsQuality.at(i).at(j),vectorStubsPhiRegion.at(i).at(j))
                                phi2D_Endcap.Fill(vectorPhi.at(i),vectorStubsPhiRegion.at(i).at(j))
			if vectorStubsQuality.at(i).at(j)>1:
				stubsWithQual23+=1
			
#			thisStub='....%d %2d %2d %2d %2d %2d %2d %2d \n' %(j,vectorStubsEtaRegion.at(i).at(j),vectorStubsPhiRegion.at(i).at(j),vectorStubsDepthRegion.at(i).at(j),vectorStubsQuality.at(i).at(j),vectorStubsEtaQuality.at(i).at(j),event.gmtTkMuonStubsType.at(i).at(j),event.gmtTkMuonStubsTfLayer.at(i).at(j))
#			stubsStr+=thisStub


		stationsCrossed=(muonsInSt1>0)+(muonsInSt2>0)+(muonsInSt3>0)+(muonsInSt4>0)
		NStations.Fill(stationsCrossed)
		NStationsPt.Fill(stationsCrossed,vectorPt.at(i))

		if muonsInSt1>1 or muonsInSt2>1 or muonsInSt3>1 or muonsInSt4>1:
#		if muonsInSt1==1 and muonsInSt2==1 and muonsInSt3==1 and muonsInSt4==1:
#                if muonsInSt1==2 and vectorNStubs.at(i)==2: 
#		if stationsCrossed <2:
                	#print (i,vectorPt.at(i),vectorEta.at(i),vectorPhi.at(i),vectorNStubs.at(i))
			#print ("Depth:",muonsInSt1,muonsInSt2,muonsInSt3,muonsInSt4)
                        #print stubsStr
	                pos2DMuonUgly.Fill(vectorEta.at(i),vectorPhi.at(i))
        	        MuonPtAllUgly.Fill(vectorPt.at(i))
                	MuonEtaAllUgly.Fill(vectorEta.at(i))
			PtEta2DMuonUgly.Fill(vectorEta.at(i),vectorPt.at(i))	

		elif  stationsCrossed >=2: 

			pos2DMuonClean.Fill(vectorEta.at(i),vectorPhi.at(i))
	
			MuonPtAllClean.Fill(vectorPt.at(i))
        	        MuonEtaAllClean.Fill(vectorEta.at(i))
                        PtEta2DMuonClean.Fill(vectorEta.at(i),vectorPt.at(i)) 

			depthNStubsV22D.Fill(1,muonsInSt1)
        	        depthNStubsV22D.Fill(2,muonsInSt2)
                	depthNStubsV22D.Fill(3,muonsInSt3)
                	depthNStubsV22D.Fill(4,muonsInSt4)

#
#		if (vectorPt.at(i)>2 and vectorPt.at(i)<5):
#	                depthNStubsV22D_2to5.Fill(1,muonsInSt1)
#                        depthNStubsV22D_2to5.Fill(2,muonsInSt2)
#                        depthNStubsV22D_2to5.Fill(3,muonsInSt3)
#                        depthNStubsV22D_2to5.Fill(4,muonsInSt4)
#
#			if abs(vectorEta.at(i))<0.83:
#	                        depthNStubsV22D_2to5_B.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_2to5_B.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_2to5_B.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_2to5_B.Fill(4,muonsInSt4)
#
#			elif abs(vectorEta.at(i))<1.24:
#	                        depthNStubsV22D_2to5_O.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_2to5_O.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_2to5_O.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_2to5_O.Fill(4,muonsInSt4)
#
#			else:
#	                        depthNStubsV22D_2to5_E.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_2to5_E.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_2to5_E.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_2to5_E.Fill(4,muonsInSt4)
#
#                        depthNStubsV22D_2to5.Fill(1,muonsInSt1)
#                        depthNStubsV22D_2to5.Fill(2,muonsInSt2)
#                        depthNStubsV22D_2to5.Fill(3,muonsInSt3)
#                        depthNStubsV22D_2to5.Fill(4,muonsInSt4)
#
#			if vectorNStubs.at(i)>=2:
#	                  depthNStubsV22D_2to5_NStubs2.Fill(1,muonsInSt1)
#        	          depthNStubsV22D_2to5_NStubs2.Fill(2,muonsInSt2)
#                	  depthNStubsV22D_2to5_NStubs2.Fill(3,muonsInSt3)
#                	  depthNStubsV22D_2to5_NStubs2.Fill(4,muonsInSt4)
#
#		elif (vectorPt.at(i)>5 and vectorPt.at(i)<10):
#                        depthNStubsV22D_5to10.Fill(1,muonsInSt1)
#                        depthNStubsV22D_5to10.Fill(2,muonsInSt2)
#                        depthNStubsV22D_5to10.Fill(3,muonsInSt3)
#                        depthNStubsV22D_5to10.Fill(4,muonsInSt4)
#
#			if abs(vectorEta.at(i))<0.83:
#	                        depthNStubsV22D_5to10_B.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_5to10_B.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_5to10_B.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_5to10_B.Fill(4,muonsInSt4)
#
#                        elif abs(vectorEta.at(i))<1.24:
#	                        depthNStubsV22D_5to10_O.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_5to10_O.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_5to10_O.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_5to10_O.Fill(4,muonsInSt4)
#			else:
#	                        depthNStubsV22D_5to10_E.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_5to10_E.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_5to10_E.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_5to10_E.Fill(4,muonsInSt4)
#
#                        if vectorNStubs.at(i)>=2:
#                          depthNStubsV22D_5to10_NStubs2.Fill(1,muonsInSt1)
#                          depthNStubsV22D_5to10_NStubs2.Fill(2,muonsInSt2)
#                          depthNStubsV22D_5to10_NStubs2.Fill(3,muonsInSt3)
#                          depthNStubsV22D_5to10_NStubs2.Fill(4,muonsInSt4)
#
#
#		elif vectorPt.at(i)>10:
#                        depthNStubsV22D_Over10.Fill(1,muonsInSt1)
#                        depthNStubsV22D_Over10.Fill(2,muonsInSt2)
#                        depthNStubsV22D_Over10.Fill(3,muonsInSt3)
#                        depthNStubsV22D_Over10.Fill(4,muonsInSt4)
#
#                        if abs(vectorEta.at(i))<0.83:
#	                        depthNStubsV22D_Over10_B.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_Over10_B.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_Over10_B.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_Over10_B.Fill(4,muonsInSt4)
#
#                        elif abs(vectorEta.at(i))<1.24:
#	                       	depthNStubsV22D_Over10_O.Fill(1,muonsInSt1)
#        	               	depthNStubsV22D_Over10_O.Fill(2,muonsInSt2)
#                	       	depthNStubsV22D_Over10_O.Fill(3,muonsInSt3)
#                       		depthNStubsV22D_Over10_O.Fill(4,muonsInSt4)
#
#			else:
#	                        depthNStubsV22D_Over10_E.Fill(1,muonsInSt1)
#        	                depthNStubsV22D_Over10_E.Fill(2,muonsInSt2)
#                	        depthNStubsV22D_Over10_E.Fill(3,muonsInSt3)
#                        	depthNStubsV22D_Over10_E.Fill(4,muonsInSt4)
#
#                        if vectorNStubs.at(i)>=2:
#                          depthNStubsV22D_Over10_NStubs2.Fill(1,muonsInSt1)
#                          depthNStubsV22D_Over10_NStubs2.Fill(2,muonsInSt2)
#                          depthNStubsV22D_Over10_NStubs2.Fill(3,muonsInSt3)
#                          depthNStubsV22D_Over10_NStubs2.Fill(4,muonsInSt4)


#		if vectorNStubs.at(i)>1:
#	                MuonPtNStubs2.Fill(vectorPt.at(i))
#                        MuonEtaNStubs2.Fill(vectorEta.at(i))
#
#	        if stubsWithQual23>1:
#		                MuonPtStubsQual2.Fill(vectorPt.at(i))
#                                MuonEtaStubsQual2.Fill(vectorEta.at(i))
#
#		if stubsWithQual23>1 or vectorNStubs.at(i)>2:
#				MuonPtStubQual2Or3Stubs.Fill(vectorPt.at(i))
#                                MuonEtaStubQual2Or3Stubs.Fill(vectorEta.at(i))
#				




c=TCanvas("c")
stubQuality.Draw("hist")
stubQuality.SetXTitle("Stub Quality")
c.SaveAs(filename+"stubQuality.png")

c2=TCanvas("c2")
stubQuality2D.Draw("colz")
stubQuality2D.SetXTitle("Stub Quality")
stubQuality2D.SetYTitle("Number of Stubs")
c2.SaveAs(filename+"stubQualityvsNStubs.png")

c3=TCanvas("c3")
depth.Draw("hist")
depth.SetXTitle("Station")
c3.SaveAs(filename+"depthStub.png")

c4=TCanvas("c4")
pos2D.Draw("colz")
pos2D.SetXTitle("Eta Region")
pos2D.SetYTitle("Phi Region")
c4.SaveAs(filename+"pos2DStubRegion.png")


c4U=TCanvas("c4U")
pos2DMuonUgly.Draw("colz")
pos2DMuonUgly.SetXTitle("Eta Region")
pos2DMuonUgly.SetYTitle("Phi Region")
c4U.SaveAs(filename+"pos2DStubRegionUgly.png")

c4U=TCanvas("c4U")
PtEta2DMuonUgly.Draw("colz")
PtEta2DMuonUgly.SetXTitle("Eta Region")
PtEta2DMuonUgly.SetYTitle("Phi Region")
c4U.SaveAs(filename+"PtEta2DStubRegionUgly.png")

c4C=TCanvas("c4C")
pos2DMuonClean.Draw("colz")
pos2DMuonClean.SetXTitle("Eta Region")
pos2DMuonClean.SetYTitle("Phi Region")
c4U.SaveAs(filename+"pos2DStubRegionClean.png")

c4C=TCanvas("c4C")
PtEta2DMuonClean.Draw("colz")
PtEta2DMuonClean.SetXTitle("Eta Region")
PtEta2DMuonClean.SetYTitle("Phi Region")
c4C.SaveAs(filename+"PtEta2DStubRegionClean.png")





d=TCanvas("d")
MuonPtAll.Draw("hist")
MuonPtAll.SetMinimum(1)
MuonPtNStubs2.Draw("hist,sames")
MuonPtNStubs2.SetLineColor(kBlue)
MuonPtAllUgly.Draw("hist,sames")
MuonPtAllUgly.SetFillColor(kPink)
MuonPtAllUgly.SetLineColor(kPink)
MuonPtAllUgly.SetXTitle("Muon Pt")
if checkMatching==False:
 d.SetLogy()
d.SaveAs(filename+"MuonPt_uglyremoval.png")

e3=TCanvas("e3")
NStations.Draw("hist")
NStations.SetXTitle("Number of Stations")
e3.SaveAs(filename+"NStationsCrossed.png")

d2=TCanvas("d2")
MuonEtaAll.Draw("hist")
MuonEtaAll.SetMinimum(1)
MuonEtaNStubs2.Draw("hist,sames")
MuonEtaNStubs2.SetLineColor(kBlue)
MuonEtaAllUgly.Draw("hist,sames")
MuonEtaAllUgly.SetFillColor(kPink)
MuonEtaAllUgly.SetLineColor(kPink)
MuonEtaAllUgly.SetXTitle("Muon Eta")
d2.SaveAs(filename+"MuonEta_uglyremoval.png")



d7=TCanvas("d7")
MuonPtAll.Draw("hist")
MuonPtAll.SetMinimum(1)
MuonPtAllClean.Draw("hist,sames")
MuonPtAllClean.SetFillColor(kGreen+1)
MuonPtAllClean.SetLineColor(kGreen+1)
MuonPtAllClean.SetXTitle("Muon Pt")
if checkMatching==False:
 d7.SetLogy()
d7.SaveAs(filename+"MuonPt_cleanremoval.png")

e5=TCanvas("e5")
NStationsPt.Draw("colz")
NStationsPt.SetXTitle("Number of Stations")
NStationsPt.SetYTitle("Muon Pt")
e5.SaveAs(filename+"NStationsCrossedPt.png")

d5=TCanvas("d5")
MuonEtaAll.Draw("hist")
MuonEtaAll.SetMinimum(1)
MuonEtaAllClean.Draw("hist,sames")
MuonEtaAllClean.SetFillColor(kGreen+1)
MuonEtaAllClean.SetLineColor(kGreen+1)
MuonEtaAllClean.SetXTitle("Muon Eta")
d5.SaveAs(filename+"MuonEta_cleanremoval.png")


c5=TCanvas("c5")
stubQualityEta2D.Draw("colz")
stubQualityEta2D.SetXTitle("Stub Quality")
stubQualityEta2D.SetYTitle("Eta Region")
c5.SaveAs(filename+"stubsQualityEta2D.png")


c6=TCanvas("c6")
stubQualityPhi2D_Barrel.Draw("colz")
stubQualityPhi2D_Barrel.SetXTitle("Stub Quality")
stubQualityPhi2D_Barrel.SetYTitle("Phi Region")
c6.SaveAs(filename+"stubsQualityPhi2D_Barrel.png")


c6a=TCanvas("c6a")
stubQualityPhi2D_Endcap.Draw("colz")
stubQualityPhi2D_Endcap.SetXTitle("Stub Quality")
stubQualityPhi2D_Endcap.SetYTitle("Phi Region")
c6a.SaveAs(filename+"stubsQualityPhi2D_Endcap.png")


c7=TCanvas("c7")
stubQualityDepth2D.Draw("colz")
stubQualityDepth2D.SetXTitle("Stub Quality")
stubQualityDepth2D.SetYTitle("Station")
c7.SaveAs(filename+"stubsQualityDepth2D.png")

c8=TCanvas("c8")
MuonPtAll.Draw("hist")
MuonPtAll.SetXTitle("Muon P_{T}")
MuonPtStubQual2Or3Stubs.Draw("hist.sames")
MuonPtStubQual2Or3Stubs.SetLineColor(kBlue)
MuonPtStubQual2.Draw("hist.sames")
MuonPtStubQual2.SetLineColor(kBlack)
MuonPtNStubs2.Draw("hist,sames")
MuonPtNStubs2.SetLineColor(kRed)
c8.SaveAs(filename+"NStubsChecksQualityPt.png")

c9=TCanvas("c9")
MuonEtaAll.Draw("hist")
MuonEtaAll.SetXTitle("Muon P_{T}")
MuonEtaStubQual2Or3Stubs.Draw("hist.sames")
MuonEtaStubQual2Or3Stubs.SetLineColor(kBlue)
MuonEtaStubQual2.Draw("hist.sames")
MuonEtaStubQual2.SetLineColor(kBlack)
MuonEtaNStubs2.Draw("hist,sames")
MuonEtaNStubs2.SetLineColor(kRed)
c9.SaveAs(filename+"NStubsChecksQualityEta.png")


c10=TCanvas("c10")
pos2DMuon.Draw("colz")
pos2DMuon.SetXTitle("Muon #eta")
pos2DMuon.SetYTitle("Muon #phi")
c10.SaveAs(filename+"pos2DMuon.png")



c11=TCanvas("c11")
eta2D.Draw("colz")
eta2D.SetXTitle("Muon #eta")
eta2D.SetYTitle("eta Region")
c11.SaveAs(filename+"Eta2D.png")


c12=TCanvas("c12")
phi2D_Barrel.Draw("colz")
phi2D_Barrel.SetXTitle("Muon #phi")
phi2D_Barrel.SetYTitle("phi Region")
c12.SaveAs(filename+"Phi2D_Barrel.png")

c12b=TCanvas("c12")
phi2D_Endcap.Draw("colz")
phi2D_Endcap.SetXTitle("Muon #phi")
phi2D_Endcap.SetYTitle("phi Region")
c12b.SaveAs(filename+"Phi2D_Endcap.png")

c13=TCanvas("c13")
depthEta2D.Draw("colz")
depthEta2D.SetYTitle("eta Region")
depthEta2D.SetXTitle("Depth")
c13.SaveAs(filename+"depthEta2D.png")


c13a=TCanvas("c13a")
depthPhi2D_Barrel.Draw("colz")
depthPhi2D_Barrel.SetYTitle("phi Region")
depthPhi2D_Barrel.SetXTitle("Depth")
c13a.SaveAs(filename+"depthPhi2D_Barrel.png")


c13b=TCanvas("c13b")
depthPhi2D_Endcap.Draw("colz")
depthPhi2D_Endcap.SetYTitle("phi Region")
depthPhi2D_Endcap.SetXTitle("Depth")
c13b.SaveAs(filename+"depthPhi2D_Endcap.png")


c15=TCanvas("c15")
depthNStubs2D.Draw("colz")
depthNStubs2D.SetXTitle("Depth")
depthNStubs2D.SetYTitle("NStubs (Total)")
c15.SaveAs(filename+"depthNStubs2D.png")


c16=TCanvas("c16")
depthNStubsV22D.Draw("colz")
depthNStubsV22D.SetXTitle("Station")
depthNStubsV22D.SetYTitle("NStubs in each Station")
c16.SaveAs(filename+"StubsPerStation2D.png")

c16a=TCanvas("c16a")
depthNStubsV22D_2to5.Draw("colz")
depthNStubsV22D_2to5.SetXTitle("Station")
depthNStubsV22D_2to5.SetYTitle("NStubs in each Station")
c16a.SaveAs(filename+"StubsPerStation2D_2to5.png")

c16b=TCanvas("c16b")
depthNStubsV22D_5to10.Draw("colz")
depthNStubsV22D_5to10.SetXTitle("Station")
depthNStubsV22D_5to10.SetYTitle("NStubs in each Station")
c16b.SaveAs(filename+"StubsPerStation2D_5to10.png")

c16c=TCanvas("c16c")
depthNStubsV22D_Over10.Draw("colz")
depthNStubsV22D_Over10.SetXTitle("Station")
depthNStubsV22D_Over10.SetYTitle("NStubs in each Station")
c16c.SaveAs(filename+"StubsPerStation2D_Over10.png")

c16a2=TCanvas("c16a2")
depthNStubsV22D_2to5_NStubs2.Draw("colz")
depthNStubsV22D_2to5_NStubs2.SetXTitle("Station")
depthNStubsV22D_2to5_NStubs2.SetYTitle("NStubs in each Station")
c16a2.SaveAs(filename+"StubsPerStation2D_2to5_NStubs2.png")

c16b2=TCanvas("c16b2")
depthNStubsV22D_5to10.Draw("colz")
depthNStubsV22D_5to10.SetXTitle("Station")
depthNStubsV22D_5to10.SetYTitle("NStubs in each Station")
c16b2.SaveAs(filename+"StubsPerStation2D_5to10_NStubs2.png")

c16c2=TCanvas("c16c2")
depthNStubsV22D_Over10_NStubs2.Draw("colz")
depthNStubsV22D_Over10_NStubs2.SetXTitle("Station")
depthNStubsV22D_Over10_NStubs2.SetYTitle("NStubs in each Station")
c16c2.SaveAs(filename+"StubsPerStation2D_Over10_NStubs2.png")


c17a2=TCanvas("c17a2")
depthNStubsV22D_2to5_B.Draw("colz")
depthNStubsV22D_2to5_B.SetXTitle("Station")
depthNStubsV22D_2to5_B.SetYTitle("NStubs in each Station")
c17a2.SaveAs(filename+"StubsPerStation2D_2to5_B.png")

c17b2=TCanvas("c17b2")
depthNStubsV22D_5to10.Draw("colz")
depthNStubsV22D_5to10.SetXTitle("Station")
depthNStubsV22D_5to10.SetYTitle("NStubs in each Station")
c17b2.SaveAs(filename+"StubsPerStation2D_5to10_B.png")

c17c2=TCanvas("c17c2")
depthNStubsV22D_Over10_B.Draw("colz")
depthNStubsV22D_Over10_B.SetXTitle("Station")
depthNStubsV22D_Over10_B.SetYTitle("NStubs in each Station")
c17c2.SaveAs(filename+"StubsPerStation2D_Over10_B.png")


c18a2=TCanvas("c18a2")
depthNStubsV22D_2to5_E.Draw("colz")
depthNStubsV22D_2to5_E.SetXTitle("Station")
depthNStubsV22D_2to5_E.SetYTitle("NStubs in each Station")
c18a2.SaveAs(filename+"StubsPerStation2D_2to5_E.png")

c18b2=TCanvas("c18b2")
depthNStubsV22D_5to10.Draw("colz")
depthNStubsV22D_5to10.SetXTitle("Station")
depthNStubsV22D_5to10.SetYTitle("NStubs in each Station")
c18b2.SaveAs(filename+"StubsPerStation2D_5to10_E.png")

c18c2=TCanvas("c18c2")
depthNStubsV22D_Over10_E.Draw("colz")
depthNStubsV22D_Over10_E.SetXTitle("Station")
depthNStubsV22D_Over10_E.SetYTitle("NStubs in each Station")
c18c2.SaveAs(filename+"StubsPerStation2D_Over10_E.png")


c19a2=TCanvas("c19a2")
depthNStubsV22D_2to5_O.Draw("colz")
depthNStubsV22D_2to5_O.SetXTitle("Station")
depthNStubsV22D_2to5_O.SetYTitle("NStubs in each Station")
c19a2.SaveAs(filename+"StubsPerStation2D_2to5_O.png")

c19b2=TCanvas("c19b2")
depthNStubsV22D_5to10.Draw("colz")
depthNStubsV22D_5to10.SetXTitle("Station")
depthNStubsV22D_5to10.SetYTitle("NStubs in each Station")
c19b2.SaveAs(filename+"StubsPerStation2D_5to10_O.png")

c19c2=TCanvas("c19c2")
depthNStubsV22D_Over10_O.Draw("colz")
depthNStubsV22D_Over10_O.SetXTitle("Station")
depthNStubsV22D_Over10_O.SetYTitle("NStubs in each Station")
c19c2.SaveAs(filename+"StubsPerStation2D_Over10_O.png")





out=TFile("checks_"+filename+".root","RECREATE")
out.cd()
stubQuality.Write()
stubQuality2D.Write()
depth.Write()
pos2D.Write()

stubQualityEta2D.Write()
stubQualityPhi2D_Barrel.Write()
stubQualityPhi2D_Endcap.Write()
stubQualityDepth2D.Write()

MuonPtAll.Write()
MuonPtStubQual2Or3Stubs.Write()
MuonPtStubQual2.Write()
MuonPtNStubs2.Write()

MuonEtaAll.Write()
MuonEtaStubQual2Or3Stubs.Write()
MuonEtaStubQual2.Write()
MuonEtaNStubs2.Write()

depthPhi2D_Barrel.Write()
depthPhi2D_Endcap.Write()
depthEta2D.Write()
eta2D.Write()
phi2D_Barrel.Write()
phi2D_Endcap.Write()
pos2DMuon.Write()

depthNStubs2D.Write()
depthNStubsV22D.Write()

depthNStubsV22D_2to5.Write()
depthNStubsV22D_5to10.Write()
depthNStubsV22D_Over10.Write()

depthNStubsV22D_2to5_NStubs2.Write()
depthNStubsV22D_5to10_NStubs2.Write()
depthNStubsV22D_Over10_NStubs2.Write()

depthNStubsV22D_2to5_B.Write()
depthNStubsV22D_5to10_B.Write()
depthNStubsV22D_Over10_B.Write()

depthNStubsV22D_2to5_E.Write()
depthNStubsV22D_5to10_E.Write()
depthNStubsV22D_Over10_E.Write()

depthNStubsV22D_2to5_O.Write()
depthNStubsV22D_5to10_O.Write()
depthNStubsV22D_Over10_O.Write()

pos2DMuonUgly.Write() 
MuonPtAllUgly.Write() 
MuonEtaAllUgly.Write()
PtEta2DMuonUgly.Write()

pos2DMuonClean.Write()
MuonPtAllClean.Write()
MuonEtaAllClean.Write()
PtEta2DMuonClean.Write()

NStationsPt.Write()
