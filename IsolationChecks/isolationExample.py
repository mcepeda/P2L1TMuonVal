# EXAMPLE OF HOW TO FILL VALIDATION PLOTS FOR GMT MUONS 
# ====================================================
# This program:
# - Checks GMTTkMuons starting from a "gmtTkMuonChecksTree" tree (with some internal
# gmTKMuon information beyond what the L1TNtuples for Phase2 store 
# - Fills validation plots for muon quantities 
# - Can run on MinimumBias (computing rates) and on Signal Samples (checking for matching
# to gen level) 
# - The Pt/Eta range to run over is configurable by ranges (check 'Configuration' section)  
# - As an example, compute isolation variables  (pf vs hw)


#!/usr/bin/env python
import math
from ROOT import *


# Get the trees
#==============

filename="MinBias_GMTIso" # Background
#filename="DoubleMuon_GMTIso" # Signal

myfilepath = '/nfs/cms/cepeda/trigger/'  # Change to your path 

f = TFile(myfilepath+filename+'.root',"READONLY")
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree") # basic tree for muons
tree.AddFriend("genTree/L1GenTree",f) # 'friend' the gen level tree

gStyle.SetOptStat(0)

entries=tree.GetEntries()

branch="gmtTkMuon"

checkMatching=   False
if filename=="DoubleMuon_GMTIso":
        checkMatching=  True


# Configuration 
#===============
#(This can be moved to the command line)

PtMin=0
PtMax=1000 #10

EtaMin=0
EtaMax=2.5

#Outfile Name (change!!)
suffix="_EXAMPLE"   

print ("==================================================")
print ("Filling validation plots for %s" %filename)
print ("Total Events: %d" %entries)
print ("Pt Range %.0f - %.0f" %(PtMin,PtMax))
print ("Eta Range %.1f - %.1f" %(EtaMin,EtaMax))
print ("==================================================")

filename=filename+suffix
if checkMatching==True:
   print ("Matching to gen for muons Enabled!!")
   filename+="_Matched"


# Define Histograms
#================= 
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

muonQuality=formatHisto("muonQuality","muonQuality",500,0,500)
muonPt=formatHisto("muonPt","muonPt",50,0,100)
muonEta=formatHisto("muonEta","muonEta",50,-2.5,2.5)
muonIso=formatHisto("muonIso","muonIso",20,0,20)
muonPFIso=formatHisto("muonPFIso","muonPFIso",50,0,100)
muonPFIsoCharged=formatHisto("muonPFIsoCharged","muonPFIsoCharged",50,0,100)
muonPFIsoRel=formatHisto("muonPFIsoRel","muonPFIsoRel",100,0,5)
muonNStubs=formatHisto("muonNStubs","muonNStubs",10,0,10)

muonIso2D=formatHisto2D("muonIso2D","muonIso abs vs rel, L/M/T",4,0,4,4,0,4)

muonQualityPt=formatHisto2D("muonQualityPt","muonQuality vs Pt",500,0,500,50,0,100)
muonIsoPt=formatHisto2D("muonIsoPt","muonIso vs Pt",20,0,20,50,0,100)
muonPFIsoRelPt=formatHisto2D("muonPFIsoRelPt","muonPFIsoRel vs Pt",100,0,5,50,0,100)
muonNStubsPt=formatHisto2D("muonNStubsPt","muonNStubs vs Pt",10,0,10,50,0,100)

leadPt=formatHisto("leadPt","leadPt",50,0,100)
leadPtIso0p2=formatHisto("leadPtIso0p2","leadPtIso0p2",50,0,100)
leadPtIso0p5=formatHisto("leadPtIso0p5","leadPtIso0p5",50,0,100)
leadPtIso1=formatHisto("leadPtIso1","leadPtIso1",50,0,100)
leadPtIso2=formatHisto("leadPtIso2","leadPtIso2",50,0,100)

leadPtIsoTKT=formatHisto("leadPtIsoTKT","leadPtIsoTKT",50,0,100)
leadPtIsoTKL=formatHisto("leadPtIsoTKL","leadPtIsoTKL",50,0,100)


eventNo=0

#  EVENT LOOP 
#=============

