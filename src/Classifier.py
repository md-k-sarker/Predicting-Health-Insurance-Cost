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
import time
from sklearn.neighbors.nearest_centroid import NearestCentroid

# import six
# import math
# import sklearn


def classifyUsingSVM(trainX, trainY, testX, testY):
    print('################# classifyUsingSVM() started ##################')
    start_time = time.time()
    
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

    print('################# classifyUsingSVM() finished ##################')
    print("--- %s seconds ---" % (time.time() - start_time))
    

def classifyUsingRandomForest(trainX, trainY, testX, testY):
    
    print('################# classifyUsingRandomForest() started ##################')
    start_time = time.time()
    
    clf = RandomForestClassifier(n_estimators=100,verbose=1 )
    print('classifyUsingRandomForest Initialized')
    
    clf.fit(trainX, trainY)
    print('classifyUsingRandomForest Trained')
    
    predictedY = clf.predict(testX)
    print('classifyUsingRandomForest prediction completed')
 
    accuracy = accuracy_score(testY, predictedY)
     
    confusionMatrix = confusion_matrix(testY , predictedY)
     
    f1Score = f1_score(testY, predictedY, average='weighted')
    
    print('accuracy:', accuracy) 
    print('confusionMatrix: ', confusionMatrix)
    print('f1Score: ', f1Score)
    
    print('################# classifyUsingRandomForest() finished ##################')
    print("--- %s seconds ---" % (time.time() - start_time))
 

def classifyUsingKNNCentroid(trainX, trainY, testX, testY):
    
    print('################# classifyUsingKNNCentroid() started ##################')
    start_time = time.time()
    
    clf = NearestCentroid()
    print('KNN Initialized')
    
    clf.fit(trainX, trainY)
    print('KNN Trained')
    
    predictedY = clf.predict(testX)
    print('KNN prediction completed')
 
    accuracy = accuracy_score(testY, predictedY)
     
    confusionMatrix = confusion_matrix(testY , predictedY)
     
    f1Score = f1_score(testY, predictedY, average='weighted')
    
    print('accuracy:', accuracy) 
    print('confusionMatrix: ', confusionMatrix)
    print('f1Score: ', f1Score)
    
    print('################# classifyUsingKNNCentroid() finished ##################')
    print("--- %s seconds ---" % (time.time() - start_time))
    
        


balancedDataConvertedToIntegerFile = '../processedData/balancedDataConvertedToInteger.csv'

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

X = dataIO.convertDatatoFloat(X, True)
Y = dataIO.convertDatatoFloat(Y, False)

print('Data loaded into memory')
print('np.unique(Y): ',np.sort( np.unique(Y)))

trainInputData, trainOutputVector, testInputData, testOutputVector = dataIO.splitTrainAndTestData(X, Y, .7,)

print('Data splitted into Test and Train')
print('trainInputData.shape: ',trainInputData.shape, 'trainOutputVector.shape: ', trainOutputVector.shape)

print('np.unique(trainOutputVector): ',np.sort(np.unique(trainOutputVector)))


classifyUsingKNNCentroid(trainInputData, trainOutputVector, testInputData, testOutputVector)
# 
classifyUsingRandomForest(trainInputData, trainOutputVector, testInputData, testOutputVector)

classifyUsingSVM(trainInputData, trainOutputVector, testInputData, testOutputVector)