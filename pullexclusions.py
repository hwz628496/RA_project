# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:28:24 2020

@author: hwz62
"""

import pandas as pd
import numpy as np
from exclusionICD import excexact, excstartswith

diagnoses = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
demographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')

# pulls only those with RA
demographics = demographics[demographics['RA_ENC_CNT'].notna()]

# Pull exclusion MRNs
mrnExcList=[]
for exactICD in excexact:
    mrnFull=diagnoses[diagnoses.ICD_CODE==exactICD].MRN
    mrnExactSet=list(set(mrnFull))
    [mrnExcList.append(mrn) for mrn in mrnExactSet]
startsMrnList=[]
for startswithICD in excstartswith:
    for s in diagnoses.ICD_CODE:
        if s.startswith(startswithICD)==True:
            startsMrnList.append(s)
        else:
            continue
    mrnStartSet=list(set(startsMrnList))
    [mrnExcList.append(mrn) for mrn in mrnStartSet]
totalMRN=demographics.MRN
mrnExcList2=list(set(totalMRN)&set(mrnExcList))

