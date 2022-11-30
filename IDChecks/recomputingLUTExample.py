# TO BE CLEANED 

#!/usr/bin/env python 
from ROOT import *

import tdrstyle
import math

#set the tdr style
tdrstyle.setTDRStyle()

fMB = TFile( 'checks_MB_GMTIso_ID.root') 
fDoubleMuGun = TFile('checks_DoubleMu_GMTIso_ID.root') 

constant_lt_tpsID =[ 40, 56, 64, 88, 64, 32, 60, 56, 56, 56,  56,  56,  56,  56,  56, 56, 28, 56,  56, 54,  36,  36,  36, 36, 36, 36, 36, 36, 32, 28, 28, 28, 28, 52, 56, 52,  52,  56,  56,  56,  56, 56, 56, 56,  56, 56,  56,  56,  28, 56, 52, 52,  56, 56, 56, 56, 56, 56, 56, 56, 56, 56,  56,  56,  28,  52,  36, 36, 36, 36,  36, 36,  36,  36,  56, 56, 36, 56, 36, 36, 28, 60, 60, 60, 56, 56, 56, 56,  56,  56,  56,  56,  56, 56, 56, 56,  28, 120, 120, 120, 92, 92, 64, 64,  64, 64, 64, 64, 64, 64, 64, 64, 28, 120, 152, 128, 100, 124, 80, 80, 64, 100, 64,
64,  64,  64,  64, 64, 28, 88, 92, 64, 92, 60, 60, 60, 92, 60, 60, 60,  60,  60,  60,  60,
36, 88, 88, 64,  64,60,  60,  60,  60, 60, 60, 60, 92, 92, 92, 92, 28, 88, 88, 88, 88, 88,
88,  88,  88,  88,  88, 88, 88, 88,  88,88,  28,  92,  92, 92, 92, 92,      92, 92, 92,
92, 92, 92, 92, 92, 92, 92,  28,  92,  92,  92,  92, 92, 92, 92,  92, 92,  92,  92,  92,
92, 92, 92,      64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  64,  64,  64,  64,  64, 64, 64,
64,  64, 64,  64,  64,  64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64,  64,  64,
64,  64,  64, 64, 64, 64,  64, 64,  64,  64]


lt_tpsID_98=[0] * 256
lt_tpsID_95=[0] * 256
lt_tpsID_90=[0] * 256
lt_tpsID_85=[0] * 256

bg_lt_tpsID_98=[0] * 256
bg_lt_tpsID_95=[0] * 256
bg_lt_tpsID_90=[0] * 256
bg_lt_tpsID_85=[0] * 256

err_bg_lt_tpsID_98=[0] * 256
err_bg_lt_tpsID_95=[0] * 256
err_bg_lt_tpsID_90=[0] * 256
err_bg_lt_tpsID_85=[0] * 256



