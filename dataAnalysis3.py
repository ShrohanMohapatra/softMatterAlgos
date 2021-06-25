#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:14:17 2021

@author: shrohanmohapatra
"""
from dataDictionary import dataDict
from scipy.optimize import curve_fit
def modelPowerLaw(x,kL,alpha,beta):
    Re = x[0]
    kappa = x[1]
    return kL*(Re**alpha)*(kappa**beta)
xdata1, xdata2, ydata = [], [], []
# First the parameters for Re = [0.01,0.05,0.10]
for i in range(18):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
parameters, pcov = curve_fit(modelPowerLaw,(xdata1,xdata2),ydata)
print('Parameters for Re = [0.01,0.05,0.10]',parameters)
print('Errors in the parameters =',pcov)
# Next the parameters for Re = [0.20,0.25,0.30]
for i in range(18,36):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
parameters, pcov = curve_fit(modelPowerLaw,(xdata1,xdata2),ydata)
print('Parameters for Re = [0.20,0.25,0.30]',parameters)
print('Errors in the parameters =',pcov)