# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:52:12 2021

@author: hwz62
"""

import pandas as pd
from random import shuffle
from helpers import countDXICD

casesIAA = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set2_iaa50_09252020.xlsx', engine='openpyxl')
controlIAA = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\control2_iaa25_01112021.xlsx', engine='openpyxl')
lucasCases = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\set3_single285_lucas_11132020_merged.xlsx', engine='openpyxl')
lucasControls = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\lucas_controls_01142021_nopw.xlsx', engine='openpyxl')

casesIAAlist = list(casesIAA.MRN)
controlIAAlist = list(controlIAA.MRN)
lucasCaseslist = list(lucasCases.MRN)
lucasControlslist = list(lucasControls.MRN)


#Which ones have Lucas already done?
lucasCasesDone = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-LucasCases_DATA_2021-01-30_1112.csv')
lucasControlsDone = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\amia300\\RAIdentification-LucasControls_DATA_2021-01-30_1108.csv')
lucasCasesDonelist = list(lucasCasesDone.mrn)
lucasControlsDonelist = list(lucasControlsDone.mrn)

lucasAlreadyDoneCases = [x for x in lucasCaseslist if x in lucasCasesDonelist]
lucasAlreadyDoneControls = [x for x in lucasControlslist if x in lucasControlsDonelist]
lucasAlreadyDonecasesIAA = [x for x in casesIAAlist if x in lucasCasesDonelist]
lucasAlreadyDonecontrolsIAA = [x for x in controlIAAlist if x in lucasControlsDonelist]

#CaseControlOverlap = [x for x in lucasCaseslist if x in lucasControlslist] check overlap between cases and controls

lucasRemainderCases = [x for x in lucasCaseslist if x not in lucasCasesDonelist]
lucasRemainderControls = [x for x in lucasControlslist if x not in lucasControlsDonelist]

lucasCasesnoIAA = [x for x in lucasCaseslist if x not in casesIAAlist]
lucasControlsnoIAA = [x for x in lucasControlslist if x not in controlIAAlist]

#components of final list for 300
halfCasesIAA = casesIAAlist[0:25]
combinedList = [halfCasesIAA,controlIAAlist,lucasCasesnoIAA[0:118],lucasControlsnoIAA]
totalList = [item for sublist in combinedList for item in sublist]


#top off to 300
casesDf = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\remainder_cases_09252020.xlsx', engine='openpyxl')
controlDf = pd.read_excel('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\lists 01-11-2021\\remainder_control_01112021.xlsx', engine='openpyxl')

casesList = list(casesDf.MRN)
controlList= list(controlDf.MRN)

shuffle(casesList)
shuffle(controlList)

cases7 = casesList[0:7]
control7= controlList[0:7]

#check if 7 cases or 7 controls in existing list
#[x for x in cases7 if x in totalList]
#[x for x in control7 if x in totalList]

combinedList2 = [totalList,cases7,control7]
totalList2 = [item for sublist in combinedList2 for item in sublist]
shuffle(totalList2)


casesDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\demographics2.csv')
casesDiagnoses = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\code\\Ranganath_DX_090820.txt', sep='","', header=0)
controlDemographics = pd.read_csv('C:\\Users\\hwz62\\Dropbox\\~Grad School\\Rheumatoid Arthritis\\controls\\Rang_Bui_Controls_Main.csv')

casesDemographics = casesDemographics[casesDemographics['RA_ENC_CNT'].notna()]

undesiredColumns = ['CONDITION', 'SEX_1', 'RACE_1', 'ETHNICITY_1']
controlDemographics2 = controlDemographics.drop(undesiredColumns, axis=1)
allDemographics = pd.concat([casesDemographics, controlDemographics2])
allDemographics2=allDemographics.set_index('MRN')

casesMRN = list(casesDemographics.MRN)
controlMRN = list(controlDemographics.MRN)
allMRN = list(allDemographics.MRN)
mrnOverlap = [x for x in controlMRN if x in casesMRN]

for i in mrnOverlap:
    allDemographics.drop(allDemographics[allDemographics['MRN']==i].index, inplace = True)
allDemographics2=allDemographics.set_index('MRN')

#Where are the overlap MRN's?
[x for x in halfCasesIAA if x in mrnOverlap]
a = [x for x in controlIAAlist if x in mrnOverlap]
controlIAAlist.remove(a)
[x for x in lucasCasesnoIAA[0:118] if x in mrnOverlap]
b = [x for x in lucasControlsnoIAA if x in mrnOverlap]
for i in b:
    lucasControlsnoIAA.remove(i)

# 3602728 in controlIAAlist and mrnOverlap, pulled from lucasControlslist 
# [1764522, 1956002, 3495761, 3883325, 4161226, 4354754] in lucasControlsnoIAA and mrnOverlap
# [5832589,5433171,5864774,2077969,4726136,2212130]

#controlIAAlist.append(3602728)
for j in [5832589,5433171,5864774,2077969,4726136,2212130,2014152]:
    lucasControlsnoIAA.append(j)

#check if cases have >1 RA diagnosis:
[countDXICD(i,casesDiagnoses) for i in halfCasesIAA]
foo = [countDXICD(i,casesDiagnoses) for i in lucasCasesnoIAA[0:118]]

partLucasCasesNoIAA = lucasCasesnoIAA[0:118]
#can't find MRN 2369077, replaced with 2342299
partLucasCasesNoIAA.remove(2369077)
partLucasCasesNoIAA.append(2342299)



# split the set evenly among six reviewers. Each reviewer will get 6 as IAA,
# leaving 294 split into 6x49. Add the 6 IAA = 55 per reviewer.
shuffle(halfCasesIAA)
shuffle(controlIAAlist)
shuffle(partLucasCasesNoIAA)
shuffle(lucasControlsnoIAA)

sixIAAt = [halfCasesIAA[0:3],controlIAAlist[0:3]]
sixIAA = [item for sublist in sixIAAt for item in sublist]

remainingCasest = [halfCasesIAA[3:], partLucasCasesNoIAA, cases7]
remainingCases = [item for sublist in remainingCasest for item in sublist]
remainingControlst = [controlIAAlist[3:], lucasControlsnoIAA, control7]
remainingControls = [item for sublist in remainingControlst for item in sublist]

shuffle(sixIAA)
shuffle(remainingCases)
shuffle(remainingControls)

#make alternating cases/control master list
remainderMaster = []
for j in range(147):
    remainderMaster.append(remainingCases[j])
    remainderMaster.append(remainingControls[j])

#each list has 6 
list1t = [sixIAA, remainderMaster[49*0:49*1]]
list2t = [sixIAA, remainderMaster[49*1:49*2]]
list3t = [sixIAA, remainderMaster[49*2:49*3]]
list4t = [sixIAA, remainderMaster[49*3:49*4]]
list5t = [sixIAA, remainderMaster[49*4:49*5]]
list6t = [sixIAA, remainderMaster[49*5:49*6]]
list1=[item for sublist in list1t for item in sublist]
list2=[item for sublist in list2t for item in sublist]
list3=[item for sublist in list3t for item in sublist]
list4=[item for sublist in list4t for item in sublist]
list5=[item for sublist in list5t for item in sublist]
list6=[item for sublist in list6t for item in sublist]

shuffle(list1)
shuffle(list2)
shuffle(list3)
shuffle(list4)
shuffle(list5)
shuffle(list6)

combinedList = [halfCasesIAA,controlIAAlist,partLucasCasesNoIAA,lucasControlsnoIAA]
totalList = [item for sublist in combinedList for item in sublist]
combinedList2 = [totalList,cases7,control7]
totalList2 = [item for sublist in combinedList2 for item in sublist]


list1CCP = [allDemographics2.loc[i].HIGHEST_CCP for i in list1]
list2CCP = [allDemographics2.loc[i].HIGHEST_CCP for i in list2]
list3CCP = [allDemographics2.loc[i].HIGHEST_CCP for i in list3]
list4CCP = [allDemographics2.loc[i].HIGHEST_CCP for i in list4]
list5CCP = [allDemographics2.loc[i].HIGHEST_CCP for i in list5]
list6CCP = [allDemographics2.loc[i].HIGHEST_CCP for i in list6]
listLucasCCP = [allDemographics2.loc[i].HIGHEST_CCP for i in totalList2]

list1df = pd.DataFrame({'MRN': list1, 'Highest CCP': list1CCP})
list2df = pd.DataFrame({'MRN': list2, 'Highest CCP': list2CCP})
list3df = pd.DataFrame({'MRN': list3, 'Highest CCP': list3CCP})
list4df = pd.DataFrame({'MRN': list4, 'Highest CCP': list4CCP})
list5df = pd.DataFrame({'MRN': list5, 'Highest CCP': list5CCP})
list6df = pd.DataFrame({'MRN': list6, 'Highest CCP': list6CCP})
listLucasdf = pd.DataFrame({'MRN': totalList2, 'Highest CCP': listLucasCCP})

with pd.ExcelWriter('first300list1_013121.xlsx') as writer:
    list1df.to_excel(writer, sheet_name="List 1")
with pd.ExcelWriter('first300list2_013121.xlsx') as writer:
    list2df.to_excel(writer, sheet_name="List 2")
with pd.ExcelWriter('first300list3_013121.xlsx') as writer:
    list3df.to_excel(writer, sheet_name="List 3")
with pd.ExcelWriter('first300list4_013121.xlsx') as writer:
    list4df.to_excel(writer, sheet_name="List 4")
with pd.ExcelWriter('first300list5_013121.xlsx') as writer:
    list5df.to_excel(writer, sheet_name="List 5")
with pd.ExcelWriter('first300list6_013121.xlsx') as writer:
    list6df.to_excel(writer, sheet_name="List 6")
with pd.ExcelWriter('first300Lucas_013121.xlsx') as writer:
    listLucasdf.to_excel(writer, sheet_name="Lucas' Set")