def plotHistosStubs(fileMB,fileDoubleMuGun,name,xtitle, maxY=1,logY=False, BIN=0):
	c=TCanvas("c"+name)
	if logY==True:
	        c.SetLogy()

	print (BIN)

        histo=fileDoubleMuGun.Get(name)
        histo.SetLineColor(kBlue)
        histo.SetMarkerColor(kBlue)
        histo.SetMarkerStyle(3)
	histo.SetLineWidth(3)

        histo2=fileMB.Get(name)
        histo2.SetLineColor(kRed)
        histo2.SetMarkerColor(kRed)
        histo2.SetMarkerStyle(34)
        histo2.SetLineWidth(3)

	histo.SetXTitle(xtitle)
        histo.SetYTitle("Fraction passing threshold")
        histo.GetYaxis().SetTitleOffset(1.6)
        histo.GetXaxis().SetTitleOffset(1.6)

	histo.Sumw2()
	histo2.Sumw2()

	errInt=Double(0)
	errInt2=Double(0)
	Int=histo.IntegralAndError(-1,-1,errInt)
        Int2=histo2.IntegralAndError(-1,-1,errInt2)

        xvalueForE98=0
        bgvalueForE98=0
        errbgvalueForE98=0

	xvalueForE95=0
	bgvalueForE95=0
        errbgvalueForE95=0

        xvalueForE90=0
        bgvalueForE90=0
        errbgvalueForE90=0

        xvalueForE85=0
        bgvalueForE85=0
        errbgvalueForE85=0

        value_default=constant_lt_tpsID[BIN]

	evalueForDef=0
        bgvalueForDef=0


	for i in range(0,histo.GetXaxis().GetNbins()):
	        if Int!=0:  
			errInti=Double(0)
			Inti=histo.IntegralAndError(i,-1,errInti)
			frac=0
			errfrac=0
			if Inti!=0: 
				frac=Inti/Int
				errfrac=frac*math.sqrt( (errInti/Inti)*(errInti/Inti) + (errInt/Int)*(errInt/Int))

			histo.SetBinContent(i,frac)
			histo.SetBinError(i,errfrac)
		
                        if xvalueForE98==0 and frac<0.98:
                                xvalueForE98=i
			if xvalueForE95==0 and frac<0.95:
				xvalueForE95=i
			if xvalueForE90==0 and frac<0.90:
                                xvalueForE90=i
                        if xvalueForE85==0 and frac<0.85:
                                xvalueForE85=i
			if i==value_default:
				evalueForDef=frac

	

		if Int2!=0:
                        errInt2i=Double(0)
                        Int2i=histo2.IntegralAndError(i,-1,errInt2i)
			frac2=0
                        errfrac2=0
			if Int2i!=0:
	                        frac2=Int2i/Int2
        	                errfrac2=frac2*math.sqrt( (errInt2i/Int2i)*(errInt2i/Int2i)+(errInt2/Int2)*(errInt2/Int2))
                        histo2.SetBinContent(i,frac2)
                        histo2.SetBinError(i,errfrac2)
		
                        if i==xvalueForE98:
                                bgvalueForE98=frac2
                                errbgvalueForE98=errfrac2
	
			if i==xvalueForE95: 
				bgvalueForE95=frac2
                                errbgvalueForE95=errfrac2

                        if i==xvalueForE90:
                                bgvalueForE90=frac2
                                errbgvalueForE90=errfrac2

                        if i==xvalueForE85:
                                bgvalueForE85=frac2
                                errbgvalueForE85=errfrac2

                        if i==value_default:
                                bgvalueForDef=frac2



	histo.GetYaxis().SetRangeUser(0,1.05)

	print ("DEFAULT:", value_default, " E:",evalueForDef, " BG?:",bgvalueForDef)
        print ("0.95 :",xvalueForE95," BG?:",bgvalueForE95)
        print ("0.90 :",xvalueForE90," BG?:",bgvalueForE90)

        lt_tpsID_98[BIN]=xvalueForE98
        bg_lt_tpsID_98[BIN]=bgvalueForE98
        err_bg_lt_tpsID_98[BIN]=errbgvalueForE98

	lt_tpsID_95[BIN]=xvalueForE95
	bg_lt_tpsID_95[BIN]=bgvalueForE95
        err_bg_lt_tpsID_95[BIN]=errbgvalueForE95

        lt_tpsID_90[BIN]=xvalueForE90
        bg_lt_tpsID_90[BIN]=bgvalueForE90
        err_bg_lt_tpsID_90[BIN]=errbgvalueForE90

        lt_tpsID_85[BIN]=xvalueForE85
        bg_lt_tpsID_85[BIN]=bgvalueForE85
        err_bg_lt_tpsID_85[BIN]=errbgvalueForE85


	histo.Draw("hist")
        histo2.Draw("sames,hist")

	line=TLine(value_default,0,value_default,1.05)
	line.SetLineColor(kGray+2)
        line.SetLineWidth(2+2)
	line.Draw()

        line95=TLine(xvalueForE95,0,xvalueForE95,0.95)
        line95.SetLineColor(kGray+1)
        line95.SetLineStyle(kDashed)
        line95.SetLineWidth(2)
        line95.Draw()

        line90=TLine(xvalueForE90,0,xvalueForE90,0.90)
        line90.SetLineColor(kGray+2)
        line90.SetLineStyle(kDotted)
        line90.SetLineWidth(2)
        line90.Draw()

        line95h=TLine(0,0.95,xvalueForE95,0.95)
        line95h.SetLineColor(kGray+1)
        line95h.SetLineStyle(kDashed)
        line95h.SetLineWidth(2)
        line95h.Draw()


        line90h=TLine(0,0.90,xvalueForE90,0.90)
        line90h.SetLineColor(kGray+2)
        line90h.SetLineStyle(kDotted)
        line90h.SetLineWidth(2)
        line90h.Draw()




