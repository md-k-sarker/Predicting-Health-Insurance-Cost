'''
Created on Nov 29, 2016

@author: sarker
'''

from sklearn import svm
from sklearn import decomposition
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import numpy as np
import DataIOFactory as dataIO
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
import re
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn import feature_selection
from sklearn.feature_selection import f_classif
import matplotlib.pyplot as plt
from matplotlib import colors

# import six
# import math
# import sklearn


def classifyUsingSVM(trainX, trainY, testX, testY):
    
    print('SVM called')
    clf = svm.SVC(kernel='rbf')
    print('SVM Initialized')
    
    clf.fit(trainX, trainY)
    print('SVM Trained')
    
    predictedY = clf.predict(testX)
    print('SVM prediction completed')
 
    accuracy = accuracy_score(testY, predictedY)
     
    confusionMatrix = confusion_matrix(testY , predictedY)
     
    f1Score = f1_score(testY, predictedY, average='weighted')
    
    print('accuracy:', accuracy) 
    print('confusionMatrix: ', confusionMatrix)
    print('f1Score: ', f1Score)


def classifyUsingRandomForest(trainX, trainY, testX, testY):
    
    print('SVM called')
    clf = svm.SVC(kernel='rbf')
    print('SVM Initialized')
    
    clf.fit(trainX, trainY)
    print('SVM Trained')
    
    predictedY = clf.predict(testX)
    print('SVM prediction completed')
 
    accuracy = accuracy_score(testY, predictedY)
     
    confusionMatrix = confusion_matrix(testY , predictedY)
     
    f1Score = f1_score(testY, predictedY, average='weighted')
    
    print('accuracy:', accuracy) 
    print('confusionMatrix: ', confusionMatrix)
    print('f1Score: ', f1Score)


fileName = '../processedData/DeathRecordsConvertedToInteger.csv' 
dataMatrix = dataIO.getDataMatrixFromCSV(fileName)

'''remove the column_Header/label_of_the_column from the data'''
columnNames = dataMatrix[0:1]
dataMatrix = dataMatrix[1:]

'''shuffle data'''
dataIO.shuffleData(dataMatrix)

'''get ICD10 code as output'''
Y = dataMatrix[:, 24]

'''remove OutputCoulumn and 
Those below mentioned columns:
Id
NumberOfEntityAxisConditions
NumberOfRecordAxisConditions'''
X = np.delete(dataMatrix, [0, 24, 29, 30], axis=1)
columnNames = np.delete(columnNames, [0, 24, 29, 30])

X = dataIO.convertDatatoFloat(X)

print('Data loaded into memory')

trainInputData, trainOutputVector, validationInputData, validationOutputVector, \
    testInputData, testOutputVector = dataIO.splitTrainValidateAndTestData(X, Y, .6, .2, .2)

print('Data splitted into Test and Train')

classifyUsingSVM(trainInputData,trainOutputVector,testInputData,testOutputVector)
