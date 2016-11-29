'''
Created on Nov 16, 2016

@author: sarker
'''

import os
import numpy as np
import ManipulateData as mpd
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
import re


'''
Column Names
Id    ResidentStatus    Education1989Revision    Education2003Revision    EducationReportingFlag    MonthOfDeath    Sex    AgeType    Age    AgeSubstitutionFlag    AgeRecode52    AgeRecode27    AgeRecode12    InfantAgeRecode22    PlaceOfDeathAndDecedentsStatus    MaritalStatus    DayOfWeekOfDeath    CurrentDataYear    InjuryAtWork    MannerOfDeath    MethodOfDisposition    Autopsy    ActivityCode    PlaceOfInjury    Icd10Code    CauseRecode358    CauseRecode113    InfantCauseRecode130    CauseRecode39    NumberOfEntityAxisConditions    NumberOfRecordAxisConditions    Race    BridgedRaceFlag    RaceImputationFlag    RaceRecode3    RaceRecode5    HispanicOrigin    HispanicOriginRaceRecode
''' 

'''
This method returns only those data-sample which has diesease. As mentioned in https://en.wikipedia.org/wiki/ICD-10#List
This method also write the data-samples into files.
'''
def getOnlyDiseaseData(inputFileName, outputFileName):

    dataMatrixWithLabel = mpd.getDataMatrixFromCSV(inputFileName)
    
    '''ICD10Code = column 24'''
    icd10Codes = dataMatrixWithLabel[:, 24]
    
    dataMatrixWithOnlyDieseases = [];
    
    '''pattern to match'''
    pattern = re.compile('[A-R]+')
    
    counter = 0
    
    '''write to file''' 
    with open(outputFileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for icd10Code in icd10Codes:
            if(re.match(pattern, icd10Code)):
                dataMatrixWithOnlyDieseases.append(dataMatrixWithLabel[counter])
                writer.writerow(dataMatrixWithLabel[counter])
            counter += 1
            
    
    dataMatrixWithOnlyDieseases = np.array(dataMatrixWithOnlyDieseases)
    return dataMatrixWithOnlyDieseases 


'''This method maps the string value to integer values'''
def changeStringToInteger(fileName, cols, hasColumnHeader):
    dataMatrixWithLabel = mpd.getDataMatrixFromCSV(fileName)
    
    '''remove the column_Header/label_of_the_column from the data'''
    if(hasColumnHeader):
        dataMatrix = dataMatrixWithLabel[1:]
    
    for i in cols:
        
        '''Column 5 = Sex: 
        F = 0
        M = 1
        '''
        if(i == 6):
            c6 = []
            for rowData in dataMatrix[:, i]:
                if(rowData == 'F'):
                    c6.append(0)
                else:
                    c6.append(1)
                    
        '''Column 15 = Marital Status
        S  =  Never married, single  = 0
        M  =  Married                = 1
        W  =  Widowed                = 2
        D  =  Divorced               = 3
        U  =  Marital Status unknown = 4'''
        if(i == 15):
            c15 = []
            for rowData in dataMatrix[:, i]:
                if(rowData == 'S'):
                    c15.append(0)
                elif(rowData == 'M'):
                    c15.append(1)
                elif(rowData == 'W'):
                    c15.append(2)
                elif(rowData == 'D'):
                    c15.append(3)
                elif(rowData == 'U'):
                    c15.append(4)
                    
        '''Column 18 = InjuryAtWork
        Y  =  Yes          = 0
        N  =  No           = 1
        U  =  Unknown      = 2'''
        if(i == 18):
            c18 = []
            for rowData in dataMatrix[:, i]:
                if(rowData == 'Y'):
                    c18.append(0)
                elif(rowData == 'N'):
                    c18.append(1)
                elif(rowData == 'U'):
                    c18.append(2)
                    
        '''Column 20 = Method Of Desposition
        B  =  Burial          = 0
        C  =  Cremation      = 1
        O  =  Other          = 2
        U  = Unknown         = 3
        E  = Unknown         = 3
        R  = Unknown         = 3'''
        if(i == 20):
            c20 = []
            for rowData in dataMatrix[:, i]:
                if(rowData == 'B'):
                    c20.append(0)
                elif(rowData == 'C'):
                    c20.append(1)
                elif(rowData == 'O'):
                    c20.append(2)
                elif(rowData == 'U'):
                    c20.append(3)
                elif(rowData == 'E'):
                    c20.append(3)
                elif(rowData == 'R'):
                    c20.append(3)
                else:
                    c20.append(3)
                    
        
        '''Column 21 = Autopsy: 
        Y = Yes     = 0
        N = No      = 1
        U = Unknown = 2
        '''            
        if(i == 21):
            c21 = []
            for rowData in dataMatrix[:, i]:
                if(rowData == 'Y'):
                    c21.append(0)
                elif(rowData == 'N'):
                    c21.append(1)
                elif(rowData == 'U'):
                    c21.append(2)
                else:
                    c21.append(2)
         
    
    '''replace the values into main matirx'''        
    dataMatrix[:, 6] = c6
    dataMatrix[:, 15] = c15
    dataMatrix[:, 18] = c18
    dataMatrix[:, 20] = c20
    dataMatrix[:, 21] = c21
    
    return dataMatrix

'''change output variable ICD10 codes into integer values
Explanantion: https://en.wikipedia.org/wiki/ICD-10#List
'''        

def mapICD10CodetoInteger(ICD10Codes):
    
    integerCodes = []
    for icd10Code in ICD10Codes:
        if(icd10Code.startswith('A') or icd10Code.startswith('B')):
            integerCodes.append(0)
        elif(icd10Code.startswith('C') or icd10Code.startswith('D0') or icd10Code.startswith('D1') or icd10Code.startswith('D2') or icd10Code.startswith('D3') or icd10Code.startswith('D4')):
            integerCodes.append(1)
        elif(icd10Code.startswith('D5') or icd10Code.startswith('D6') or icd10Code.startswith('D7') or icd10Code.startswith('D8')):
            integerCodes.append(2)
        elif(icd10Code.startswith('E')):
            integerCodes.append(3)
        elif(icd10Code.startswith('F')):
            integerCodes.append(4)
        elif(icd10Code.startswith('G')):
            integerCodes.append(5)
        elif(icd10Code.startswith('H0') or icd10Code.startswith('H1') or icd10Code.startswith('H2') or icd10Code.startswith('H3') or icd10Code.startswith('H4') or icd10Code.startswith('H5')):
            integerCodes.append(6)
        elif(icd10Code.startswith('H6') or icd10Code.startswith('H7') or icd10Code.startswith('H8') or icd10Code.startswith('H9')):
            integerCodes.append(7)
        elif(icd10Code.startswith('I')):
            integerCodes.append(8)
        elif(icd10Code.startswith('J')):
            integerCodes.append(9)
        elif(icd10Code.startswith('K')):
            integerCodes.append(10)
        elif(icd10Code.startswith('L')):
            integerCodes.append(11)
        elif(icd10Code.startswith('M')):
            integerCodes.append(12)
        elif(icd10Code.startswith('N')):
            integerCodes.append(13)
        elif(icd10Code.startswith('O') or icd10Code.startswith('0')):
            integerCodes.append(14)
        elif(icd10Code.startswith('P')):
            integerCodes.append(15)
        elif(icd10Code.startswith('Q')):
            integerCodes.append(16)
        elif(icd10Code.startswith('R')):
            integerCodes.append(17)
        else:
            print(icd10Code)
    
    return integerCodes


'''Be sure about where you has the file and where you want to put the resultant file'''
actualDataFile = '../data/DeathRecords/DeathRecords.csv'
deathRecordsOnlyDiseaseFile = '../processedData/DeathRecordsOnlyDisease.csv'
deathRecordsConvertedToIntegerFile = '../processedData/DeathRecordsConvertedToInteger.csv'

'''Get and Write only diesease data samples'''
# getOnlyDiseaseData(actualDataFile, deathRecordsOnlyDiseaseFile)

'''transform the data into integer format. only the input features.'''
cols = [6, 15, 18, 20, 21]
dataMatrix = changeStringToInteger(deathRecordsOnlyDiseaseFile , cols , True) 
 
'''change the output or icd10codes'''                
dataMatrix[ : , 24] = mapICD10CodetoInteger(dataMatrix[:, 24])

'''write the converted values to file'''
with open(deathRecordsConvertedToIntegerFile, 'w') as csvfile:
    writer = csv.writer(csvfile , delimiter=',')
    for row in dataMatrix:
        writer.writerow(row)    
       

# 
# # #Manner of Death, column 19 
# '''take death of manner as output value'''
# Y = dataMatrix[:, 16]
# 
# '''take inputs upto 31. after 31 the values are not convertible to float'''
# X =  dataMatrix[: , range(0 , 6) ] 
# '''delete column 19. i.e delete deathManner column from input'''
# #X = np.delete(dataMatrix, [0, 16], axis=1)
# 
# 
# '''convert to float'''
# X = mpd.convertDatatoFloat(X)
# Y = mpd.convertDatatoFloat(Y)
# 
# 
# '''Split into train, test and validation'''
# trainX, trainY, validationX, validationY, testX, testY = mpd.splitTrainValidateAndTestData(X, Y, 0.6, 0.2, 0.2)
# 
# print(trainX.shape, trainY.shape)
# 
# clf = MLPClassifier()
# 
# clf.fit(trainX, trainY)
# 
# predictedY = clf.predict(testX)
# 
# accuracy = accuracy_score(testY, predictedY)
# 
# confusionMatrix = confusion_matrix(testY , predictedY)
# 
# f1Score = f1_score(testY, predictedY, average='weighted')
# 
# print('confusionMatrix: ', confusionMatrix)
# print('f1Score: ', f1Score)
# 
# 
#         
#         
#     