#	leg =TLegend(0.5,0.95,0.9,0.60,"","brNDC");
#	leg.SetFillStyle(0)
#	leg.SetBorderSize(0)
#        entry=leg.AddEntry(histo,"DoubleMuGun","l");
#	entry=leg.AddEntry(histo2,"Min Bias","l");
#	leg.Draw()

	c.SaveAs("Bines/FRAC_MBvsDoubleMu_"+name+".png")

for ptBin in range(0,3):
   for etaBin in range(0,13):
		BINLUT= ptBin | (etaBin<<4)
                print (ptBin, etaBin, BINLUT)
		plotHistosStubs(fMB,fDoubleMuGun,"muonQuality_"+str(ptBin)+"_"+str(etaBin),"Quality PT:"+str(ptBin)+", ETA:"+str(etaBin),0.4, False,BINLUT)
#                plotHistosStubs(fMB,fDoubleMuGun,"muonNStubs_"+str(ptBin)+"_"+str(etaBin),"NStubs PT:"+str(ptBin)+", ETA:"+str(etaBin),0.4, BINLUT)


#  KEY: TH1F	muonQuality_15_13;1	muonQuality
#  KEY: TH1F	muonPtBin_15_13;1	muonPtBin
#  KEY: TH1F	muonEtaBin_15_13;1	muonEtaBin
#  KEY: TH1F	muonNStubs_15_13;1	muon NStubs

import numpy as np
np.set_printoptions(suppress=True)
np.set_printoptions(precision=2)

print ("LUT98=",lt_tpsID_98)
print ("BGLUT98= %4.2f",np.array(bg_lt_tpsID_98))
print ("ERRBGLUT98=",np.array(err_bg_lt_tpsID_98))

print ("LUT95=",lt_tpsID_95)
print ("BGLUT95=",np.array(bg_lt_tpsID_95))
print ("ERRBGLUT95=",np.array(err_bg_lt_tpsID_95))

print ("LUT90=",lt_tpsID_90)
print ("BGLUT90=",np.array(bg_lt_tpsID_90))
print ("ERRBGLUT90=",np.array(err_bg_lt_tpsID_90))

print ("LUT85=",lt_tpsID_85)
print ("BGLUT85=",np.array(bg_lt_tpsID_85))
print ("ERRBGLUT85=",np.array(err_bg_lt_tpsID_85))


