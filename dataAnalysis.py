#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 19:14:42 2021

@author: shrohanmohapatra
"""
from dataDictionary import dataDict
from scipy.optimize import curve_fit
def modelPowerLaw(x,kL,alpha,beta):
    Re = x[0]
    kappa = x[1]
    return kL*(Re**alpha)*(kappa**beta)
xdata1, xdata2, ydata = [], [], []
for i in range(36):
    xdata1.append(dataDict[i]['Reynolds number']),
    xdata2.append(dataDict[i]['r0/a'])
    ydata.append(dataDict[i]['Total force'])
parameters, pcov = curve_fit(modelPowerLaw,(xdata1,xdata2),ydata)
print(parameters)
