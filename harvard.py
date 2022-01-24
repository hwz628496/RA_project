# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:07:50 2020

@author: hwz62
"""

import pandas as pd
from math import log, exp
from raICD import exact, startsw

problemList = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\problemList.csv')
diagnoses = pd.read_csv('Ranganath_DX_090820.txt', sep='","', header=0)
demographics = pd.read_csv('C:\\Users\\hwz62\\Documents\\HIPAA Backup\\Rheumatoid Arthritis\\demographics2.csv')


def containsICDbad(icdList):
    icdCount = 0
    for code in exact:
        if code in icdList:
            icdCount += 1
        else:
            continue
    for c in startsw:
        if any(s.startswith(c) for s in icdList):
            icdCount += 1
        else:
            continue
    return icdCount

def containsICD(icdList):
    icdCount = 0
    for icdItem in icdList:
        for code in exact:
            if code == icdItem:
                icdCount += 1
            else:
                continue
        for c in startsw:
            if icdItem.startswith(c):
                icdCount += 1
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

