# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:04:47 2021

@author: hwz62
"""

import pandas as pd
from random import shuffle

set3Filename = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set3_single235_09252020.xlsx'
set3LucasFilename = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set3_single235_lucas_09252020.xlsx'
set2IAA = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set2_iaa50_09252020.xlsx'

control3Filename = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\control3_single118_01112021.xlsx'
control3LucasFilename = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\control3_single118_lucas_01112021.xlsx'
control2IAA = 'C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\control2_iaa25_01112021.xlsx'

# Read in 
cohort1 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 1', engine='openpyxl')
cohort2 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 2', engine='openpyxl')
cohort3 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 3', engine='openpyxl')
cohort4 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 4', engine='openpyxl')
cohort5 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 5', engine='openpyxl')
cohort6 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 6', engine='openpyxl')
cohort7 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 7', engine='openpyxl')
cohort8 = pd.read_excel(set3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 8', engine='openpyxl')
cohortLucas = pd.read_excel(set3LucasFilename, usecols='A:J', index_col=1, engine='openpyxl').sort_index()
cohortiaa = pd.read_excel(set2IAA, usecols='A:J', index_col=1, engine='openpyxl')

control1 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 1', engine='openpyxl')
control2 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 2', engine='openpyxl')
control3 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 3', engine='openpyxl')
control4 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 4', engine='openpyxl')
control5 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 5', engine='openpyxl')
control6 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 6', engine='openpyxl')
control7 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 7', engine='openpyxl')
control8 = pd.read_excel(control3Filename, usecols='A:J', index_col=1, sheet_name='Cohort 8', engine='openpyxl')
controlLucas = pd.read_excel(control3LucasFilename, usecols='A:J', index_col=1, engine='openpyxl').sort_index()
controliaa = pd.read_excel(control2IAA, usecols='A:J', index_col=1, engine='openpyxl')



cohort1Index = list(cohort1.index)
cohort2Index = list(cohort2.index)
cohort3Index = list(cohort3.index)
cohort4Index = list(cohort4.index)
cohort5Index = list(cohort5.index)
cohort6Index = list(cohort6.index)
cohort7Index = list(cohort7.index)
cohort8Index = list(cohort8.index)
cohortLucasIndex = list(cohortLucas.index)
cohortiaaIndex = list(cohortiaa.index)

control1Index = list(control1.index)
control2Index = list(control2.index)
control3Index = list(control3.index)
control4Index = list(control4.index)
control5Index = list(control5.index)
control6Index = list(control6.index)
control7Index = list(control7.index)
control8Index = list(control8.index)
controlLucasIndex = list(controlLucas.index)
controliaaIndex = list(controliaa.index)


shuffle(cohort1Index)
shuffle(cohort2Index)
shuffle(cohort3Index)
shuffle(cohort4Index)
shuffle(cohort5Index)
shuffle(cohort6Index)
shuffle(cohort7Index)
shuffle(cohort8Index)
shuffle(cohortLucasIndex)
shuffle(cohortiaaIndex)

shuffle(control1Index)
shuffle(control2Index)
shuffle(control3Index)
shuffle(control4Index)
shuffle(control5Index)
shuffle(control6Index)
shuffle(control7Index)
shuffle(control8Index)
shuffle(controlLucasIndex)
shuffle(controliaaIndex)

# Downsample half of the cases and merge with controls
cohort1 = pd.concat([cohort1, control1])
cohort2 = pd.concat([cohort2, control2])
cohort3 = pd.concat([cohort3, control3])
cohort4 = pd.concat([cohort4, control4])
cohort5 = pd.concat([cohort5, control5])
cohort6 = pd.concat([cohort6, control6])
cohort7 = pd.concat([cohort7, control7])
cohort8 = pd.concat([cohort8, control8])
cohortLucas = pd.concat([cohortLucas, controlLucas])
cohortiaa = pd.concat([cohortiaa, controliaa])


cohort1Index = cohort1Index[:117] + control1Index
cohort2Index = cohort2Index[:117] + control2Index
cohort3Index = cohort3Index[:117] + control3Index
cohort4Index = cohort4Index[:117] + control4Index
cohort5Index = cohort5Index[:117] + control5Index
cohort6Index = cohort6Index[:117] + control6Index
cohort7Index = cohort7Index[:117] + control7Index
cohort8Index = cohort8Index[:117] + control8Index
cohortLucasIndex = cohortLucasIndex[:117] + controlLucasIndex
cohortiaaIndex = cohortiaaIndex[:25] + controliaaIndex

IndexOrder = list(range(285))
shuffle(IndexOrder)
iaaPos = IndexOrder[:50]
indPos = IndexOrder[50:]

newCohort1 = pd.DataFrame()
newCohort2 = pd.DataFrame()
newCohort3 = pd.DataFrame()
newCohort4 = pd.DataFrame()
newCohort5 = pd.DataFrame()
newCohort6 = pd.DataFrame()
newCohort7 = pd.DataFrame()
newCohort8 = pd.DataFrame()
newCohortLucas = pd.DataFrame()

for i in range(len(indPos)):
    pos = indPos[i]
    newCohort1[pos]=pd.concat([pd.Series([cohort1Index[i]]), cohort1.loc[cohort1Index[i]]])
    newCohort2[pos]=pd.concat([pd.Series([cohort2Index[i]]), cohort2.loc[cohort2Index[i]]])
    newCohort3[pos]=pd.concat([pd.Series([cohort3Index[i]]), cohort3.loc[cohort3Index[i]]])
    newCohort4[pos]=pd.concat([pd.Series([cohort4Index[i]]), cohort4.loc[cohort4Index[i]]])
    newCohort5[pos]=pd.concat([pd.Series([cohort5Index[i]]), cohort5.loc[cohort5Index[i]]])
    newCohort6[pos]=pd.concat([pd.Series([cohort6Index[i]]), cohort6.loc[cohort6Index[i]]])
    newCohort7[pos]=pd.concat([pd.Series([cohort7Index[i]]), cohort7.loc[cohort7Index[i]]])
    newCohort8[pos]=pd.concat([pd.Series([cohort8Index[i]]), cohort8.loc[cohort8Index[i]]])
    newCohortLucas[pos]=pd.concat([pd.Series([cohortLucasIndex[i]]), cohortLucas.loc[cohortLucasIndex[i]]])

for j in range(len(iaaPos)):
    pos = iaaPos[j]
    iaaItem = pd.concat([pd.Series([cohortiaaIndex[j]]), cohortiaa.loc[cohortiaaIndex[j]]])
    newCohort1[pos]=iaaItem
    newCohort2[pos]=iaaItem
    newCohort3[pos]=iaaItem
    newCohort4[pos]=iaaItem
    newCohort5[pos]=iaaItem
    newCohort6[pos]=iaaItem
    newCohort7[pos]=iaaItem
    newCohort8[pos]=iaaItem
    newCohortLucas[pos]=iaaItem

finalCohort1 = newCohort1.transpose()
finalCohort2 = newCohort2.transpose()
finalCohort3 = newCohort3.transpose()
finalCohort4 = newCohort4.transpose()
finalCohort5 = newCohort5.transpose()
finalCohort6 = newCohort6.transpose()
finalCohort7 = newCohort7.transpose()
finalCohort8 = newCohort8.transpose()
finalCohortLucas = newCohortLucas.transpose()

finalCohort1 = finalCohort1.sort_index()
finalCohort2 = finalCohort2.sort_index()
finalCohort3 = finalCohort3.sort_index()
finalCohort4 = finalCohort4.sort_index()
finalCohort5 = finalCohort5.sort_index()
finalCohort6 = finalCohort6.sort_index()
finalCohort7 = finalCohort7.sort_index()
finalCohort8 = finalCohort8.sort_index()
finalCohortLucas = finalCohortLucas.sort_index()

finalCohort1.rename(columns={0:'MRN'}, inplace=True)
finalCohort2.rename(columns={0:'MRN'}, inplace=True)
finalCohort3.rename(columns={0:'MRN'}, inplace=True)
finalCohort4.rename(columns={0:'MRN'}, inplace=True)
finalCohort5.rename(columns={0:'MRN'}, inplace=True)
finalCohort6.rename(columns={0:'MRN'}, inplace=True)
finalCohort7.rename(columns={0:'MRN'}, inplace=True)
finalCohort8.rename(columns={0:'MRN'}, inplace=True)
finalCohortLucas.rename(columns={0:'MRN'}, inplace=True)

with pd.ExcelWriter('set4_single285_01112021_mixed.xlsx') as writer:
    finalCohort1['MRN'].to_excel(writer, sheet_name='Cohort 1')
    finalCohort2['MRN'].to_excel(writer, sheet_name='Cohort 2')
    finalCohort3['MRN'].to_excel(writer, sheet_name='Cohort 3')
    finalCohort4['MRN'].to_excel(writer, sheet_name='Cohort 4')
    finalCohort5['MRN'].to_excel(writer, sheet_name='Cohort 5')
    finalCohort6['MRN'].to_excel(writer, sheet_name='Cohort 6')
    finalCohort7['MRN'].to_excel(writer, sheet_name='Cohort 7')
    finalCohort8['MRN'].to_excel(writer, sheet_name='Cohort 8')

with pd.ExcelWriter('set4_single285_lucas_01112021_mixed.xlsx') as writer:
    finalCohortLucas['MRN'].to_excel(writer, sheet_name="Lucas' set")

indPos2 = pd.DataFrame(indPos)
iaaPos2 = pd.DataFrame(iaaPos)

with pd.ExcelWriter('positions.xlsx') as writer:
    indPos2.to_excel(writer, sheet_name="Individual Positions")
    iaaPos2.to_excel(writer, sheet_name="IAA Positions")