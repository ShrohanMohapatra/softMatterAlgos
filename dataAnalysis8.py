#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 22:59:58 2021

@author: shrohanmohapatra
"""

from dataDictionary import dataDict
import numpy as np
from scipy.optimize import curve_fit
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
def modelPolyLaw(x,q1,q2,q3,q4,p0,p1,p2,p3):
    Re = x[0]
    ka = x[1]
    return p0+p1*(Re**q1)+p2*(ka**q2)+p3*(Re**q3)*(ka**q4)
xdata1, xdata2, ydata = [], [], []
# First the parameters for Re = [0.01,0.05,0.10]
for i in range(18):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
params1, _ = curve_fit(
    modelPolyLaw,(xdata1,xdata2),ydata, 
    maxfev=2200, 
    bounds = ([4.7,4.7,10.1,10.1,0,-10**3,-0.01,-10**2],
              [5.3,5.3,20,20,1.5*10**(-8),2*10**3,0.01,2*10**2])
    )
print('Parameters for Re = [0.01,0.05,0.10]',params1)
# Next the parameters for Re = [0.20,0.25,0.30]
for i in range(18,36):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
params2, _ = curve_fit(
    modelPolyLaw,(xdata1,xdata2),ydata, 
    maxfev=2200, 
    bounds = ([4.7,4.7,10.1,10.1,0,-10**3,-0.01,-10**2],
              [5.3,5.3,20,20,1.5*10**(-8),2*10**3,0.01,10**2])
    )
print('Parameters for Re = [0.20,0.25,0.30]',params2)
yDataNew = []
q1 = params1[0]
q2 = params1[1]
q3 = params1[2]
q4 = params1[3]
p0 = params1[4]
p1 = params1[5]
p2 = params1[6]
p3 = params1[7]
for k in range(18):
    yDataNew.append(
        modelPolyLaw((xdata1[k],xdata2[k])
                     ,q1,q2,q3,q4,p0,p1,p2,p3)
        )
q1 = params2[0]
q2 = params2[1]
q3 = params2[2]
q4 = params2[3]
p0 = params2[4]
p1 = params2[5]
p2 = params2[6]
p3 = params2[7]
for k in range(18,36):
    yDataNew.append(
        modelPolyLaw((xdata1[k],xdata2[k])
                     ,q1,q2,q3,q4,p0,p1,p2,p3)
        )
err = []
for k in range(36):
    err.append(abs(yDataNew[k]-ydata[k])/ydata[k]*0.01)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata1, xdata2, err)
ax.set_xlabel('Re')
ax.set_ylabel('r0/a')
ax.set_zlabel('Error from the original data')