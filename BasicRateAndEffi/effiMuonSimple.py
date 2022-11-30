###############################################
# EXAMPLE: EFFICIENCIES 
# ==================================
#
# This file is a example of how to compute efficiencies
# (Matching gen Muons to GMT Muons with a very simple dR check)
#
##############################################

#!/usr/bin/env python
from ROOT import *
import math 

filename="DoubleMuon_GMTIso"

f = TFile( '/nfs/cms/cepeda/trigger/'+filename+'.root')
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")

tree.AddFriend("genTree/L1GenTree",f)

entries=tree.GetEntries()

TH1.GetDefaultSumw2()

# CONFIGURATION
################

minPt=2
maxPt= 100

etaMin=0
etaMax=2.4

# LABEL for bookeeping
name="_EXAMPLE_SIMPLEEFFI_"

branch='gmtTkMuon'
binsEta=50
bins=20
start=0
end=100
color=kRed

print ("=========================================================")
print ("Computing Isolation Efficiencies from %s" %filename)
print ("Total Events: %d" %entries)
print ("Pt Range: %.0f - %.0f" %(minPt,maxPt))
print ("Eta Range: %.1f - %.1f" %(etaMin,etaMax))
print ("=========================================================")


# HISTOGRAM DEFINITION
#######################

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

		# Get all branches 
                vectorPt=getattr(event, branch+"Pt") # GMT Muons
                vectorEta=getattr(event, branch+"Eta")
                vectorPhi=getattr(event, branch+"Phi")
                vectorStubs=getattr(event, branch+"NStubs")

                vectorGenPt=getattr(event, "partPt") # Gen Particles
                vectorGenEta=getattr(event,"partEta")
                vectorGenPhi=getattr(event,"partPhi")
                vectorGenId=getattr(event,"partId")
                vectorGenStat=getattr(event,"partStat")


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

			histoBestDeltaR.Fill(bestDeltaR) # Saving this for further checks

                        # Now check matching: fill histograms only for triggered muons 

			if bestDeltaR<0.1 and matchMuon!=-1:

			   # Check also the eta of the l1 muon?	
#                          if abs(vectorEta.at(matchMuon))<etaMin or abs(vectorEta.at(matchMuon))>etaMax:
#                                continue

				# If you want to check some additional criteria (ID/Qual),
				# it would go here 
				# if (!myCondition) continue  

				
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

                                # Check what happens with other cuts, for instance the
                                # number of NStubs
				if(vectorStubs.at(matchMuon)>=2): 
					histoMatchPtNStubs2.Fill(vectorGenPt.at(i))
					histoMatch2DPtEtaNStubs2.Fill(vectorGenPt.at(i),vectorGenEta.at(i))
                                        histoMatchEtaNStubs2.Fill(vectorGenEta.at(i))

			else:
				# Save the gen muons we didnt match to understand why:
				histoNotMatchedPt.Fill(vectorGenPt.at(i))	
				histoNotMatchedEta.Fill(vectorGenEta.at(i))

		histoCount.Fill(count)


# To compute the efficiency: ratio of gen muons matched to l1  over total of
# gen muons (using the binomial option B)
 
effiPt.Divide(histoMatchPt,histoPt,1,1,"B")
effiEta.Divide(histoMatchEta,histoEta,1,1,"B")

effiPtNStubs2.Divide(histoMatchPtNStubs2,histoPt,1,1,"B")
effiEtaNStubs2.Divide(histoMatchEtaNStubs2,histoEta,1,1,"B")


# SAVE OUTPUT
#################

print ("Saving  the efficiencies in effi_example_%s_%sfilename.root" %(name,filename))

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




