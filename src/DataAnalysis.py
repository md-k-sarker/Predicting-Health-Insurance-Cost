'''
Created on Nov 28, 2016

@author: sarker
'''

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
from sklearn import feature_selection
from sklearn.feature_selection import f_classif
import matplotlib.pyplot as plt
from matplotlib import colors
import six
import math
import sklearn
import matplotlib.pyplot as plt



def featuresFromPCA(X):
    pca = decomposition.PCA(n_components=3)
    pca.fit(X)
    print(X) 
    X = pca.transform(X)
    print(X) 
 
def getColorNames():
    
    colorNames = []
    for color in colors.cnames:    
        colorNames.append(color)
    
    return colorNames
    
        
def featuresFromFeatureSelection(X,Y,columnNames):
    
    for f in columnNames:
        print(f)
    X_new_withfitTransform = SelectKBest(chi2, k=34).fit(X, Y)
    colors = getColorNames()
    counter  = 0
    
    scores = X_new_withfitTransform.scores_
    scores_scaled = np.divide(scores, 1000) 
        
    for score in scores_scaled:
        #if(score > 10):
        #print('Feature {:>34}'.format(columnNames[counter]))
        print('{:>34}  '.format( score))
        '''Plot a graph'''    
        plt.bar(counter, score,color=colors[counter])
        counter +=1 

    plt.ylabel('Scores(1k)')
    plt.title('Scores calculated by Chi-Square Test')
    plt.legend(columnNames, bbox_to_anchor=(0., 0.8, 1., .102), loc=3,ncol=5, mode="expand", borderaxespad=0.)
    plt.show()
    
    #print(feature_selection.chi2(X,Y))
        


def loadData():
    print('##############loadData()###############')
    #fileName = '../processedData/1000Records.csv' 
    fileName = '../processedData/DeathRecordsConvertedToInteger.csv'
    
    dataMatrix = dataIO.getDataMatrixFromCSV(fileName)
    
    '''remove the column_Header/label_of_the_column from the data'''
    columnNames = dataMatrix[0:1]
    
    dataMatrix = dataMatrix[1:]
    
    
    '''get ICD10 code as output'''
    Y = dataMatrix[:,24]
    Y = dataIO.convertDatatoFloat(Y,False)
    print('Conversion to float completed')
    
    '''remove OutputCoulumn and 
    Those below mentioned columns:
    Id
    NumberOfEntityAxisConditions
    NumberOfRecordAxisConditions'''
    X = np.delete(dataMatrix, [0,24,29,30], axis = 1)
    columnNames = np.delete(columnNames, [0,24,29,30])
    
    X = dataIO.convertDatatoFloat(X, True)
    print('##############loadData() completed###############')
    return X, Y, columnNames



def plotClassImbalance(Y):
    '''plot the output data'''
    
    print('Start counting')
    frequency = np.bincount(Y)
    
    frequency = np.divide(frequency, 1000) # frequency /= 1000
    
    print('Counting finished')
    
    #fig = plt.figure()
    plt.bar(range(len(frequency)),frequency)
    plt.xlabel('Classes')
    plt.ylabel('No. of Samples(1K)')
    plt.title('No. of Samples for each class')
    
    
    print('Figure configuration completed')
    np.sort(frequency)
    for f in frequency:
        print(f)
    plt.show( )
    
    print('Figure display completed')


def plotScatterPlotFor18Classes(Y,featureN):
    print('##############plotScatterPlotFor18Classes()###############')
#     fileChi_Square_Values = '../results/Chi_SquareValuesfor_All_Features.csv'
#     
#     featuresWithScore = np.array(list(csv.reader(open(fileChi_Square_Values, "r+"), delimiter=','))) 
#     
#     for row in featuresWithScore:
#         print('row: ', row[0], '  ', row[1])
    
    print('Figure configuration started') 
    colors = getColorNames()
    counter = 0
    for x,y in zip(featureN,Y):    
        plt.scatter(x,y,color=colors[int(y)])
        counter +=1       
        print(counter)
         
    plt.xlabel('InfantCauseRecode130')
    plt.ylabel('Classes')
    plt.title('InfantCauseRecode130 vs different classes')
         
    print('Figure configuration completed')

    plt.show()
        

def getFeatureN(X,columnNames):
    print('##############getFeature()###############')
    counter = 0
    index = -1
    for c in columnNames:
        if(c == 'InfantCauseRecode130'):
            index = counter
            break
        
        counter +=1
    print('##############getFeatureN() completed###############')
    return X[:,index]

#plotScatterPlot()
X, Y, columnNames = loadData()

featureN = getFeatureN(X, columnNames)

plotScatterPlotFor18Classes(Y, featureN)

#featuresFromFeatureSelection(X, Y, columnNames)

