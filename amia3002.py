# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:05:57 2021

@author: hwz62
"""

import pandas as pd

casesDiag = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
casesDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')

controlDiag = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_DX.txt', sep='|', header=0)
controlDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')

lucasCasesDone = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-LucasCases_DATA_2021-01-30_1112.csv')
lucasControlsDone = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-LucasControls_DATA_2021-01-30_1108.csv')

lucasCases = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set4_single285_lucas_01112021_merged.xlsx', engine='openpyxl')
lucasControls = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\lucas_controls_01142021_nopw.xlsx', engine='openpyxl')

lucasCasesOld = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set3_single285_lucas_11132020_merged.xlsx', engine='openpyxl')


lucasCaseslist = list(lucasCases.MRN)
lucasCasesOldlist = list(lucasCasesOld.MRN)
lucasControlslist = list(lucasControls.MRN)
lucasCasesDonelist = list(lucasCasesDone.mrn)
lucasControlsDonelist = list(lucasControlsDone.mrn)

lucasCasesnoControl = [x for x in lucasCaseslist if x not in lucasControlslist]
