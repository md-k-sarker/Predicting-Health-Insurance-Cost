'''
Created on Dec 3, 2016

@author: sarker
'''

import csv
import numpy as np
from matplotlib import colors


'''
return hatch for barplot
'''
def getHatches():
    return ['-', '+', 'x', '\\', '*', 'o', 'O', '.']

'''return colorNames for all available color in matplolib'''
def getColorNames():
    
    colorNames = []
    for color in colors.cnames:    
        colorNames.append(color)
    
    return colorNames

    