print ("Running over tree....")
for event in tree:
        if eventNo>entries:
                break
        if eventNo%100000 == 0:
                        print ("....%d" %eventNo)

        eventNo+=1

        # Get the branches you need :
        vectorPt=getattr(event, branch+"Pt")
        vectorEta=getattr(event, branch+"Eta")
        vectorPhi=getattr(event, branch+"Phi")
        #vectorD0=getattr(event, branch+"D0")
        #vectorZ0=getattr(event, branch+"Z0")
        #vectorChg=getattr(event, branch+"Chg")
        vectorIso=getattr(event, branch+"Iso")
        vectorQual=getattr(event, branch+"Qual")
        #vectorBeta=getattr(event, branch+"Beta")
        vectorNStubs=getattr(event, branch+"NStubs")

        vectorPFIso=getattr(event, branch+"SumPFIsoAllNoMu")
        vectorPFIsoCharged=getattr(event, branch+"SumPFIsoCharged")

        vectorPfCandsPt=getattr(event, "pfCandPt")
        vectorPfCandsId=getattr(event, "pfCandId")
        vectorPfCandsEta=getattr(event, "pfCandEta")
        vectorPfCandsPhi=getattr(event, "pfCandPhi")

        notFilled=True

        # Loop over the vectors to access muon Pt, Eta, etc...

        for i in range(0,vectorPt.size()):

            # Do some selection: 

            if vectorPt.at(i)<PtMin:
			continue

            if vectorPt.at(i)>PtMax:
                  continue

            if abs(vectorEta.at(i))<EtaMin:
                  continue

            if abs(vectorEta.at(i))>EtaMax:
                  continue

#            if vectorNStubs.at(i)<2:
#                  continue


            # Check of the generator level information (for efficiencies/signal)
            # The genInfo comes from the 'friend' tree genTree
            if checkMatching==True:
	 
                   bestDeltaR=10
                   trueMuon=-1
   
                   for j in range(0,event.partPt.size()):
                           if event.partStat.at(j)!=1:
                                   continue # we only want muons with status==1 (=stable)
                           if abs(event.partId.at(j))!=13:
                                   continue # 13==muon. Skip all others.  
                           if event.partPt.at(j)<1:
                                   continue # remove very low pt stuff
                           if abs(event.partEta.at(j))>2.5:
                                   continue # stay in acceptance  
   
			   # Check the angle: 
                           deltaEta=abs(vectorEta.at(i)-event.partEta.at(j))
                           deltaPhi=TVector2.Phi_mpi_pi(vectorPhi.at(i)-event.partPhi.at(j))
                           deltaR= math.sqrt(deltaEta*deltaEta+deltaPhi*deltaPhi)
   
                           if deltaR<bestDeltaR:
                               bestDeltaR=deltaR
                               trueMuon=j
  
		   #you might want to remove also the true muons that are out of the detector acceptance 
                   #if  abs(vectorEta.at(i))<etaMin or abs(vectorEta.at(i))>etaMax:
                   #        continue
   
		   # Check the match, and if not skip this l1muon
                   if bestDeltaR>0.1 or trueMuon==-1:
                            continue

#            This is just a printout for debugging 
#            if  vectorPFIso.at(i)/vectorPt.at(i) > 0.9 and vectorPFIso.at(i)/vectorPt.at(i) <1.1 :
#                  print ("Muon PT %2.2f,ETA %2.2f,PHI %2.2f,SUMISO %2.2f): " %(vectorPt.at(i),vectorEta.at(i),vectorPhi.at(i),vectorPFIso.at(i)) )
#                  print ("Cands in DR=0.4:")


            # Compute the isolation starting from the pfCandidates branches:
            sumIsoDR02=0  # Sum in a DR02 cone 
            sumIsoDR02With002Veto=0 # Sum with an annulus, 0.002-0.2 (to not self-veto) 
            sumIsoDR02With002VetoCharged=0 # Only charged 

            for k in range (0,vectorPfCandsPt.size()):
			# angle:
                        dEta= abs(vectorPfCandsEta.at(k)-vectorEta.at(i))
                        dPhi= abs(vectorPfCandsPhi.at(k)-vectorPhi.at(i))
                        if dPhi>math.pi:
                              dPhi=2*math.pi-dPhi
                        dR=math.sqrt(dEta*dEta+dPhi*dPhi)
			# count:
                        if dR<0.2:
