# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 13:28:20 2022

@author: hwz62
"""

import pandas as pd
from helpers import loadClinData
from harvard import harvard
from sklearn.metrics import confusion_matrix


demographics, demo2, diagnoses, diag2 = loadClinData()
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
droppedHarvard=list(harvard3200.harvard)
droppedMRN=list(harvard3200.mrn)
droppedRA=[mrn3200.loc[i].ra for i in droppedMRN]
droppedHarYN=[int(i>0.632) for i in droppedHarvard]
df = pd.DataFrame({'mrn': droppedMRN,'harvard': droppedHarvard, 'ra': droppedRA, 'harvard cutoff': droppedHarYN})

#reload with clarified ra entries
df = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\code\\3200MRN.csv')
confusion3200 = confusion_matrix(df['ra'], df['harvard cutoff'])


#### Original 300 ####
from amia300List import list1, list2, list3, list4, list5, list6

#calculate harvard scores
list1Har = []
for i in list1:
    list1Har.append(harvard(i,demographics,diagnoses))
list2Har = []
for i in list2:
    list2Har.append(harvard(i,demographics,diagnoses))
list3Har = []
for i in list3:
    list3Har.append(harvard(i,demographics,diagnoses))
list4Har = []
for i in list4:
    list4Har.append(harvard(i,demographics,diagnoses))
list5Har = []
for i in list5:
    list5Har.append(harvard(i,demographics,diagnoses))
list6Har = []
for i in list6:
    list6Har.append(harvard(i,demographics,diagnoses))

HarYN1=[int(i>0.632) for i in list1Har]
HarYN2=[int(i>0.632) for i in list2Har]
HarYN3=[int(i>0.632) for i in list3Har]
HarYN4=[int(i>0.632) for i in list4Har]
HarYN5=[int(i>0.632) for i in list5Har]
HarYN6=[int(i>0.632) for i in list6Har]

list1Df = pd.DataFrame({'mrn': list1,'harvard': list1Har, 'ra': droppedRA, 'harvard cutoff': HarYN1})