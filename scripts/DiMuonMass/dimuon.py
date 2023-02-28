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
from ROOT import TLorentzVector

#filename="DoubleMuon_GMTIso"
#f = TFile( '/nfs/cms/cepeda/trigger/'+filename+'.root')

path='/eos/user/c/cepeda/trigger/'
#filename='DoubleMu_GMTIso_ID'
#filename='DYMenu'
#filename='DYLowMass_12_5'
filename="DY_M50_12_5"
label=filename
f= TFile(path+filename+'.root')

tree = f.Get("l1PhaseIITree/L1PhaseIITree")

tree.AddFriend("genTree/L1GenTree",f)

entries=tree.GetEntries()

TH1.GetDefaultSumw2()

# CONFIGURATION
################

minPt=5
maxPt= 1000

etaMin=0
etaMax=2.4

# LABEL for bookeeping
name="_FullEta_Pt5_"

binsEta=50
bins=200
start=0
end=200

print ("=========================================================")
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

histoZMass=formatHisto("ZMass_GmtTk","ZMass GMTTk",bins,start,end)
histoGenZMass=formatHisto("ZMass_Gen","ZMassGen",bins,start,end)
histostaZMass=formatHisto("ZMass_Gmt","ZMass GMT",bins,start,end)

histoResMass2D=formatHisto2D("ResMass_GmtTk","ZMass GMT",bins,start,end,200,-1,1)
histostaResMass2D=formatHisto2D("ResMass_Gmt","ZMass sta",bins,start,end,200,-1,1)

histoResMass2DVL1=formatHisto2D("ResMassVSL1_GmtTk","ZMass GMT",bins,start,end,200,-1,1)
histostaResMass2DVL1=formatHisto2D("ResMassVSL1_Gmt","ZMass sta",bins,start,end,200,-1,1)

histosta2D=formatHisto2D("Mass2D_GenVsGmt","",bins,start,end,bins,start,end)
histo2D=formatHisto2D("Mass2D_GenVsGmtTk","",bins,start,end,bins,start,end)




#========================================================
#
#  EVENT LOOP
###############

eventNo=0

# if you want to run a check over a few events:
#entries=100000

