###############################################
# EXAMPLE: PF ISOLATION EFFICIENCIES 
# ==================================
#
# This file is a example of how to compute isolation efficiencies
# In this case, building PF Isolation from pfCandidates (in a DR=02 cone 
# and with a DR=002 Veto). The threshold can be configured. 
# For other kinds of isolation (eg: hw), the condition must be changed
#
##############################################


#!/usr/bin/env python
from ROOT import *
import math 

# INPUT
########

filename="DoubleMuon_GMTIso"
myfilepath='/nfs/cms/cepeda/trigger/'
f = TFile( myfilepath+filename+'.root')
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree") # gmt info
tree.AddFriend("genTree/L1GenTree",f) # generator info
entries=tree.GetEntries()
TH1.GetDefaultSumw2()

# CONFIGURATION
################

branch='gmtTkMuon'

minPt=2
maxPt= 100

etaMin=0
etaMax=2.4

isolationThreshold= 0.2

# LABEL for bookeeping 
name="_EXAMPLE_"

binsEta=50
bins=20
start=0
end=100
color=kRed

print ("=========================================================")
print ("Computing PF Isolation Efficiencies from %s" %filename)
print ("Total Events: %d" %entries)
print ("Pt Range: %.0f - %.0f" %(minPt,maxPt))
print ("Eta Range: %.1f - %.1f" %(etaMin,etaMax))
print ("Isolation threshold (PF DR02 With 002 Veto):  %.2f" %isolationThreshold)
print ("=========================================================")


#========================================================


# HISTOGRAM FORMAT & DEFINITION
###############################

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

# BASIC HISTOS (VALIDATION): 

histoPt=formatHisto("genMuonPt","Gen Muon Pt",bins,start,end)
histoEta=formatHisto("genMuonEta","Gen Muon Eta",binsEta,-2.5,2.5)
histoCount=formatHisto("CountGenMuons","CountGenPt20",10,0,10)