#                           print ("...cand PT %2.2f,ETA %2.2f,PHI %2.2f, ID %2d, DR %2.2f:" %(vectorPfCandsPt.at(k),vectorPfCandsEta.at(k),vectorPfCandsPhi.at(k),vectorPfCandsId.at(k), dR))  
                            if vectorPfCandsId.at(k)!=4:
                               sumIsoDR02+=vectorPfCandsPt.at(k)
                               if dR>0.02:
                                   sumIsoDR02With002Veto+=vectorPfCandsPt.at(k)
                                   if vectorPfCandsId.at(k)==0: # This ID shows the type. 0== charged particles
                                      sumIsoDR02With002VetoCharged+=vectorPfCandsPt.at(k) 


	    # Now fill all the histograms:

            # Histograms with all muons:
            muonQuality.Fill(vectorQual.at(i))
            muonPt.Fill(vectorPt.at(i))
            muonEta.Fill(vectorEta.at(i))
            muonPFIsoRel.Fill(sumIsoDR02With002Veto/vectorPt.at(i))
            muonPFIso.Fill(sumIsoDR02With002Veto)
            muonPFIsoCharged.Fill(sumIsoDR02With002VetoCharged/vectorPt.at(i))
            muonIso.Fill(vectorIso.at(i))
            muonNStubs.Fill(vectorNStubs.at(i))

            # For fun lets do a hwIso plot that is more human readable
            absIso=int(vectorIso.at(i))&3 
            relIso=( int(vectorIso.at(i)) >>2)&3

            muonIso2D.Fill(absIso,relIso)

            muonQualityPt.Fill(vectorQual.at(i),vectorPt.at(i))
            muonPFIsoRelPt.Fill(sumIsoDR02With002Veto/vectorPt.at(i),vectorPt.at(i))
            muonNStubsPt.Fill(vectorNStubs.at(i),vectorPt.at(i))
            muonIsoPt.Fill(vectorIso.at(i),vectorPt.at(i))


            # Histograms with only the lead muon information 
            # Note: vectorPt is sorted by Pt already

            if notFilled==True:
		leadPt.Fill(vectorPt.at(i))
		if sumIsoDR02With002Veto/vectorPt.at(i) < 2: 
 			leadPtIso2.Fill(vectorPt.at(i))
   	        if sumIsoDR02With002Veto/vectorPt.at(i) < 1:  
                        leadPtIso1.Fill(vectorPt.at(i))
                if sumIsoDR02With002Veto/vectorPt.at(i) < 0.5:  
                        leadPtIso0p5.Fill(vectorPt.at(i))
                if sumIsoDR02With002Veto/vectorPt.at(i) < 0.2:
                        leadPtIso0p2.Fill(vectorPt.at(i))
	
		if vectorIso.at(i)>=12:
			leadPtIsoTKT.Fill(vectorPt.at(i))
                if vectorIso.at(i)>=4:
                        leadPtIsoTKL.Fill(vectorPt.at(i))
		notFilled=False	


# Create rate plots
# =================
 
# For this, we want plots where each bin shows the amount of events passing a Pt threshold: 
# - Compute the integral (Pt,Inf) starting the the 'leadPt' plots
# - Normalize it to the total rate at 200 PU
# - There are other ways of doing this, directly from the tree, but this way is useful to
#   have validation plots  + rate plots in one go) 
# - This does SingleMuon plots, for DoubleMuon you need to plot the 2nd muon passing the
#   cuts (etc)

# Careful! For this to correspond to a rate it needs to be done on a NuGun/MB sample and
# disabling matching!! 

# To normalize:  total rate / entries in the tree 
totalrate=31038.0/entries

# In a function:
def doRate(histo,name):
        historate=histo.Clone()
        historate.SetName(name)
        for i in range(0,historate.GetNbinsX()):
                integral=historate.Integral(i+1,-1) # > and not >=
                historate.SetBinContent(i,integral)
        historate.Scale(totalrate)
        return historate

# Now do all the isolation plots:
rate=doRate(leadPt,"All")
rateIso0p2=doRate(leadPtIso0p2,"IsoRel0p2")
rateIso0p5=doRate(leadPtIso0p5,"IsoRel0p5")
rateIso1=doRate(leadPtIso1,"IsoRel1")
rateIso2=doRate(leadPtIso2,"IsoRel2")
rateIsoTKT=doRate(leadPtIsoTKT,"IsoRelTKT")
rateIsoTKL=doRate(leadPtIsoTKL,"IsoRelTKL")




# Save all the histograms for later plotting 

print ("Saving the results in checks_%s.root" %filename)
out=TFile("checks_"+filename+".root","RECREATE")
out.cd()

muonQuality.Write()
muonPt.Write()
muonEta.Write()
muonIso.Write()
muonPFIso.Write()
muonPFIsoCharged.Write()
muonPFIsoRel.Write()
muonNStubs.Write()

muonIso2D.Write()

muonQualityPt.Write()
muonIsoPt.Write()
muonPFIsoRelPt.Write()
muonNStubsPt.Write()

leadPt.Write()
leadPtIso2.Write()
leadPtIso1.Write()
leadPtIso0p5.Write()
leadPtIso0p2.Write()
leadPtIsoTKL.Write()
leadPtIsoTKT.Write()

rate.Write()
rateIso2.Write()
rateIso1.Write()
rateIso0p5.Write()
rateIso0p2.Write()
rateIsoTKL.Write()
rateIsoTKT.Write()
