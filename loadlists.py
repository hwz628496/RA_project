# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:17:55 2020

@author: hwz62
"""

import pandas as pd
from random import shuffle

set3Filename = 'set3_single235_09252020.xlsx'
set3LucasFilename = 'set3_single235_lucas_09252020.xlsx'
set2IAA = 'set2_iaa50_09252020.xlsx'

cohort1 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 1')
cohort2 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 2')
cohort3 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 3')
cohort4 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 4')
cohort5 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 5')
cohort6 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 6')
cohort7 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 7')
cohort8 = pd.read_excel(set3Filename, usecols='A:J', index_col=0, sheet_name='Cohort 8')
cohortLucas = pd.read_excel(set3LucasFilename, usecols='A:J', index_col=0).sort_index()
iaa = pd.read_excel(set2IAA, usecols='A:J', index_col=0)

cohort1Index = list(cohort1.index)
cohort2Index = list(cohort2.index)
cohort3Index = list(cohort3.index)
cohort4Index = list(cohort4.index)
cohort5Index = list(cohort5.index)
cohort6Index = list(cohort6.index)
cohort7Index = list(cohort7.index)
cohort8Index = list(cohort8.index)
cohortLucasIndex = list(cohortLucas.index)
iaaIndex = list(iaa.index)

shuffle(cohort1Index)
shuffle(cohort2Index)
shuffle(cohort3Index)
shuffle(cohort4Index)
shuffle(cohort5Index)
shuffle(cohort6Index)
shuffle(cohort7Index)
shuffle(cohort8Index)
shuffle(cohortLucasIndex)
shuffle(iaaIndex)

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
    newCohort1[pos]=cohort1.loc[cohort1Index[i]]
    newCohort2[pos]=cohort2.loc[cohort2Index[i]]
    newCohort3[pos]=cohort3.loc[cohort3Index[i]]
    newCohort4[pos]=cohort4.loc[cohort4Index[i]]
    newCohort5[pos]=cohort5.loc[cohort5Index[i]]
    newCohort6[pos]=cohort6.loc[cohort6Index[i]]
    newCohort7[pos]=cohort7.loc[cohort7Index[i]]
    newCohort8[pos]=cohort8.loc[cohort8Index[i]]
    newCohortLucas[pos]=cohortLucas.loc[cohortLucasIndex[i]]

for j in range(len(iaaPos)):
    pos = iaaPos[j]
    newCohort1[pos]=iaa.loc[iaaIndex[j]]
    newCohort2[pos]=iaa.loc[iaaIndex[j]]
    newCohort3[pos]=iaa.loc[iaaIndex[j]]
    newCohort4[pos]=iaa.loc[iaaIndex[j]]
    newCohort5[pos]=iaa.loc[iaaIndex[j]]
    newCohort6[pos]=iaa.loc[iaaIndex[j]]
    newCohort7[pos]=iaa.loc[iaaIndex[j]]
    newCohort8[pos]=iaa.loc[iaaIndex[j]]
    newCohortLucas[pos]=iaa.loc[iaaIndex[j]]

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

with pd.ExcelWriter('set3_single285_11132020_merged.xlsx') as writer:
    finalCohort1['MRN'].to_excel(writer, sheet_name='Cohort 1')
    finalCohort2['MRN'].to_excel(writer, sheet_name='Cohort 2')
    finalCohort3['MRN'].to_excel(writer, sheet_name='Cohort 3')
    finalCohort4['MRN'].to_excel(writer, sheet_name='Cohort 4')
    finalCohort5['MRN'].to_excel(writer, sheet_name='Cohort 5')
    finalCohort6['MRN'].to_excel(writer, sheet_name='Cohort 6')
    finalCohort7['MRN'].to_excel(writer, sheet_name='Cohort 7')
    finalCohort8['MRN'].to_excel(writer, sheet_name='Cohort 8')

with pd.ExcelWriter('set3_single285_lucas_11132020_merged.xlsx') as writer:
    finalCohortLucas['MRN'].to_excel(writer, sheet_name="Lucas' set")

indPos2 = pd.DataFrame(indPos)
iaaPos2 = pd.DataFrame(iaaPos)

with pd.ExcelWriter('positions.xlsx') as writer:
    indPos2.to_excel(writer, sheet_name="Individual Positions")
    iaaPos2.to_excel(writer, sheet_name="IAA Positions")