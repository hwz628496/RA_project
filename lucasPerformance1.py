# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:25:29 2021

@author: hwz62
"""

import pandas as pd
from helpers import harvard
from amia300List import totallist2 as totallist
from amia300List import cases, controls
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

casesDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')
casesDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
controlDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')
controlDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_DX.txt', sep='|', header=0)


casesDemographics = casesDemographics[casesDemographics['RA_ENC_CNT'].notna()]
undesiredColumns = ['CONDITION', 'SEX_1', 'RACE_1', 'ETHNICITY_1']
controlDemographics2 = controlDemographics.drop(undesiredColumns, axis=1)
allDemographics = pd.concat([casesDemographics, controlDemographics2])
allDemographics2=allDemographics.set_index('MRN')
allDiagnoses = pd.concat([casesDiagnoses, controlDiagnoses])


lucasAll = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-Ranganath_DATA_2021-03-02_1744.csv')

lucasMRN = list(lucasAll.mrn)
completedMRN = [x for x in lucasMRN if x in totallist]
completedMRN = list(set(completedMRN))
lucasAnswers=[list(lucasAll[lucasAll.mrn==i].ra)[0] for i in completedMRN]
lucasRecordID=[list(lucasAll[lucasAll.mrn==i].record_id)[0] for i in completedMRN]

henryAnswers = []
for i in completedMRN:
    if i in cases:
        henryAnswers.append(1)
    elif i in controls:
        henryAnswers.append(2)
    else:
        print('MRN not found at %d', i)
        break

diagnoses = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
demographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')
harvardRaw = [harvard(mrn, allDemographics, allDiagnoses) for mrn in completedMRN]
harvardAnswers = []
for i in harvardRaw:
    if i < 0.632:
        harvardAnswers.append(2)
    else:
        harvardAnswers.append(1)

allResults = pd.DataFrame([completedMRN, henryAnswers, lucasAnswers, harvardAnswers])
allResults = allResults.transpose()

allResults2 = pd.DataFrame([completedMRN, lucasRecordID, henryAnswers, lucasAnswers, harvardAnswers, harvardRaw])
allResults2 = allResults2.transpose()
allResults2.columns = ['mrn', 'record_id', 'henry', 'veena', 'harvard', 'harvardscore']

pd.crosstab(allResults[1], allResults[2])
pd.crosstab(allResults[1], allResults[3])
pd.crosstab(allResults[3], allResults[2])

# all agree
sum([(henryAnswers[i]==1 and harvardAnswers[i]==1) and (henryAnswers[i]==1 and lucasAnswers[i]==1) for i in range(len(henryAnswers))])
sum([(henryAnswers[i]==2 and harvardAnswers[i]==2) and (henryAnswers[i]==2 and lucasAnswers[i]==2) for i in range(len(henryAnswers))])

precision_recall_fscore_support(allResults[3],allResults[2])

