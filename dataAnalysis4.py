#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 11:49:57 2021

@author: shrohanmohapatra
"""
from dataDictionary import dataDict
from scipy.optimize import curve_fit
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
parameters, pcov = curve_fit(modelPolyLaw,(xdata1,xdata2),ydata, maxfev=2400)
print('Parameters for Re = [0.01,0.05,0.10]',parameters)
# Next the parameters for Re = [0.20,0.25,0.30]
for i in range(18,36):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
parameters, pcov = curve_fit(modelPolyLaw,(xdata1,xdata2),ydata, maxfev=2400)
print('Parameters for Re = [0.20,0.25,0.30]',parameters)