for event in tree:
                if eventNo>entries: 
                        break
                eventNo+=1
                count=0
                if eventNo%2000 == 0:
                        print (eventNo)

		# Get all branches 
                vectorPt=getattr(event, "gmtTkMuonPt") # GMT Muons
                vectorEta=getattr(event, "gmtTkMuonEta")
                vectorPhi=getattr(event, "gmtTkMuonPhi")
                vectorstaPt=getattr(event, "gmtMuonPt") # GMT Muons
                vectorstaEta=getattr(event, "gmtMuonEta")
                vectorstaPhi=getattr(event, "gmtMuonPhi")

                vectorGenPt=getattr(event, "partPt") # Gen Particles
                vectorGenEta=getattr(event,"partEta")
                vectorGenPhi=getattr(event,"partPhi")
                vectorGenId=getattr(event,"partId")
                vectorGenStat=getattr(event,"partStat")

                # GEN 

                nGenPart=vectorGenPt.size()
                leadGM=-1
                secondGM=-1
                genm1=TLorentzVector()
                genm2=TLorentzVector()
                genZ=TLorentzVector()
                genmass=0  

                nGenMuonsInAcc=0 

                if nGenPart>=2: # careful this is all!!
                   # Lets find the two highest pt muons in the eta range 
                   # This could just be done with the first two by Pt, and with a Draw, I'm complicating my life   
                   leadGPt=0
                   secondGPt=0
   

                   for i in range(0,nGenPart):
                          if vectorGenStat.at(i)!=1: #stable
                            continue
                          if abs(vectorGenId.at(i))!=13: # I want muons
                                continue
                          if (vectorGenPt.at(i)<minPt or abs(vectorGenEta.at(i))<etaMin or  abs(vectorGenEta.at(i))>etaMax):
                                 continue
                          nGenMuonsInAcc+=1
                          if vectorGenPt.at(i)>leadGPt:
                                        secondGM=leadGM
                                        leadGM=i
                                        secondGPt=leadGPt
                                        leadGPt=vectorGenPt.at(i)
                          elif vectorGenPt.at(i)>secondGPt:
                                        secondGM=i
                                        secondGPt=vectorGenPt.at(i)
  
                   if nGenMuonsInAcc>=2:
                         genm1.SetPtEtaPhiM(vectorGenPt.at(leadGM),vectorGenEta.at(leadGM),vectorGenPhi.at(leadGM),0.105)
                         genm2.SetPtEtaPhiM(vectorGenPt.at(secondGM),vectorGenEta.at(secondGM),vectorGenPhi.at(secondGM),0.105)
                         genZ=genm1+genm2
                         genmass=genZ.M()
                         histoGenZMass.Fill(genmass)
                         #genmass2=sqrt( 2*vectorGenPt.at(leadGM)*vectorGenPt.at(secondGM)*(cosh(vectorGenEta.at(leadGM)-vectorGenEta.at(secondGM))-cos(vectorGenPhi.at(leadGM)-vectorGenPhi.at(secondGM))))
                         #print ("GEN -->",genmass,genmass2)

                #if nGenMuonsInAcc<2: 
                #        continue

                # L1 gmtTkMuons

                nMuons=vectorPt.size()
                leadM=-1
                secondM=-1
                leadPt=0
                secondPt=0

                m1=TLorentzVector()
                m2=TLorentzVector()
                mass=0
                nMuonsInAcc=0

                if nMuons>=2:

                   # Lets find the two highest pt muons in the eta range 
                   # This could just be done with the first two by Pt, and with a Draw, I complicated my life too much... 
   
                   for j in range(0,nMuons):
                         # print (j,vectorPt.at(j),vectorEta.at(j),vectorPhi.at(j))
                          if (vectorPt.at(j)<minPt or abs(vectorEta.at(j))<etaMin or  abs(vectorEta.at(j))>etaMax):
                                 continue 
                          nMuonsInAcc+=1
                          if vectorPt.at(j)>leadPt:
                                        secondM=leadM
                                        leadM=j 
                                        secondPt=leadPt
                                        leadPt=vectorPt.at(j)                                         
                          elif vectorPt.at(j)>secondPt:
                                        secondM=j
                                        secondPt=vectorPt.at(j)
  
                   #print (nMuons,nMuonsInAcc,leadM,secondM,leadPt,secondPt)
 
                   if nMuonsInAcc>=2 and leadM!=-1 and secondM!=-1: 
                     m1.SetPtEtaPhiM(vectorPt.at(leadM),vectorEta.at(leadM),vectorPhi.at(leadM),0.105)
                     m2.SetPtEtaPhiM(vectorPt.at(secondM),vectorEta.at(secondM),vectorPhi.at(secondM),0.105)
                     Z=m1+m2
                     mass=Z.M()
                     histoZMass.Fill(mass)
   
                     if genmass!=0:
                        res=(mass-genmass)/genmass 
                        histoResMass2D.Fill(genmass,res)
                        histoResMass2DVL1.Fill(mass,res)
                        histo2D.Fill(genmass,mass)

                # L1 GMTMuons (Standalone)

                nstaMuons=vectorstaPt.size()
                leadstaM=-1
                secondstaM=-1
                leadstaPt=0
                secondstaPt=0

                stam1=TLorentzVector()
                stam2=TLorentzVector()
                stamass=0
                nstaMuonsInAcc=0

                if nMuons>=2:

                   # Lets find the two highest pt muons in the eta range 
   
                   for j in range(0,nstaMuons):
                          if (vectorstaPt.at(j)<minPt or abs(vectorstaEta.at(j))<etaMin or  abs(vectorstaEta.at(j))>etaMax):
                                 continue 
                          nstaMuonsInAcc+=1
                          if vectorstaPt.at(j)>leadstaPt:
                                        secondstaM=leadstaM
                                        leadstaM=j 
                                        secondstaPt=leadstaPt
                                        leadstaPt=vectorstaPt.at(j)                                         
                          elif vectorstaPt.at(j)>secondstaPt:
                                        secondstaM=j
                                        secondstaPt=vectorstaPt.at(j)
  
 
                   if nstaMuonsInAcc>=2 and leadstaM!=-1 and secondstaM!=-1: 
                     stam1.SetPtEtaPhiM(vectorstaPt.at(leadstaM),vectorstaEta.at(leadstaM),vectorstaPhi.at(leadstaM),0.105)
                     stam2.SetPtEtaPhiM(vectorstaPt.at(secondstaM),vectorstaEta.at(secondstaM),vectorstaPhi.at(secondstaM),0.105)
                     staZ=stam1+stam2
                     stamass=staZ.M()
                     histostaZMass.Fill(stamass)
                     #if stamass<20:
                         #print ('low mass?', vectorstaPt.at(leadstaM),vectorstaEta.at(leadstaM),vectorstaPt.at(secondstaM),vectorstaEta.at(secondstaM),stamass,nstaMuonsInAcc,nstaMuons)
   
                     if genmass!=0:
                        ressta=(stamass-genmass)/genmass 
                        histostaResMass2D.Fill(genmass,ressta)
                        histostaResMass2DVL1.Fill(stamass,ressta)
                        histosta2D.Fill(genmass,stamass)




out=TFile("dimuon_example_"+name+label+".root","RECREATE")
out.cd()

histoZMass.Write()
histostaZMass.Write()
histoGenZMass.Write()
histoResMass2D.Write()
histostaResMass2D.Write()
histostaResMass2DVL1.Write()
histosta2D.Write()
histoResMass2DVL1.Write()
histo2D.Write()


