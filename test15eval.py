# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 11:38:32 2021

@author: hwz62
"""
import pandas as pd
from helpers import harvard

test15 = [625998, 876736, 891671, 1288012, 1382966, 1766518, 2048955, 2327552, 3947163, 4166111, 4315159, 4561865, 5951119, 6152832, 6187135]
positive = [4561865, 876736, 6152832, 6187135, 1382966, 5951119, 3947163, 2048955, 891671, 625998]
negative = [2327552, 1288012, 1766518, 4315159, 4166111]


diagnoses = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
demographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')


harvard15 = [harvard(mrn, demographics, diagnoses) for mrn in test15]
harvardpositive = [harvard(mrn, demographics, diagnoses) for mrn in positive]
harvardnegative = [harvard(mrn, demographics, diagnoses) for mrn in negative]