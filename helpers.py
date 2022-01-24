# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:35:14 2020

@author: hwz62
"""
import pandas as pd
from math import log, exp
from raICD import exact, startsw
from random import choices
from random import shuffle

def containsICD(icdList):
    icdCount = 0
    for code in exact:
        if code in icdList:
            icdCount += sum([code == s for s in icdList])
        else:
            continue
    for c in startsw:
        if any(s.startswith(c) for s in icdList):
            icdCount += sum([s.startswith(c) for s in icdList])
        else:
            continue
    return icdCount


def countAllICD(mrn, problemList, diagnoses):
    plICD = list(problemList[problemList['MRN'] == mrn]['ICD_CODE'])
    dxICD = list(diagnoses[diagnoses['MRN'] == mrn]['ICD_CODE'])
    totalCounts = containsICD(plICD)+containsICD(dxICD)
    return totalCounts


def countDXICD(mrn, diagnoses):
    dxICD = list(diagnoses[diagnoses['MRN'] == mrn]['ICD_CODE'])
    totalCounts = containsICD(dxICD)
    return totalCounts


def harvard(mrn, demographics, diagnoses):
    ICDcounts = countDXICD(mrn, diagnoses)
    lupus = demographics[demographics['MRN']==mrn]['LUPUS_CNT'].notna().bool()
    if lupus == True:
        lupusCt = int(demographics[demographics['MRN']==mrn]['LUPUS_CNT'])
    else:
        lupusCt = 0
    psoriatic = demographics[demographics['MRN']==mrn]['PSORIATICARTHRO_CNT'].notna().bool()
    if psoriatic == True:
        psoriaticCt = int(demographics[demographics['MRN']==mrn]['PSORIATICARTHRO_CNT'])
    else:
        psoriaticCt = 0
    lab = demographics[demographics['MRN']==mrn]['LAB_RF'].notna().bool()
    if (lab == True) and (float(demographics[demographics['MRN']==mrn]['LAB_RF']) > 0):
        labCt = 1
    else:
        labCt = 0
    dxent = demographics[demographics['MRN']==mrn]['PATIENT_DXENCT'].notna().bool()
    if dxent == True:
        dxentCt = int(demographics[demographics['MRN']==mrn]['PATIENT_DXENCT'])
    else:
        dxentCt = 0
    sum_beta = 1.937*log(1+ICDcounts)-0.529*log(1+lupusCt)-0.122*log(1+psoriaticCt)+1.639*labCt-0.954*log(1+dxentCt)
    value = exp(-1.017 + sum_beta)/(1 + exp(-1.017 + sum_beta))
    return value


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


def loadClinData():
    casesDemographics = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\demographics2.csv')
    casesDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
    controlDemographics = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')
    controlDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_DX.txt', sep='|', header=0)
    casesDemographics = casesDemographics[casesDemographics['RA_ENC_CNT'].notna()]
    undesiredColumns = ['CONDITION', 'SEX_1', 'RACE_1', 'ETHNICITY_1']
    controlDemographics2 = controlDemographics.drop(undesiredColumns, axis=1)
    demographics = pd.concat([casesDemographics, controlDemographics2])
    demo2 = demographics.set_index('MRN')
    diagnoses = pd.concat([casesDiagnoses, controlDiagnoses])
    diag2 = diagnoses.set_index('MRN')
    return demographics, demo2, diagnoses, diag2