for ptBin in range(0,3):
	bg98OnlyOnePtBin=[0]*13
	errbg98OnlyOnePtBin=[0]*13
	bg95OnlyOnePtBin=[0]*13
	errbg95OnlyOnePtBin=[0]*13
	bg90OnlyOnePtBin=[0]*13
	errbg90OnlyOnePtBin=[0]*13
	bg85OnlyOnePtBin=[0]*13
	errbg85OnlyOnePtBin=[0]*13
	
	for etaBin in range(0,13):
		BINLUT= ptBin | (etaBin<<4)
		bg98OnlyOnePtBin[etaBin]= bg_lt_tpsID_98[BINLUT]
	        errbg98OnlyOnePtBin[etaBin]= err_bg_lt_tpsID_98[BINLUT]
	        bg95OnlyOnePtBin[etaBin]= bg_lt_tpsID_95[BINLUT]
	        errbg95OnlyOnePtBin[etaBin]= err_bg_lt_tpsID_95[BINLUT]
	        bg90OnlyOnePtBin[etaBin]= bg_lt_tpsID_90[BINLUT]
	        errbg90OnlyOnePtBin[etaBin]= err_bg_lt_tpsID_90[BINLUT]
	        bg85OnlyOnePtBin[etaBin]= bg_lt_tpsID_85[BINLUT]
	        errbg85OnlyOnePtBin[etaBin]= err_bg_lt_tpsID_85[BINLUT]
		
		if ptBin==0:
			print ("%d %d %0.2f %d %0.2f %d %0.2f %d %0.2f \n" %(etaBin,lt_tpsID_98[BINLUT],bg_lt_tpsID_98[BINLUT],lt_tpsID_95[BINLUT],bg_lt_tpsID_95[BINLUT],lt_tpsID_90[BINLUT],bg_lt_tpsID_90[BINLUT],lt_tpsID_85[BINLUT],bg_lt_tpsID_85[BINLUT]))

	
	from array import array
	order = array( 'f', range(0,13))
	zeros = array( 'f', [0]*13 )
	y98  = array( 'f', bg98OnlyOnePtBin)
	ey98 = array( 'f', errbg98OnlyOnePtBin)
	y95  = array( 'f', bg95OnlyOnePtBin)
	ey95 = array( 'f', errbg95OnlyOnePtBin)
	y85  = array( 'f', bg85OnlyOnePtBin)
	ey85 = array( 'f', errbg85OnlyOnePtBin)
	y90  = array( 'f', bg90OnlyOnePtBin)
	ey90 = array( 'f', errbg90OnlyOnePtBin)
	
	
	gr98=TGraphErrors(13,order,y98,zeros,ey98)
	gr95=TGraphErrors(13,order,y95,zeros,ey95)
	gr85=TGraphErrors(13,order,y85,zeros,ey85)
	gr90=TGraphErrors(13,order,y90,zeros,ey90)
	
	gr98.SetLineColor(kBlack)
	gr98.SetMarkerColor(kBlack)
	gr98.SetMarkerStyle(20)
	
	gr95.SetLineColor(kBlue)
	gr95.SetMarkerColor(kBlue)
	gr95.SetMarkerStyle(21)
	
	gr90.SetLineColor(kRed)
	gr90.SetMarkerColor(kRed)
	gr90.SetMarkerStyle(22)
	
	gr85.SetLineColor(kGreen+2)
	gr85.SetMarkerColor(kGreen+2)
	gr85.SetMarkerStyle(23)
	
	mg=TMultiGraph()
	mg.Add(gr98)
	mg.Add(gr95)
	mg.Add(gr90)
	mg.Add(gr85)
	mg.SetTitle("Bg rejection for fixed efficiency; BIN ETA (PTBIN="+str(ptBin)+"); Bg Rejection")
	mg.SetMaximum(1.1)
	c3=TCanvas("c3")
	c3.cd()
	mg.Draw("ALPE")
	
	
	leg =TLegend(0.2,0.95,0.5,0.70,"","brNDC");
	leg.SetFillStyle(0)
	leg.SetBorderSize(0)
	entry=leg.AddEntry(gr98,"98% eff","lp");
	entry=leg.AddEntry(gr95,"95% eff","lp");
	entry=leg.AddEntry(gr90,"90% eff","lp");
	entry=leg.AddEntry(gr85,"85% eff","lp");
	leg.Draw()
	
	c3.SaveAs("BgRejection_PTBIN"+str(ptBin)+".png")
	
	
