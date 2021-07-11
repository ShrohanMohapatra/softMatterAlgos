#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 22:34:29 2021

@author: shrohanmohapatra
"""
import numpy as np
import matplotlib.pyplot as plt
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
fileOpen = open('velocityFieldTutorial.csv')
xAxis, yAxis, uData, vData = [], [], [], []
counter = 0
for lines in fileOpen.readlines():
    if counter == 0:
        counter = counter + 1
        continue
    extractor = lines.split(',')
    xAxis.append(parser(extractor[0]))
    yAxis.append(parser(extractor[1]))
    uData.append(parser(extractor[3]))
    vData.append(parser(extractor[4]))

xData = np.array([xAxis[k] for k in range(len(xAxis))])
yData = np.array([yAxis[k] for k in range(len(yAxis))])
uData = np.array([uData[k] for k in range(len(uData))])
vData = np.array([vData[k] for k in range(len(uData))])
fig = plt.figure()
plt.quiver(xData, yData, uData, vData, color='g')
plt.title('Velocity Field')
plt.xlabel('x (in m)')
plt.ylabel('y (in m)')
plt.show()


