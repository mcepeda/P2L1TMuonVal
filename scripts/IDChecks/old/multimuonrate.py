#!/usr/bin/env python
import math
from ROOT import *

filename="MB_GMTIso_ID"

f = TFile('/nfs/cms/cepeda/trigger/'+filename+'.root',"READONLY")
tree = f.Get("gmtTkMuonChecksTree/L1PhaseIITree")
tree.AddFriend("genTree/L1GenTree",f)

gStyle.SetOptStat(0)

print ("Got the tree!")

entries= tree.GetEntries()

print (entries)

branch="gmtTkMuon"

suffix="Qual_All"

minPt=5
maxEta=2.5

nQuals=5

thresholdQual=[ [0]*13  ]*nQuals

thresholdQual[0]=[0]*13

# 98%
thresholdQual[1]=[53,31,33,32,32,32,32,32,32,49,32,38,33]
# 95%
thresholdQual[2]=[59,33,53,40,47,60,58,58,53,64,41,49,38]
# 90%
thresholdQual[3]=[75,51,60,61,61,91,124,123,88,93,65,75,44]
# 95%
thresholdQual[4]=[87,60,64,63,63,95,153,156,97,104,95,95,51]

labels=["NoCut","WP98","WP95","WP90","WP85"]

filename=filename+suffix

eventNo=0

count_TripleMu_4_2_2 =[0]*nQuals
count_SingleMu_20 = [0]*nQuals 
count_DoubleMu_13p5_6=[0]*nQuals


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


count5=[0]*nQuals

leadPt={}
secondPt={}
thirdPt={}


for q in range(0,nQuals):
   leadPt[q]=formatHisto("leadPt_"+labels[q],"leadPt",100,0,100)
   secondPt[q]=formatHisto("secondPt_"+labels[q],"secondPt",100,0,100)
   thirdPt[q]=formatHisto("thirdPt_"+labels[q],"thirdPt",100,0,100)




for event in tree:
        if eventNo>entries:
                break
        if eventNo%100000 == 0:
                        print ("....%d" %eventNo)

        eventNo+=1

        vectorPt=getattr(event, branch+"Pt")
        vectorEta=getattr(event, branch+"Eta")
        vectorNStubs=getattr(event, branch+"NStubs")
        vectorIdLUTEta=getattr(event, branch+"IdLUTEta")
        vectorIdLUTPt=getattr(event, branch+"IdLUTPt")
        vectorIdLUTQuality=getattr(event, branch+"IdLUTQuality")
        vectorZ0=getattr(event, branch+"Z0")

        notFilled=[True]*nQuals
        notFilled2=[True]*nQuals
        notFilled3=[True]*nQuals

        single=[False]*nQuals
	double=[False]*nQuals
	triple=[False]*nQuals


        for i in range(0,vectorPt.size()):

	    # Check Qual:  
            qual=[True]*nQuals		
	    binEta=vectorIdLUTEta.at(i)

	    if abs(vectorEta.at(i)>maxEta):
                continue

            for q in range(0,nQuals):
	       if vectorIdLUTPt.at(i)==0:
		  if vectorIdLUTQuality.at(i) < thresholdQual[q][binEta]:
			qual[q]=False

               leadZ0=-20	
               if notFilled[q]==True:	
		  if qual[q]==True:
		    if vectorPt.at(i)>minPt:
				count5[q]+=1
		    leadPt[q].Fill(vectorPt.at(i))
                    leadZ0=vectorZ0.at(i)	
		    if vectorPt.at(i)>20:
			single[q]=True
                    if vectorPt.at(i)>13.5:
			double[q]=True
		    if vectorPt.at(i)>4:
		        triple[q]=True
		  notFilled[q]=False	

               elif notFilled2[q]==True:
		  if qual[q]==True:
                    secondPt[q].Fill(vectorPt.at(i))
                  if qual[q]==False or vectorPt.at(i) <6 :
			  double[q]=False
                  if qual[q]==False or vectorPt.at(i) <2 :
                          triple[q]=False
                  if abs(leadZ0-vectorZ0.at(i))>1:
                          double[q]=False
                          triple[q]=False
                  notFilled2[q]=False

               elif notFilled3[q]==True:
		  if qual[q]==True:
                    thirdPt[q].Fill(vectorPt.at(i))
                  if qual[q]==False or vectorPt.at(i) <2 :
                          triple[q]=False           
                  if abs(leadZ0-vectorZ0.at(i))>1:
                          triple[q]=False 
                  notFilled3[q]=False
        for q in range(0,nQuals):
		if single[q]:
			count_SingleMu_20[q]+=1
                if double[q]:
                        count_DoubleMu_13p5_6[q]+=1
                if triple[q]:
                        count_TripleMu_4_2_2[q]+=1        


totalrate=31038.0/entries

for q in range(0,nQuals):
	print (labels[q],count_SingleMu_20[q]*totalrate,count_DoubleMu_13p5_6[q]*totalrate,count_TripleMu_4_2_2[q]*totalrate)



rate={}
rate2={}
rate3={}

def doRate(histo,name):
        historate=histo.Clone()
        historate.SetName(name)
        for i in range(0,historate.GetNbinsX()):
                integral=historate.Integral(i+1,-1)
                historate.SetBinContent(i,integral)
        historate.Scale(totalrate)
        return historate

for q in range(0,nQuals):
	rate[q]=doRate(leadPt[q],labels[q])
	rate2[q]=doRate(secondPt[q],labels[q]+"_Double")
        rate3[q]=doRate(thirdPt[q],labels[q]+"_Triple")

out=TFile("checks_ratesMulti_"+filename+".root","RECREATE")
out.cd()

for q in range(0,nQuals):
	leadPt[q].Write()
	rate[q].Write()
        secondPt[q].Write()
        rate2[q].Write()
        thirdPt[q].Write()
        rate3[q].Write()
