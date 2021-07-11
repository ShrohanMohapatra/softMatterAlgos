#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:01:57 2021

@author: shrohanmohapatra
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from math import log
def parser(stringVar):
    if stringVar[len(stringVar)-1] == '\n':
        if stringVar[0] == '-':
            return (-1)*float(
                ''.join([stringVar[k] for k in range(1,len(stringVar)-1)])
                )
        else:
            return float(
                ''.join([stringVar[k] for k in range(len(stringVar)-1)])
                )
    elif stringVar[0] == '-':
        return (-1)*float(
            ''.join([stringVar[k] for k in range(1,len(stringVar))])
            )
    else:
        return float(
                ''.join([stringVar[k] for k in range(len(stringVar))])
                )
fileOpen = open('pressureFieldTutorial.csv')
xAxis, yAxis, zAxis = [], [], []
counter = 0
for lines in fileOpen.readlines():
    if counter == 0:
        counter = counter + 1
        continue
    extractor = lines.split(',')
    xAxis.append(parser(extractor[0]))
    yAxis.append(parser(extractor[1]))
    zAxis.append(abs(parser(extractor[3])))
pav = sum(zAxis)/len(zAxis)
xData = np.array([xAxis[k] for k in range(len(xAxis))])
yData = np.array([yAxis[k] for k in range(len(yAxis))])
zData = np.array([log((zAxis[k]+0.01)/pav) for k in range(len(zAxis))])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xData, yData, zData)
ax.set_xlabel('x (in m)')
ax.set_ylabel('y (in m)')
ax.set_zlabel('log(p/pav) (Average pressure = pav)')
ax.set_title('3D contour')
plt.show()


