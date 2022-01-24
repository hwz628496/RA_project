# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:48:56 2021

@author: hwz62
"""
import pandas as pd
from amia300List import cases, controls

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
#demographics=allDemographics.set_index('MRN')
diagnoses = pd.concat([casesDiagnoses, controlDiagnoses])
cliniciansFilename = 'C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\amia300\\Final Data\\All Results.xlsx'
clinicians = pd.read_excel(cliniciansFilename, engine='openpyxl')
clinicians = clinicians.set_index('mrn')

#look for missing data from clinicians' reviews
cliniciansDataFilename = 'C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\amia300\\RAIdentification-300AllReviews_DATA_2021-03-23_0849.csv'
cliniciansData = pd.read_csv(cliniciansDataFilename)

#needed columns from clinicians' review
acrCol = ['mrn', 'joint_involvement', 'serology', 'apr_score', 'sdd_score', 'scores', 'acr2010missing', 'comments_2010']
acrVal = cliniciansData[acrCol]

#missing data per column
jointMissing = acrVal['joint_involvement'].isna().sum() #210
serologyMissing = acrVal['serology'].isna().sum() #206
acutePhaseMissing = acrVal['apr_score'].isna().sum() #138
durationMissing = acrVal['sdd_score'].isna().sum() #221
sum(acrVal['joint_involvement'].isna()&acrVal['serology'].isna()&acrVal['apr_score'].isna()&acrVal['sdd_score'].isna())
#114 patient with all missing data

#all missing characteristics
missingMRN=acrVal[acrVal['joint_involvement'].isna()&acrVal['serology'].isna()&acrVal['apr_score'].isna()&acrVal['sdd_score'].isna()].mrn
missingMRN = list(set(list(missingMRN)))
caseMissing=[]
ctrlMissing=[]
for i in missingMRN:
    if i in cases:
        caseMissing.append(i)
    elif i in controls:
        ctrlMissing.append(i)
    else:
        print(i)

missingData=acrVal[acrVal['joint_involvement'].isna()&acrVal['serology'].isna()&acrVal['apr_score'].isna()&acrVal['sdd_score'].isna()]


