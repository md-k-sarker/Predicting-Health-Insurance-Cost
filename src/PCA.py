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



fileName = '../processedData/DeathRecordsConvertedToInteger.csv' 
dataMatrix = mpd.getDataMatrixFromCSV(fileName)

'''get ICD10 code as output'''
Y = dataMatrix[:,24]

'''remove OutputCoulumn and Id Column'''
X = np.delete(dataMatrix, [0,24], axis = 1)

X = mpd.convertDatatoFloat(X)

pca = decomposition.PCA(n_components=3)
pca.fit(X)
print(X) 
X = pca.transform(X)
print(X) 

