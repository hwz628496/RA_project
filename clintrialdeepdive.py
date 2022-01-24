# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:25:49 2021

@author: hwz62
"""
import pandas as pd
from helpers import loadClinData
from harvard import harvard
from clintrialMRN import actharMRN, rawlusMRN, tociMRN, tofaMRN
from harvard import countDXICD
from sklearn.metrics import confusion_matrix

demographics, demo2, diagnoses, diag2 = loadClinData() #demo2, diag2 have mrn as index

harvardActhar = []
for i in actharMRN:
    try:
        harvardActhar.append(harvard(i,demographics,diagnoses))
    except:
        harvardActhar.append(i)


harvardActharDf = pd.DataFrame({'mrn': actharMRN,'harvard': harvardActhar})
harvardActharDf = harvardActharDf.drop(harvardActharDf[harvardActharDf.harvard > 2].index)
droppedMRN=list(harvardActharDf.mrn)
trueActharRA = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
HarActharYN = [int(i>0.632) for i in list(harvardActharDf.harvard)]

dfActhar = pd.DataFrame({'mrn': droppedMRN,'harvard': list(harvardActharDf.harvard), 'ra': trueActharRA, 'harvard cutoff': HarActharYN})
ActharAgree = [HarActharYN[i]==trueActharRA[i] for i in range(len(trueActharRA))]
sum(ActharAgree)/len(ActharAgree)
ActharConfusion = confusion_matrix(trueActharRA, HarActharYN)

# check if DX count are valid
counts=[]
for i in droppedMRN:
    counts.append(countDXICD(i, diagnoses))
    
#rawlus 
harvardRawlus = []
for i in rawlusMRN:
    try:
        harvardRawlus.append(harvard(int(i),demographics,diagnoses))
    except:
        harvardRawlus.append(int(i))


harvardRawlusDf = pd.DataFrame({'mrn': rawlusMRN,'harvard': harvardRawlus})
harvardRawlusDf = harvardRawlusDf.drop(harvardRawlusDf[harvardRawlusDf.harvard > 2].index)
droppedMRN=list(harvardRawlusDf.mrn)
trueRawlusRA = [1]*len(droppedMRN)
HarRawlusYN = [int(i>0.632) for i in list(harvardRawlusDf.harvard)]

dfRawlus = pd.DataFrame({'mrn': droppedMRN,'harvard': list(harvardRawlusDf.harvard), 'ra': trueRawlusRA, 'harvard cutoff': HarRawlusYN})
RawlusAgree = [HarRawlusYN[i]==trueRawlusRA[i] for i in range(len(HarRawlusYN))]
sum(RawlusAgree)/len(RawlusAgree)
RawlusConfusion = confusion_matrix(trueRawlusRA, HarRawlusYN)

#toci 
harvardToci = []
for i in tociMRN:
    try:
        harvardToci.append(harvard(int(i),demographics,diagnoses))
    except:
        harvardToci.append(int(i))

harvardTociDf = pd.DataFrame({'mrn': tociMRN,'harvard': harvardToci})
harvardTociDf = harvardTociDf.drop(harvardTociDf[harvardTociDf.harvard > 2].index)
droppedMRN=list(harvardTociDf.mrn)
trueTociRA = [1]*len(droppedMRN)
HarTociYN = [int(i>0.632) for i in list(harvardTociDf.harvard)]

dfToci = pd.DataFrame({'mrn': droppedMRN,'harvard': list(harvardTociDf.harvard), 'ra': trueTociRA, 'harvard cutoff': HarTociYN})
TociAgree = [HarTociYN[i]==trueTociRA[i] for i in range(len(HarTociYN))]
sum(TociAgree)/len(TociAgree)
TociConfusion = confusion_matrix(trueTociRA, HarTociYN)

#tofa 
harvardTofa = []
for i in tofaMRN:
    try:
        harvardTofa.append(harvard(int(i),demographics,diagnoses))
    except:
        harvardTofa.append(int(i))

harvardTofaDf = pd.DataFrame({'mrn': tofaMRN,'harvard': harvardTofa})
harvardTofaDf = harvardTofaDf.drop(harvardTofaDf[harvardTofaDf.harvard > 2].index)
droppedMRN=list(harvardTofaDf.mrn)
trueTofaRA = [1]*len(droppedMRN)
HarTofaYN = [int(i>0.632) for i in list(harvardTofaDf.harvard)]

dfTofa = pd.DataFrame({'mrn': droppedMRN,'harvard': list(harvardTofaDf.harvard), 'ra': trueTofaRA, 'harvard cutoff': HarTofaYN})
TofaAgree = [HarTofaYN[i]==trueTofaRA[i] for i in range(len(HarTofaYN))]
sum(TofaAgree)/len(TofaAgree)
TofaConfusion = confusion_matrix(trueTofaRA, HarTofaYN)
