#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 22:39:28 2021

@author: shrohanmohapatra
"""
from dataDictionary import dataDict
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
xdata1, xdata2, ydata = [], [], []
for i in range(36):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata1, xdata2, ydata)
ax.set_xlabel('Re')
ax.set_ylabel('r0/a')
ax.set_zlabel('Force')
