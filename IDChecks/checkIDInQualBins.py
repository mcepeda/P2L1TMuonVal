# EXAMPLE: Check the Quality in Pt/Eta bins
# WARNING: NOT CLEANED YET 

#!/usr/bin/env python
from ROOT import *
import math

filename="DoubleMu_GMTIso_ID"
#filename="MB_GMTIso_ID"

checkMatching=  False
if filename=="DoubleMu_GMTIso_ID":
        checkMatching=  True

if checkMatching==True:
  filename+="_Matched"

out=TFile("checks_"+filename+".root","RECREATE")


f = TFile('/nfs/cms/cepeda/trigger/'+filename+'.root')
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")
tree.AddFriend("genTree/L1GenTree",f)

gStyle.SetOptStat(0)

print ("Got the tree!")

entries= tree.GetEntries()

branch="gmtTkMuon"

checkMatching=  False

PtMin=0
PtMax=1000 #10

eventNo=0

print ("=========================================================")
print ("Checking Quality bins (Pt,Eta)  %s" %filename)
print ("Total Events: %d" %entries)
print ("Pt Range: %.0f - %.0f" %(minPt,maxPt))
print ("Eta Range: %.1f - %.1f" %(etaMin,etaMax))
print ("=========================================================")


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

muonQuality={}
muonPtBin={}
muonEtaBin={}
muonPtEtaBin={}
muonPt={}
muonEta={}
muonNStubs={}


# 16*14 Bins in Pt and Eta are set for the quality, create hisotgrams for each bin 
for ptBin in range(0,16):
   for etaBin in range(0,14):	
#	print ("muonQuality_"+str(ptBin)+"_"+str(etaBin))
	muonQuality[str(ptBin)+"_"+str(etaBin)]=formatHisto("muonQuality_"+str(ptBin)+"_"+str(etaBin),"muonQuality",300,0,300)
	muonPtBin[str(ptBin)+"_"+str(etaBin)]  =formatHisto("muonPtBin_"+str(ptBin)+"_"+str(etaBin),"muonPtBin",20,0,20)
	muonEtaBin[str(ptBin)+"_"+str(etaBin)] =formatHisto("muonEtaBin_"+str(ptBin)+"_"+str(etaBin),"muonEtaBin",10,0,10)
	
	muonPtEtaBin[str(ptBin)+"_"+str(etaBin)]= formatHisto2D("muonPtEtaBin_"+str(ptBin)+"_"+str(etaBin),"",20,0,20,10,0,10)
	
	muonPt[str(ptBin)+"_"+str(etaBin)]      =formatHisto("muonPt_"+str(ptBin)+"_"+str(etaBin),"muonPt",300,0,300)
	muonEta[str(ptBin)+"_"+str(etaBin)]     =formatHisto("muonEta_"+str(ptBin)+"_"+str(etaBin),"muonEta",50,-2.5,2.5)
	muonNStubs[str(ptBin)+"_"+str(etaBin)]  =formatHisto("muonNStubs_"+str(ptBin)+"_"+str(etaBin),"muon NStubs",10,0,10)
	
	
# Loop over all bins 
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

		# Specific Stub branches 	
	        vectorStubsEtaRegion=getattr(event, branch+"StubsEtaRegion")
	        vectorStubsPhiRegion=getattr(event, branch+"StubsPhiRegion")
	        vectorStubsDepthRegion=getattr(event, branch+"StubsDepthRegion")
	        vectorStubsQuality=getattr(event, branch+"StubsQuality")
	        vectorStubsEtaQuality=getattr(event, branch+"StubsEtaQuality")
	        vectorStubsTfLayer=getattr(event, branch+"StubsTfLayer")
	        vectorStubsType=getattr(event, branch+"StubsType")

		# Branches related to the Quality (Eta and Pt Bin, Quality)	
	        vectorIdLUTEta=getattr(event, branch+"IdLUTEta")
	        vectorIdLUTPt=getattr(event, branch+"IdLUTPt")
	        vectorIdLUTQuality=getattr(event, branch+"IdLUTQuality")
	

		# Loop over muons (l1 muons!)	
	        for i in range(0,vectorPt.size()):
	
			if vectorPt.at(i)<PtMin:
				continue
	
	                if vectorPt.at(i)>PtMax:
	                        continue
	

			# Check matching to generator level 	
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

			# This is the Bin in Pt and Eta in the LUT 
			binPtEta=str(vectorIdLUTPt.at(i))+"_"+str(vectorIdLUTEta.at(i))

			# Fill the plots 	
	                muonQuality[binPtEta].Fill(vectorIdLUTQuality.at(i))
	                muonPtBin[binPtEta].Fill(vectorIdLUTPt.at(i)) 		
	                muonEtaBin[binPtEta].Fill(vectorIdLUTEta.at(i))
	
	                muonPtEtaBin[binPtEta].Fill(vectorIdLUTPt.at(i),vectorIdLUTEta.at(i))
	
	                muonPt[binPtEta].Fill(vectorPt.at(i))
	                muonEta[binPtEta].Fill(vectorEta.at(i))
	                muonNStubs[binPtEta].Fill(vectorNStubs.at(i))
	


# Loop to save the many plots (per bin) 

for ptBin in range(0,16):
   for etaBin in range(0,14):
	#out=TFile("checks_"+filename+".root","RECREATE")
	out.cd()
	muonPtEtaBin[str(ptBin)+"_"+str(etaBin)].Write()
	muonQuality[str(ptBin)+"_"+str(etaBin)].Write()
	muonPtBin[str(ptBin)+"_"+str(etaBin)].Write()
	muonEtaBin[str(ptBin)+"_"+str(etaBin)].Write()
	muonNStubs[str(ptBin)+"_"+str(etaBin)].Write()
	
