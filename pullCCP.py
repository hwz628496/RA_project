# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:08:50 2021

@author: hwz62
"""

import pandas as pd

EightSetFilename = "C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 11-13-2020\\set3_single285_11132020_merged.xlsx"
LucasSetFilename = "C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 11-13-2020\\set3_single285_lucas_11132020_merged.xlsx"


cohort1 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 1', engine='openpyxl')
cohort2 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 2', engine='openpyxl')
cohort3 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 3', engine='openpyxl')
cohort4 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 4', engine='openpyxl')
cohort5 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 5', engine='openpyxl')
cohort6 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 6', engine='openpyxl')
cohort7 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 7', engine='openpyxl')
cohort8 = pd.read_excel(EightSetFilename, usecols='B', sheet_name='Cohort 8', engine='openpyxl')
cohortLucas = pd.read_excel(LucasSetFilename, usecols='B', sheet_name="Lucas' set", engine='openpyxl')

casesDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')
controlDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')

undesiredColumns = ['CONDITION', 'SEX_1', 'RACE_1', 'ETHNICITY_1']
controlDemographics2 = controlDemographics.drop(undesiredColumns, axis=1)
allDemographics = pd.concat([casesDemographics, controlDemographics2])
allDemographics=allDemographics.set_index('MRN')

cohort1CCP = [allDemographics.loc[cohort1.MRN[i]].HIGHEST_CCP for i in range(len(cohort1))]
cohort2CCP = [allDemographics.loc[cohort2.MRN[i]].HIGHEST_CCP for i in range(len(cohort2))]
cohort3CCP = [allDemographics.loc[cohort3.MRN[i]].HIGHEST_CCP for i in range(len(cohort3))]
cohort4CCP = [allDemographics.loc[cohort4.MRN[i]].HIGHEST_CCP for i in range(len(cohort4))]
cohort5CCP = [allDemographics.loc[cohort5.MRN[i]].HIGHEST_CCP for i in range(len(cohort5))]
cohort6CCP = [allDemographics.loc[cohort6.MRN[i]].HIGHEST_CCP for i in range(len(cohort6))]
cohort7CCP = [allDemographics.loc[cohort7.MRN[i]].HIGHEST_CCP for i in range(len(cohort7))]
cohort8CCP = [allDemographics.loc[cohort8.MRN[i]].HIGHEST_CCP for i in range(len(cohort8))]
cohortLucasCCP = [allDemographics.loc[cohortLucas.MRN[i]].HIGHEST_CCP for i in range(len(cohortLucas))]

cohort1["Highest CCP"] = cohort1CCP
cohort2["Highest CCP"] = cohort2CCP
cohort3["Highest CCP"] = cohort3CCP
cohort4["Highest CCP"] = cohort4CCP
cohort5["Highest CCP"] = cohort5CCP
cohort6["Highest CCP"] = cohort6CCP
cohort7["Highest CCP"] = cohort7CCP
cohort8["Highest CCP"] = cohort8CCP
cohortLucas["Highest CCP"] = cohortLucasCCP

with pd.ExcelWriter('set4_single285_01132021_mixed.xlsx') as writer:
    cohort1.to_excel(writer, sheet_name='Cohort 1')
    cohort2.to_excel(writer, sheet_name='Cohort 2')
    cohort3.to_excel(writer, sheet_name='Cohort 3')
    cohort4.to_excel(writer, sheet_name='Cohort 4')
    cohort5.to_excel(writer, sheet_name='Cohort 5')
    cohort6.to_excel(writer, sheet_name='Cohort 6')
    cohort7.to_excel(writer, sheet_name='Cohort 7')
    cohort8.to_excel(writer, sheet_name='Cohort 8')

with pd.ExcelWriter('set4_single285_lucas_01132021_mixed.xlsx') as writer:
    cohortLucas.to_excel(writer, sheet_name="Lucas' set")