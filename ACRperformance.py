# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 08:49:44 2021

@author: hwz62
"""

import pandas as pd
from amia300List import totallist2 as totallist
from amia300List import cases
from amia300List import controls
from amia300List import list1, list2

currentlyDoneAll = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-300AllReviews_DATA_2021-03-23_0849.csv')
iaa = [x for x in list1 if x in list2]
individuals = [x for x in totallist if x not in iaa]

amia300 = pd.DataFrame()

for i in individuals:
    amia300=amia300.append(currentlyDoneAll[currentlyDoneAll.mrn==i])

amia300 = amia300.drop([296, 297])

acrCol = ['joint_involvement','serology', 'apr_score', 'sdd_score','scores']
acrPred = amia300[acrCol[0:4]].sum(axis=1)
summary=[amia300[i].value_counts() for i in acrCol]