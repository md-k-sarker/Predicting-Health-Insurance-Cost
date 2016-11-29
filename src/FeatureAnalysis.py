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
import ManipulateData as mpd
import csv
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
import re
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
import matplotlib.pyplot as plt
from matplotlib import colors
import six
import math



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

    X_new_withfitTransform = SelectKBest(chi2, k=34).fit(X, Y)

    colors = getColorNames()
    counter  = 0
        
    for score in X_new_withfitTransform.scores_:
        if(score > 10):
            print('{:>34}'.format( columnNames[counter]))
            print('{:>34}  '.format( score))
        '''Plot a graph'''    
        plt.bar(counter, score,color=colors[counter])
        counter +=1 

    plt.ylabel('Scores')
    plt.title('Scores calculated by Chi-Test')
    plt.legend(columnNames, bbox_to_anchor=(0., 0.8, 1., .102), loc=3,ncol=5, mode="expand", borderaxespad=0.)
    plt.show()
        


#fileName = '../processedData/1000Records.csv' 

fileName = '../processedData/DeathRecordsConvertedToInteger.csv' 
dataMatrix = mpd.getDataMatrixFromCSV(fileName)

'''remove the column_Header/label_of_the_column from the data'''
columnNames = dataMatrix[0:1]
dataMatrix = dataMatrix[1:]


'''get ICD10 code as output'''
Y = dataMatrix[:,24]

'''remove OutputCoulumn and 
Those below mentioned columns:
Id
NumberOfEntityAxisConditions
NumberOfRecordAxisConditions'''
X = np.delete(dataMatrix, [0,24,29,30], axis = 1)
columnNames = np.delete(columnNames, [0,24,29,30])

X = mpd.convertDatatoFloat(X)

featuresFromFeatureSelection(X, Y,columnNames)

