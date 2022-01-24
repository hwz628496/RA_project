# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 08:58:03 2020

@author: hwz62
"""

import pandas as pd
import numpy as np
from harvard import harvard

# problemList = pd.read_csv('problemList.csv')
diagnoses = pd.read_csv('Ranganath_DX_090820.txt', sep='","', header=0)
demographics = pd.read_csv('demographics2.csv')

demographics = demographics[demographics['RA_ENC_CNT'].notna()] #pulls only those with RA

# harvardDict={}
# for mrn in list(demographics['MRN']):
#     harvardValue = harvard(mrn, demographics, diagnoses)
#     harvardDict[mrn] = harvardValue

# Drop the MRN's of the 15 for QA

from lucasMRN import positive15, negative15
for code in positive15:
    dropMRN = demographics[demographics['MRN']==code].index[0]
    demographics = demographics.drop([dropMRN])
for code in negative15:
    dropMRN = demographics[demographics['MRN']==code].index[0]
    demographics = demographics.drop([dropMRN])


harvardValues = [harvard(mrn, demographics, diagnoses) for mrn in list(demographics['MRN'])]
x=np.array(harvardValues)
bins = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1])
inds = np.digitize(x, bins)
binDict=dict(zip(list(demographics['MRN']),inds))

ageProfile = dict(demographics['AGE'].value_counts())
ethnicityProfileRaw = dict(demographics['ETHNICITY'].value_counts())
raceProfileRaw = dict(demographics['RACE'].value_counts())
sexProfile = dict(demographics['SEX'].value_counts())


# Pool features to establish baseline
ageDeciles = {'18-27':0,'28-37':0, '38-47':0, '48-57':0, '58-67':0, '58-67':0, '68-77':0, '78-87':0, '88+':0}

for i in ageProfile.keys():
    if i <= 27:
        ageDeciles['18-27']=ageDeciles['18-27']+ageProfile[i]
    elif (i >= 28 and i <= 37):
        ageDeciles['28-37']=ageDeciles['28-37']+ageProfile[i]
    elif (i >= 38 and i <= 47):
        ageDeciles['38-47']=ageDeciles['38-47']+ageProfile[i]
    elif (i >= 48 and i <= 57):
        ageDeciles['48-57']=ageDeciles['48-57']+ageProfile[i]
    elif (i >= 58 and i <= 67):
        ageDeciles['58-67']=ageDeciles['58-67']+ageProfile[i]
    elif (i >= 68 and i <= 77):
        ageDeciles['68-77']=ageDeciles['68-77']+ageProfile[i]
    elif (i >= 78 and i <= 87):
        ageDeciles['78-87']=ageDeciles['78-87']+ageProfile[i]
    elif i >= 88:
        ageDeciles['88+']=ageDeciles['88+']+ageProfile[i]
    else:
        ValueError('Unfound age decile {}'.format(i))

ethnicityProfile = {'Hispanic':0, 'Not Hispanic':0, 'Unkonwn/Patient Refused':0}

for j in ethnicityProfileRaw.keys():
    if j == 'Not Hispanic or Latino':
        ethnicityProfile['Not Hispanic']=ethnicityProfile['Not Hispanic']+ethnicityProfileRaw[j]
    elif (j == 'Unknown' or j == 'Patient Refused'):
        ethnicityProfile['Unkonwn/Patient Refused']=ethnicityProfile['Unkonwn/Patient Refused']+ethnicityProfileRaw[j]
    else:
        ethnicityProfile['Hispanic']=ethnicityProfile['Hispanic']+ethnicityProfileRaw[j]

raceProfile = {'White':0, 'Not White':0, 'Unknown/Patient Refused':0}

for k in raceProfileRaw.keys():
    if k == 'White or Caucasian':
        raceProfile['White']=raceProfile['White']+raceProfileRaw[k]
    elif (k == 'Unknown' or k == 'Patient Refused'):
        raceProfile['Unknown/Patient Refused']=raceProfile['Unknown/Patient Refused']+raceProfileRaw[k]
    else:
        raceProfile['Not White']=raceProfile['Not White']+raceProfileRaw[k]


# Pool features for patients

def ageBin(i):
    if i <= 27:
        return '18-27'
    elif (i >= 28 and i <= 37):
        return '28-37'
    elif (i >= 38 and i <= 47):
        return '38-47'
    elif (i >= 48 and i <= 57):
        return '48-57'
    elif (i >= 58 and i <= 67):
        return '58-67'
    elif (i >= 68 and i <= 77):
        return '68-77'
    elif (i >= 78 and i <= 87):
        return '78-87'
    elif i >= 88:
        return '88+'
    else:
        return ValueError('Unfound age decile {}'.format(i))

def ethnicityBin(j):
    if j == 'Not Hispanic or Latino':
        return 'Not Hispanic'
    elif (j == 'Unknown' or j == 'Patient Refused'):
        return 'Unknown/Patient Refused'
    else:
        return 'Hispanic'

def raceBin(k):
    if k == 'White or Caucasian':
        return 'White'
    elif (k == 'Unknown' or k == 'Patient Refused'):
        return 'Unknown/Patient Refused'
    else:
        return 'Not White'

patients = demographics.filter(['MRN', 'AGE', 'SEX', 'RACE', 'ETHNICITY'])


def encoder(sex, race, eth, age):
    code=['9', '9', '9', '9']
    if sex=='Female':
        code[0]='a'
    if sex=='Male':
        code[0]='b'
    if sex=='Unknown':
        code[0]='c'
    if race=='White':
        code[1]='a'
    if race=='Not White':
        code[1]='b'
    if race=='Unknown/Patient Refused':
        code[1]='c'
    if eth=='Not Hispanic':
        code[2]='a'
    if eth=='Hispanic':
        code[2]='b'
    if eth=='Unknown/Patient Refused':
        code[2]='c'
    if age=='18-27':
        code[3]='a'
    if age=='28-37':
        code[3]='b'
    if age=='38-47':
        code[3]='c'
    if age=='48-57':
        code[3]='d'
    if age=='58-67':
        code[3]='e'
    if age=='68-77':
        code[3]='f'
    if age=='78-87':
        code[3]='g'
    if age=='88+':
        code[3]='h'
    return ''.join(code)

ageList=[]
ethnicyList=[]
raceList=[]

for index, row in patients.iterrows():
    ageList.append(ageBin(row['AGE']))
    ethnicyList.append(ethnicityBin(row['ETHNICITY']))
    raceList.append(raceBin(row['RACE']))

patients['AGEBIN'] = ageList
patients['RACEBIN'] = raceList
patients['ETHNICITYBIN'] = ethnicyList

encodeList=[]
for index, row in patients.iterrows():
    code1 = encoder(row['SEX'], row['RACEBIN'], row['ETHNICITYBIN'], row['AGEBIN'])
    code2 = code1+str(binDict[row['MRN']])
    encodeList.append(code2)

patients['CODE'] = encodeList


if patients[patients['CODE']=='9999'].empty == False:
    badMRN = list(patients[patients['CODE']=='9999']['MRN'])
    badMRNstr = "".join(str(badMRN))
    raise ValueError('Code 9999 encountered for MRN: {}'.format(badMRNstr))

# Generate dictionary of MRN's for each code combination

# def numCohort(listLength, patients):
#     expectedTranch = {}
#     codeDist = dict(patients['CODE'].value_counts())
#     total = sum(codeDist.values())
#     for key in codeDist.items():
#         expectedNumber = listLength*key[1]/total
#         if expectedNumber > 2:
#             expectedTranch[key[0]] = int(expectedNumber)
#     return expectedTranch

# numCohort(250, patients)

# from scipy.stats import rv_discrete
# codeDist2={}
# codeDist = dict(patients['CODE'].value_counts())
# total = sum(codeDist.values())
# for key in codeDist.items():
#     codeDist2[key[0]] = key[1]/total

from random import choices
from random import shuffle

def numPatientTypes(num, patients):
    codeDist = dict(patients['CODE'].value_counts())
    weights = list(codeDist.values())
    population = list(codeDist.keys())
    return choices(population=population,weights=weights, k=num)


def produceCohort(ptct, drawingDf, patients):
    codesList = numPatientTypes(ptct, drawingDf)
    cohort = []
    for code in codesList:
        MRNSubset = list(drawingDf[drawingDf['CODE']==code]['MRN'])
        shuffle(MRNSubset)
        MRNPull = MRNSubset[0]
        cohort.append(MRNPull)
        MRNIndex = drawingDf.loc[drawingDf['MRN']==MRNPull].index[0]
        drawingDf = drawingDf.drop([MRNIndex])
    cohortDf = pd.DataFrame()
    for mrn in cohort:
        row=patients.loc[patients['MRN']==mrn]
        cohortDf = cohortDf.append(row)
    return cohortDf, drawingDf


# Draw lists

drawing0 = patients.filter(['MRN', 'CODE'])
iaa, drawing1 = produceCohort(50, drawing0, patients)
lucas, drawing2 = produceCohort(235, drawing1, patients)
cohort1, drawing3 = produceCohort(235, drawing2, patients)
cohort2, drawing4 = produceCohort(235, drawing3, patients)
cohort3, drawing5 = produceCohort(235, drawing4, patients)
cohort4, drawing6 = produceCohort(235, drawing5, patients)
cohort5, drawing7 = produceCohort(235, drawing6, patients)
cohort6, drawing8 = produceCohort(235, drawing7, patients)
cohort7, drawing9 = produceCohort(235, drawing8, patients)
cohort8, drawing10 = produceCohort(235, drawing9, patients)


# Check distribution of patients

# from scipy import stats

# def compareCohorts(cohort, patients):
#     baseDist = dict(patients['CODE'].value_counts())
#     cohortDist = dict(cohort['CODE'].value_counts())
#     baseTot = sum(baseDist.values())
#     cohortTot = sum(cohortDist.values())
#     for key, value in baseDist.items():
#         baseDist[key] = value/baseTot
#     for key, value in cohortDist.items():
#         cohortDist[key] = value/cohortTot
#     diff = {}
#     for key, value in cohortDist.items():
#         diff[key] = baseDist[key]-cohortDist[key]
#     ttest, p = stats.ttest_1samp(list(diff.values()), 0)
#     return diff, p

# diff1, p1 = compareCohorts(cohort1, patients)
# diff2, p2 = compareCohorts(cohort2, patients)
# diff3, p3 = compareCohorts(cohort3, patients)
# diff4, p4 = compareCohorts(cohort4, patients)
# diff5, p5 = compareCohorts(cohort5, patients)
# diff6, p6 = compareCohorts(cohort6, patients)
# diff7, p7 = compareCohorts(cohort7, patients)
# diff8, p8 = compareCohorts(cohort8, patients)

# codeList = list(patients['CODE'].unique())

# bin123=['a', 'b', 'c']
# bin4=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# bin5=['1', '2', '3', '4', '5']

# from itertools import product

# codeList = [''.join(i) for i in product(bin123, bin123, bin123, bin4, bin5)]

# popCode = [sum(patients['CODE']==code) for code in codeList]
# cohort1Code = [sum(cohort1['CODE']==code) for code in codeList]

# from scipy.stats import chisquare
# chisquare(cohort1Code, popCode)




# Save cohorts to file

with pd.ExcelWriter('set3_single235_09252020.xlsx') as writer:
    cohort1.to_excel(writer, sheet_name = 'Cohort 1')
    cohort2.to_excel(writer, sheet_name = 'Cohort 2')
    cohort3.to_excel(writer, sheet_name = 'Cohort 3')
    cohort4.to_excel(writer, sheet_name = 'Cohort 4')
    cohort5.to_excel(writer, sheet_name = 'Cohort 5')
    cohort6.to_excel(writer, sheet_name = 'Cohort 6')
    cohort7.to_excel(writer, sheet_name = 'Cohort 7')
    cohort8.to_excel(writer, sheet_name = 'Cohort 8')

with pd.ExcelWriter('set2_iaa50_09252020.xlsx') as writer:
    iaa.to_excel(writer, sheet_name = 'Inter-rater')

with pd.ExcelWriter('set3_single235_lucas_09252020.xlsx') as writer:
    lucas.to_excel(writer, sheet_name = "Lucas' set")


with pd.ExcelWriter('set3_single235_09252020_MRNonly.xlsx') as writer:
    cohort1['MRN'].to_excel(writer, sheet_name = 'Cohort 1')
    cohort2['MRN'].to_excel(writer, sheet_name = 'Cohort 2')
    cohort3['MRN'].to_excel(writer, sheet_name = 'Cohort 3')
    cohort4['MRN'].to_excel(writer, sheet_name = 'Cohort 4')
    cohort5['MRN'].to_excel(writer, sheet_name = 'Cohort 5')
    cohort6['MRN'].to_excel(writer, sheet_name = 'Cohort 6')
    cohort7['MRN'].to_excel(writer, sheet_name = 'Cohort 7')
    cohort8['MRN'].to_excel(writer, sheet_name = 'Cohort 8')

with pd.ExcelWriter('set2_iaa50_09252020_MRNonly.xlsx') as writer:
    iaa['MRN'].to_excel(writer, sheet_name = 'Inter-rater')

# Save latest drawing in case of needing more cases
with pd.ExcelWriter('remainder_09252020.xlsx') as writer:
    drawing10.to_excel(writer, sheet_name = 'Drawing 10 remainder')