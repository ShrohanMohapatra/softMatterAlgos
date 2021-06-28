#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:24:08 2021
@author: shrohanmohapatra
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fileReader = open('TerminalDataForLaminar')
xPointers, yPointers, zPointers = [], [], []
for lines in fileReader.readlines():
    extraction = lines.split(' ')
    xPointers.append(float((extraction[0].split('='))[1]))
    yPointers.append(float((extraction[1].split('='))[1]))
    zPointers.append(float((extraction[2].split('='))[1]))
xPlot = np.array(xPointers)
yPlot = np.array(yPointers)
zPlot = np.array(zPointers)
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection='3d')
ax.plot_trisurf(xPlot,yPlot,zPlot)
ax.set_xlabel('Re')
ax.set_xlim(0.0, 0.25)
ax.set_ylabel('r0/a')
ax.set_ylim(0.0, 1.0)
ax.set_zlabel('Fint/(mu*U)')
ax.set_zlim(np.min(zPlot), np.max(zPlot))
ax.set_title('Force per unit length with Re and r0/a')
plt.show()


