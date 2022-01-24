# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:40:21 2021

@author: hwz62
"""

import pandas as pd
import numpy as np
# from exclusionICD import excexact, excstartswith
from helpers import ageBin, ethnicityBin, raceBin
from helpers import encoder, produceCohort, harvard
# from lucasMRN import positive15, negative15
from random import shuffle

cDiag = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_DX.txt', sep='|', header=0)
cDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')


harvardValues = [harvard(mrn, cDemographics, cDiag) for mrn in list(cDemographics['MRN'])]
x = np.array(harvardValues)
bins = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1])
inds = np.digitize(x, bins)
binDict = dict(zip(list(cDemographics['MRN']), inds))

ageProfile = dict(cDemographics['AGE'].value_counts())
ethnicityProfileRaw = dict(cDemographics['ETHNICITY'].value_counts())
raceProfileRaw = dict(cDemographics['RACE'].value_counts())
sexProfile = dict(cDemographics['SEX'].value_counts())


# Pool features to establish baseline
ageDeciles = {'18-27': 0,
              '28-37': 0,
              '38-47': 0,
              '48-57': 0,
              '58-67': 0,
              '58-67': 0,
              '68-77': 0,
              '78-87': 0,
              '88+': 0}

for i in ageProfile.keys():
    if i <= 27:
        ageDeciles['18-27'] = ageDeciles['18-27']+ageProfile[i]
    elif (i >= 28 and i <= 37):
        ageDeciles['28-37'] = ageDeciles['28-37']+ageProfile[i]
    elif (i >= 38 and i <= 47):
        ageDeciles['38-47'] = ageDeciles['38-47']+ageProfile[i]
    elif (i >= 48 and i <= 57):
        ageDeciles['48-57'] = ageDeciles['48-57']+ageProfile[i]
    elif (i >= 58 and i <= 67):
        ageDeciles['58-67'] = ageDeciles['58-67']+ageProfile[i]
    elif (i >= 68 and i <= 77):
        ageDeciles['68-77'] = ageDeciles['68-77']+ageProfile[i]
    elif (i >= 78 and i <= 87):
        ageDeciles['78-87'] = ageDeciles['78-87']+ageProfile[i]
    elif i >= 88:
        ageDeciles['88+'] = ageDeciles['88+']+ageProfile[i]
    else:
        ValueError('Unfound age decile {}'.format(i))

ethnicityProfile = {'Hispanic': 0,
                    'Not Hispanic': 0,
                    'Unkonwn/Patient Refused': 0}

for j in ethnicityProfileRaw.keys():
    if j == 'Not Hispanic or Latino':
        ethnicityProfile['Not Hispanic'] = ethnicityProfile['Not Hispanic']+ethnicityProfileRaw[j]
    elif (j == 'Unknown' or j == 'Patient Refused'):
        ethnicityProfile['Unkonwn/Patient Refused'] = ethnicityProfile['Unkonwn/Patient Refused']+ethnicityProfileRaw[j]
    else:
        ethnicityProfile['Hispanic'] = ethnicityProfile['Hispanic']+ethnicityProfileRaw[j]

raceProfile = {'White': 0, 'Not White': 0, 'Unknown/Patient Refused': 0}

for k in raceProfileRaw.keys():
    if k == 'White or Caucasian':
        raceProfile['White'] = raceProfile['White']+raceProfileRaw[k]
    elif (k == 'Unknown' or k == 'Patient Refused'):
        raceProfile['Unknown/Patient Refused'] = raceProfile['Unknown/Patient Refused']+raceProfileRaw[k]
    else:
        raceProfile['Not White'] = raceProfile['Not White']+raceProfileRaw[k]


# Pool features for patients

patients = cDemographics.filter(['MRN', 'AGE', 'SEX', 'RACE', 'ETHNICITY'])

ageList = []
ethnicyList = []
raceList = []

for index, row in patients.iterrows():
    ageList.append(ageBin(row['AGE']))
    ethnicyList.append(ethnicityBin(row['ETHNICITY']))
    raceList.append(raceBin(row['RACE']))

patients['AGEBIN'] = ageList
patients['RACEBIN'] = raceList
patients['ETHNICITYBIN'] = ethnicyList

encodeList = []
for index, row in patients.iterrows():
    code1 = encoder(row['SEX'], row['RACEBIN'],
                    row['ETHNICITYBIN'], row['AGEBIN'])
    code2 = code1+str(binDict[row['MRN']])
    encodeList.append(code2)

patients['CODE'] = encodeList

# Draw lists

drawing0 = patients.filter(['MRN', 'CODE'])
iaa, drawing1 = produceCohort(25, drawing0, patients)
lucas, drawing2 = produceCohort(118, drawing1, patients)
cohort1, drawing3 = produceCohort(118, drawing2, patients)
cohort2, drawing4 = produceCohort(118, drawing3, patients)
cohort3, drawing5 = produceCohort(118, drawing4, patients)
cohort4, drawing6 = produceCohort(118, drawing5, patients)
cohort5, drawing7 = produceCohort(118, drawing6, patients)
cohort6, drawing8 = produceCohort(118, drawing7, patients)
cohort7, drawing9 = produceCohort(118, drawing8, patients)
cohort8, drawing10 = produceCohort(118, drawing9, patients)

# Merge IAA with main list:

mergedCohort1 = list(iaa.append(cohort1)['MRN'])
mergedCohort2 = list(iaa.append(cohort2)['MRN'])
mergedCohort3 = list(iaa.append(cohort3)['MRN'])
mergedCohort4 = list(iaa.append(cohort4)['MRN'])
mergedCohort5 = list(iaa.append(cohort5)['MRN'])
mergedCohort6 = list(iaa.append(cohort6)['MRN'])
mergedCohort7 = list(iaa.append(cohort7)['MRN'])
mergedCohort8 = list(iaa.append(cohort8)['MRN'])
mergedCohortLucas = list(iaa.append(lucas)['MRN'])

shuffle(mergedCohort1)
shuffle(mergedCohort2)
shuffle(mergedCohort3)
shuffle(mergedCohort4)
shuffle(mergedCohort5)
shuffle(mergedCohort6)
shuffle(mergedCohort7)
shuffle(mergedCohort8)
shuffle(mergedCohortLucas)

mergedCohort1 = pd.DataFrame(mergedCohort1, columns=['MRN'])
mergedCohort2 = pd.DataFrame(mergedCohort2, columns=['MRN'])
mergedCohort3 = pd.DataFrame(mergedCohort3, columns=['MRN'])
mergedCohort4 = pd.DataFrame(mergedCohort4, columns=['MRN'])
mergedCohort5 = pd.DataFrame(mergedCohort5, columns=['MRN'])
mergedCohort6 = pd.DataFrame(mergedCohort6, columns=['MRN'])
mergedCohort7 = pd.DataFrame(mergedCohort7, columns=['MRN'])
mergedCohort8 = pd.DataFrame(mergedCohort8, columns=['MRN'])
mergedCohortLucas = pd.DataFrame(mergedCohortLucas, columns=['MRN'])


# Save cohorts to file

with pd.ExcelWriter('control3_single235_01112021.xlsx') as writer:
    cohort1.to_excel(writer, sheet_name='Cohort 1')
    cohort2.to_excel(writer, sheet_name='Cohort 2')
    cohort3.to_excel(writer, sheet_name='Cohort 3')
    cohort4.to_excel(writer, sheet_name='Cohort 4')
    cohort5.to_excel(writer, sheet_name='Cohort 5')
    cohort6.to_excel(writer, sheet_name='Cohort 6')
    cohort7.to_excel(writer, sheet_name='Cohort 7')
    cohort8.to_excel(writer, sheet_name='Cohort 8')

with pd.ExcelWriter('control2_iaa50_01112021.xlsx') as writer:
    iaa.to_excel(writer, sheet_name='Inter-rater')

with pd.ExcelWriter('control3_single235_lucas_01112021.xlsx') as writer:
    lucas.to_excel(writer, sheet_name="Lucas' set")

with pd.ExcelWriter('control3_single235_01112021_merged.xlsx') as writer:
    mergedCohort1.to_excel(writer, sheet_name='Cohort 1')
    mergedCohort2.to_excel(writer, sheet_name='Cohort 2')
    mergedCohort3.to_excel(writer, sheet_name='Cohort 3')
    mergedCohort4.to_excel(writer, sheet_name='Cohort 4')
    mergedCohort5.to_excel(writer, sheet_name='Cohort 5')
    mergedCohort6.to_excel(writer, sheet_name='Cohort 6')
    mergedCohort7.to_excel(writer, sheet_name='Cohort 7')
    mergedCohort8.to_excel(writer, sheet_name='Cohort 8')

with pd.ExcelWriter('control3_single235_lucas_01112021_merged.xlsx') as writer:
    mergedCohortLucas.to_excel(writer, sheet_name="Lucas' set")

# Save latest drawing in case of needing more cases
with pd.ExcelWriter('remainder_01112021.xlsx') as writer:
    drawing10.to_excel(writer, sheet_name='Drawing 10 remainder')