histoMatchPt=formatHisto("matchGen_"+branch+"_"+name+"_Pt",name,bins,start,end,color)
histoMatchEta=formatHisto("matchGen_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color)
histoMatchPhi=formatHisto("matchGen_"+branch+"_"+name+"_Phi",name,100,-4,4,color)

histo2DPtEta=formatHisto2D("genMuon2DPtEta","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)
histoMatch2DPtEta=formatHisto2D("matchGen_"+branch+"_"+name+"_2DPtEta","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)
histoMatch2DPtEtaNStubs2=formatHisto2D("matchGen_"+branch+"_"+name+"_2DPtEta_NStubs2","Gen Muon Pt vs Eta",bins,start,end,binsEta, -2.5,2-5)

histoMatchPtNStubs2=formatHisto("matchGen_"+branch+"_"+name+"_Pt_NStubs2",name,bins,start,end,color)
histoMatchEtaNStubs2=formatHisto("matchGen_"+branch+"_"+name+"_Eta_NStubs2",name,binsEta,-2.5,2.5,color)
histoMatchPhiNStubs2=formatHisto("matchGen_"+branch+"_"+name+"_Phi_NStubs2",name,100,-4,4,color)

histoL1Pt=formatHisto("match_l1_"+branch+"_"+name+"_Pt",name,bins,start,end,color) 
histoL1Eta=formatHisto("match_l1_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color) 
histoL1Phi=formatHisto("match_l1_"+branch+"_"+name+"_Phi","",100,-4,4,color)
histoL1Stubs=formatHisto("match_l1_"+branch+"_"+name+"_Stubs",name,10,0,10,color)

histoNotMatchedPt=formatHisto("noMatchGen_"+branch+"_"+name+"_Pt",name,bins,start,end,color)
histoNotMatchedEta=formatHisto("noMatchGen_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color)

histoBestDeltaR = formatHisto ("bestDeltaR_"+branch+"_"+name,"best R",100,0,1,color)

histoMatchCheck = formatHisto ("matchCheck_"+branch+"_"+name,"",10,0,10,color)

histoRes = formatHisto ("ptres_"+branch+"_"+name,"ptl1-ptgen / pt gen",100,-1,1,color)

# EFFICIENCY HISTOS: 

effiPt=formatHisto("effi_"+branch+"_"+name+"_Pt",name,bins,start,end,color)
effiEta=formatHisto("effi_"+branch+"_"+name+"_Eta",name,binsEta,-2.5,2.5,color)

effiPtNStubs2=formatHisto("effi_"+branch+"_"+name+"_Pt_NStubs2",name,bins,start,end,color)
effiEtaNStubs2=formatHisto("effi_"+branch+"_"+name+"_Eta_NStubs2",name,binsEta,-2.5,2.5,color)

#========================================================
#
#  EVENT LOOP
###############

eventNo=0
# if you want to run a check over a few events:
# entries=1000


for event in tree:
                if eventNo>entries:
                        break
                eventNo+=1
                count=0

                # Get the branches that you need 
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


                # Start with the generator level: true muons 

		# Loop over true muons: 
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
 
			# Fill Histograms for all generator level muons:

			histoPt.Fill(vectorGenPt.at(i))
                        histoEta.Fill(vectorGenEta.at(i))
                        histo2DPtEta.Fill(vectorGenPt.at(i),vectorGenEta.at(i))

			# Now lets see if that muon was triggered: find a gmt match

			bestDeltaR=10
			matchMuon=-1
		
                	for j in range(0,vectorPt.size()):
				deltaEta=abs(vectorEta.at(j)-vectorGenEta.at(i))
				deltaPhi=TVector2.Phi_mpi_pi(vectorPhi.at(j)-vectorGenPhi.at(i))
				deltaR= math.sqrt(deltaEta*deltaEta+deltaPhi*deltaPhi)

				if deltaR<bestDeltaR:
					bestDeltaR=deltaR
					matchMuon=j

			histoBestDeltaR.Fill(bestDeltaR) # Save the DR for inspection


			# Now lets compute isolation:

            		sumIsoDR02=0
            		sumIsoDR02With002Veto=0
            		sumIsoDR02With002VetoCharged=0

			# Only if we found the match, do the isolation computation
			# (Loop over pfCands around the muon)

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

			# Now check matching and isolation: fill histograms only for
			# isolated muons

			if bestDeltaR<0.1 and matchMuon!=-1:

				# THIS DEFINES THE PF ISOLATION CUT 
				# (For other kinds of isolations, this condition should be
				# modified!)
				if sumIsoDR02With002Veto/vectorPt.at(matchMuon)>isolationThreshold:
					continue 

                                # Fill the gen information for matched muons 
                                histoMatchPt.Fill(vectorGenPt.at(i))
                                histoMatchCheck.Fill(matchMuon)
                                histoMatchPhi.Fill(vectorGenPhi.at(i))
                                histoMatchEta.Fill(vectorGenEta.at(i))
                                histoMatch2DPtEta.Fill(vectorGenPt.at(i),vectorGenEta.at(i))

                                # Resolution:
                                histoRes.Fill((vectorPt.at(matchMuon)-vectorGenPt.at(i))/vectorGenPt.at(i))

                                # Save also the l1 information for further study
                                histoL1Phi.Fill(vectorPhi.at(matchMuon))
                                histoL1Pt.Fill(vectorPt.at(matchMuon))
                                histoL1Stubs.Fill(vectorStubs.at(matchMuon))
                                histoL1Eta.Fill(vectorEta.at(matchMuon))

				# Check what happens with other cuts, eg NStubs
				if(vectorStubs.at(matchMuon)>=2): 
					histoMatchPtNStubs2.Fill(vectorGenPt.at(i))
					histoMatch2DPtEtaNStubs2.Fill(vectorGenPt.at(i),vectorGenEta.at(i))
                                        histoMatchEtaNStubs2.Fill(vectorGenEta.at(i))

			else:
				# How are the muons that we miss? 	
				histoNotMatchedPt.Fill(vectorGenPt.at(i))	
				histoNotMatchedEta.Fill(vectorGenEta.at(i))

		histoCount.Fill(count) # How many muons?

# To compute the efficiency: ratio of gen muons matched to l1 (and isolated) over total of
# gen muons (using the binomial option B) 

effiPt.Divide(histoMatchPt,histoPt,1,1,"B")
effiEta.Divide(histoMatchEta,histoEta,1,1,"B")

effiPtNStubs2.Divide(histoMatchPtNStubs2,histoPt,1,1,"B")
effiEtaNStubs2.Divide(histoMatchEtaNStubs2,histoEta,1,1,"B")


# Save everything 
print ("Saving  the efficiencies in effi_example_%s_%sfilename.root" %(name,filename))
out=TFile("effi_example_"+name+"_"+filename+".root","RECREATE")
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

histoMatchPtNStubs2.Write() 
histoMatchEtaNStubs2.Write()

histoL1Pt.Write()  
histoL1Eta.Write()  
histoL1Phi.Write()  
histoL1Stubs.Write()

histoNotMatchedPt.Write() 
histoNotMatchedEta.Write()

histoBestDeltaR.Write()

histoMatchCheck.Write()

histoRes.Write()




