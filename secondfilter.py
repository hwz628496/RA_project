# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:47:49 2021

@author: hwz62
"""

import pandas as pd
import numpy as np
from helpers import harvard
from amia300List import noIAA
from sklearn import tree
from sklearn.model_selection import cross_val_score

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
gold = clinicians.reviewer

#harvardValues = [harvard(mrn, demographics, diagnoses) for mrn in list(demographics['MRN'])]
harvardValues = [harvard(mrn, demographics, diagnoses) for mrn in noIAA]
harvardCutoff = [int(i>0.632) for i in harvardValues]

# 1 = definitely RA because good specificity. 
eularCol = ['ESR_VALUE', 'CRP_VALUE']

noHarvard = [a for a,b in zip(noIAA, harvardCutoff) if not b]
noHarvardDemographics = demo2.loc[noHarvard]

noHarvardGold = gold.loc[noHarvard]
y = noHarvardGold[noHarvardGold.isin([1,2])]
y = y.map({1:1,2:0})

goodMRN = list(y.index)

noHarvardDemographics=noHarvardDemographics.loc[goodMRN]

x = noHarvardDemographics[eularCol]
x=x.fillna(0)
x=x.replace('<0.3', 0.1)
x=x.replace('<0.5', 0.3)
x=x.astype(float)
x = x.to_numpy()
y = y.to_numpy()

# Decision tree to classify remainder
clf = tree.DecisionTreeClassifier(max_depth=3)
scores = cross_val_score(estimator=clf, X=x, y=y, n_jobs=4)
clf.fit(x,y)
tree.plot_tree(clf) 
clf.predict(x) #Since 9/157 are positive, classifier predicts everything as negative and gets a 94% success rate

# Try: downsampling

noHarvardOne = noHarvardGold[noHarvardGold==1].index
noHarvardOneDemo = noHarvardDemographics.loc[noHarvardOne][eularCol]
