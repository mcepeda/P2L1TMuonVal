#!/usr/bin/env python
import math
from ROOT import *

filename="MB_GMTIso_ID"
#filename="DoubleMuon_GMTIso"

f = TFile('/nfs/cms/cepeda/trigger/'+filename+'.root',"READONLY")
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")
tree.AddFriend("genTree/L1GenTree",f)

gStyle.SetOptStat(0)

print ("Got the tree!")

entries=tree.GetEntries()

print (entries)

branch="gmtTkMuon"

checkMatching=   False

if filename=="DoubleMuon_GMTIso":
	checkMatching=  True

PtMin=0
PtMax=1000 #10

EtaMin=0
EtaMax=2.5
#EtaMax=0.83

#EtaMin=0.83
#EtaMax=1.24

#EtaMin=1.24
#EtaMax=2.5

suffix="Qual_All"

# 98%
thresholdQual98=[53,31,33,32,32,32,32,32,32,49,32,38,33]
# 95%
thresholdQual95=[59,33,53,40,47,60,58,58,53,64,41,49,38]
# 90%
thresholdQual90=[75,51,60,61,61,91,124,123,88,93,65,75,44]
# 95%
thresholdQual85=[87,60,64,63,63,95,153,156,97,104,95,95,51]


filename=filename+suffix
if checkMatching==True:
  filename+="_Matched"

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

muonQuality=formatHisto("muonQuality","muonQuality",500,0,500)
muonPt=formatHisto("muonPt","muonPt",100,0,100)
muonEta=formatHisto("muonEta","muonEta",50,-2.5,2.5)
muonNStubs=formatHisto("muonNStubs","muonNStubs",10,0,10)

leadPt=formatHisto("leadPt","leadPt",100,0,100)
leadPtQ98=formatHisto("leadPtQ98","leadPtQ98",100,0,100)
leadPtQ95=formatHisto("leadPtQ95","leadPtQ95",100,0,100)
leadPtQ90=formatHisto("leadPtQ90","leadPtQ90",100,0,100)
leadPtQ85=formatHisto("leadPtQ85","leadPtQ85",100,0,100)
leadPtDefHWQ=formatHisto("leadPtDefHWQ","leadPt",100,0,100)


leadEtaBin=formatHisto("leadEtaBin","leadEtaBin",13,0,12)
leadEtaBinQ98=formatHisto("leadEtaBinQ98","leadEtaBinQ98",13,0,12)
leadEtaBinQ95=formatHisto("leadEtaBinQ95","leadEtaBinQ95",13,0,12)
leadEtaBinQ90=formatHisto("leadEtaBinQ90","leadEtaBinQ90",13,0,12)
leadEtaBinQ85=formatHisto("leadEtaBinQ85","leadEtaBinQ85",13,0,12)
leadEtaBinDefHWQ=formatHisto("leadEtaBinDefHWQ","leadEtaBin",13,0,12)


for event in tree:
        if eventNo>entries:
                break
        if eventNo%10000 == 0:
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
        vectorIdLUTEta=getattr(event, branch+"IdLUTEta")
        vectorIdLUTPt=getattr(event, branch+"IdLUTPt")
        vectorIdLUTQuality=getattr(event, branch+"IdLUTQuality")

        notFilled=True

        for i in range(0,vectorPt.size()):

            if vectorPt.at(i)<PtMin:
			continue

            if vectorPt.at(i)>PtMax:
                  continue

            if abs(vectorEta.at(i))<EtaMin:
                  continue

            if abs(vectorEta.at(i))>EtaMax:
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

	    # Check Qual:  
            qual98=True
            qual95=True
            qual90=True
            qual85=True

            if vectorIdLUTPt.at(i)==0:
                binEta=vectorIdLUTEta.at(i)
                if vectorIdLUTQuality.at(i)< thresholdQual98[binEta]:
                        qual98=False
                if vectorIdLUTQuality.at(i)< thresholdQual95[binEta]:
                        qual95=False
                if vectorIdLUTQuality.at(i)< thresholdQual90[binEta]:
                        qual90=False
                if vectorIdLUTQuality.at(i)< thresholdQual85[binEta]:
                        qual85=False

            muonQuality.Fill(vectorQual.at(i))
            muonPt.Fill(vectorPt.at(i))
            muonEta.Fill(vectorEta.at(i))
            muonNStubs.Fill(vectorNStubs.at(i))

            if notFilled==True:
		leadPt.Fill(vectorPt.at(i))
	
		if vectorQual.at(i)>0:
	                leadPtDefHWQ.Fill(vectorPt.at(i))
	
		if qual98==True: 
			leadPtQ98.Fill(vectorPt.at(i))
                if qual95==True: 
                        leadPtQ95.Fill(vectorPt.at(i))
                if qual90==True: 
                        leadPtQ90.Fill(vectorPt.at(i))
                if qual85==True: 
                        leadPtQ85.Fill(vectorPt.at(i))

		if vectorIdLUTPt.at(i)==0:
			leadEtaBin.Fill(vectorIdLUTEta.at(i))

	                if vectorQual.at(i)>0:
         	               leadEtaBinDefHWQ.Fill(vectorIdLUTEta.at(i))

			if qual98==True:
                        	leadEtaBinQ98.Fill(vectorIdLUTEta.at(i))
                	if qual95==True:
                        	leadEtaBinQ95.Fill(vectorIdLUTEta.at(i))
                	if qual90==True:
                        	leadEtaBinQ90.Fill(vectorIdLUTEta.at(i))
                	if qual85==True:
                        	leadEtaBinQ85.Fill(vectorIdLUTEta.at(i))



		notFilled=False	

totalrate=31038.0/entries

def doRate(histo,name):
        historate=histo.Clone()
        historate.SetName(name)
        for i in range(0,historate.GetNbinsX()):
                integral=historate.Integral(i,-1)
                historate.SetBinContent(i,integral)
        historate.Scale(totalrate)
        return historate

rate=doRate(leadPt,"All")
rateQ98=doRate(leadPtQ98,"Q98")
rateQ95=doRate(leadPtQ95,"Q95")
rateQ90=doRate(leadPtQ90,"Q90")
rateQ85=doRate(leadPtQ85,"Q85")
rateDefHWQ=doRate(leadPtDefHWQ,"All")

leadEtaBin.Scale(totalrate)
leadEtaBinQ98.Scale(totalrate)
leadEtaBinQ95.Scale(totalrate)
leadEtaBinQ90.Scale(totalrate)
leadEtaBinQ85.Scale(totalrate)
leadEtaBinDefHWQ.Scale(totalrate)

leadPt.Scale(totalrate)
leadPtDefHWQ.Scale(totalrate)
leadPtQ98.Scale(totalrate)
leadPtQ95.Scale(totalrate)
leadPtQ90.Scale(totalrate)
leadPtQ85.Scale(totalrate)


out=TFile("checks_"+filename+".root","RECREATE")
out.cd()

muonQuality.Write()
muonPt.Write()
muonEta.Write()
muonNStubs.Write()

leadPt.Write()
leadPtQ98.Write()
leadPtQ95.Write()
leadPtQ90.Write()
leadPtQ85.Write()

leadPtDefHWQ.Write()

leadEtaBin.Write()
leadEtaBinQ98.Write()
leadEtaBinQ95.Write()
leadEtaBinQ90.Write()
leadEtaBinQ85.Write()



rate.Write()
rateDefHWQ.Write()
rateQ98.Write()
rateQ95.Write()
rateQ90.Write()
rateQ85.Write()

