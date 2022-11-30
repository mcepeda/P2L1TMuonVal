#!/usr/bin/env python
from ROOT import *
import math

#filename="DoubleMu_GMTIso_ID"
filename="MB_GMTIso_ID"

out=TFile("checks_"+filename+".root","RECREATE")

f = TFile('/nfs/cms/cepeda/trigger/'+filename+'.root')
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")
tree.AddFriend("genTree/L1GenTree",f)

gStyle.SetOptStat(0)

print ("Got the tree!")

entries=1000 # tree.GetEntries()

branch="gmtTkMuon"

checkMatching=  False

if filename=="DoubleMu_GMTIso_ID":
	checkMatching=  True

PtMin=0
PtMax=1000 #10

filename=filename
if checkMatching==True:
  filename+="_Matched"

#filename+="_PtBin0_NStubs2_"
#filename+="_PtBin0_" 


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


for ptBin in range(0,1):
   for etaBin in range(0,1):	

	muonQuality=formatHisto("muonQuality_"+str(ptBin)+"_"+str(etaBin),"muonQuality",300,0,300)
	muonPtBin=formatHisto("muonPtBin_"+str(ptBin)+"_"+str(etaBin),"muonPtBin",20,0,20)
	muonEtaBin=formatHisto("muonEtaBin_"+str(ptBin)+"_"+str(etaBin),"muonEtaBin",10,0,10)
	
	muonPtEtaBin = formatHisto2D("muonPtEtaBin_"+str(ptBin)+"_"+str(etaBin),"",20,0,20,10,0,10)
	
	muonPt=formatHisto("muonPt_"+str(ptBin)+"_"+str(etaBin),"muonPt",300,0,300)
	muonEta=formatHisto("muonEta_"+str(ptBin)+"_"+str(etaBin),"muonEta",50,-2.5,2.5)
	muonNStubs=formatHisto("muonNStubs_"+str(ptBin)+"_"+str(etaBin),"muon NStubs",10,0,10)
	
	
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
	
	        vectorIdLUTEta=getattr(event, branch+"IdLUTEta")
	        vectorIdLUTPt=getattr(event, branch+"IdLUTPt")
	        vectorIdLUTQuality=getattr(event, branch+"IdLUTQuality")
	
	
	        for i in range(0,vectorPt.size()):
	
			if vectorPt.at(i)<PtMin:
	
				continue
	
	                if vectorPt.at(i)>PtMax:
	
	                        continue
	
			if vectorIdLUTPt.at(i)!=ptBin:
				continue


                        if vectorIdLUTEta.at(i)!=etaBin:
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
	
	
	                muonQuality.Fill(vectorIdLUTQuality.at(i))
	                muonPtBin.Fill(vectorIdLUTPt.at(i)) 		
	                muonEtaBin.Fill(vectorIdLUTEta.at(i))
	
	                muonPtEtaBin.Fill(vectorIdLUTPt.at(i),vectorIdLUTEta.at(i))
	
	                muonPt.Fill(vectorPt.at(i))
	                muonEta.Fill(vectorEta.at(i))
	                muonNStubs.Fill(vectorNStubs.at(i))
	
	
	#out=TFile("checks_"+filename+".root","RECREATE")
	out.cd()
	
	muonPtEtaBin.Write()
	muonQuality.Write()
	muonPtBin.Write()
	muonEtaBin.Write()
	muonNStubs.Write()
	
