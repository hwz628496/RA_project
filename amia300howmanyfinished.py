# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:37:15 2021

@author: hwz62
"""

import pandas as pd
from amia300List import totallist2 as totallist

currentlyDoneAll = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-300FullData_DATA_2021-03-02_1637.csv')
currentlyDoneMRN = list(currentlyDoneAll.mrn)

doneFromList = [x for x in currentlyDoneMRN if x in totallist]

# 1 is Veena
# 9 is David Chetrit
# 3 is Angela Pham
#10 is Richard Sato
# 5 is Karla Criner

for i in [1, 9, 3, 10, 5]:
    print(len([x for x in list(currentlyDoneAll[currentlyDoneAll.extractor_name==i].mrn) if x in totallist]))