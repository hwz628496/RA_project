# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:04:32 2021

@author: hwz62
"""

import pandas as pd
from harvard import harvard
from harvard import countDXICD
from sklearn.metrics import confusion_matrix

#baseline data from redcap
casesDemographics = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\demographics2.csv')
casesDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
controlDemographics = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')
controlDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_DX.txt', sep='|', header=0)
casesDemographics = casesDemographics[casesDemographics['RA_ENC_CNT'].notna()]
undesiredColumns = ['CONDITION', 'SEX_1', 'RACE_1', 'ETHNICITY_1']
controlDemographics2 = controlDemographics.drop(undesiredColumns, axis=1)
demographics = pd.concat([casesDemographics, controlDemographics2])
demo2 = demographics.set_index('MRN')
diagnoses = pd.concat([casesDiagnoses, controlDiagnoses])
diag2 = diagnoses.set_index('MRN')

#import 3200 MRN
mrn3200 = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\3200MRN\\veena_mrn_list.csv')
mrn3200 = mrn3200.set_index('mrn', drop=False)
mrn3200mrn = mrn3200.mrn
mrn3200mrn = list(set(mrn3200mrn))

#calculate harvard scores
harvard3200 = []
for i in mrn3200mrn:
    try:
        harvard3200.append(harvard(i,demographics,diagnoses))
    except:
        harvard3200.append(i)

harvard3200 = pd.DataFrame({'mrn': mrn3200mrn,'harvard': harvard3200})
harvard3200 = harvard3200.drop(harvard3200[harvard3200.harvard > 2].index)

#build master df
droppedHarvard=list(harvard3200.harvard)
droppedMRN=list(harvard3200.mrn)
droppedRA=[mrn3200.loc[i].ra for i in droppedMRN]
droppedHarYN=[int(i>0.632) for i in droppedHarvard]

df = pd.DataFrame({'mrn': droppedMRN,'harvard': droppedHarvard, 'ra': droppedRA, 'harvard cutoff': droppedHarYN})

#check for agreement - 2081 out of 3147 agree
agreement = [df.iloc[i].ra==df.iloc[i]['harvard cutoff'] for i in range(3147)]
agreement[56]=False
agreement[226]=False
agreement[711]=False
agreement[747]=False
agreement[831]=False
agreement[1195]=False
agreement[1258]=False
agreement[1557]=False
agreement[1898]=False
agreement[2120]=False
agreement[2653]=False
agreement[2702]=True
agreement[2990]=False
agreement[3015]=False

#check out MRN 2519694, 5013039, 4758215, 4587115, 3400307

#check counts

counts=[]
for i in droppedMRN:
    counts.append(countDXICD(i, diagnoses))

#confusion3200 = confusion_matrix(droppedRA, droppedHarYN)
