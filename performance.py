# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:28:13 2021

@author: hwz62
"""

import pandas as pd
from amia300List import totallist2 as totallist
from amia300List import list1, list2
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
from sklearn.metrics import cohen_kappa_score


cliniciansFilename = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\Final Data\\All Results.xlsx'
clinicians = pd.read_excel(cliniciansFilename, engine='openpyxl')
clinicians = clinicians.set_index('mrn')

lucasFilename = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\Final Data\\Lucas Results.xlsx'
lucas = pd.read_excel(lucasFilename, usecols='B:H', engine='openpyxl')
lucas = lucas.set_index('mrn')

IAA = [x for x in list1 if x in list2]
individualCases = [x for x in totallist if x not in IAA]

individualClinicians = clinicians.loc[individualCases]
individualLucas = lucas.loc[individualCases]

compare = [individualClinicians.harvard, individualClinicians.reviewer, individualLucas.lucas]
compareDf = pd.DataFrame(compare)
compareDf = compareDf.transpose()

# 1 is harvard, 2 is reviewer, 3 is lucas
pd.crosstab(compareDf.harvard, compareDf.reviewer)
pd.crosstab(compareDf.harvard, compareDf.lucas)
pd.crosstab(compareDf.reviewer, compareDf.lucas)

precision_recall_fscore_support(compareDf.reviewer, compareDf.lucas)


# psoriasis and SLE

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

psoriasisICD9 = 696
psoriasisICD10 = ['L40.54', 'M07.0', 'M07.3']
SLEICD9 = [710.0, 695.4]
SLEICD10 = ['M32.14', 'M32.13', 'L93', 'M32.8', 'L93.2', 'M32.19', 'M32.12', 'M32.10', 'M32', 'M32.9', 'M32.1', 'M32.1', 'M35.1']