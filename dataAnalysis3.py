#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 23:14:17 2021

@author: shrohanmohapatra
"""

from scipy.optimize import curve_fit
def modelPowerLaw(x,kL,alpha,beta):
    Re = x[0]
    kappa = x[1]
    return kL*(Re**alpha)*(kappa**beta)
dataDict = []
Re = [0.01,0.05,0.10,0.20,0.25,0.30]
k0 = [0.01,0.05,0.10,0.20,0.25,0.30]
count = 0
for i in range(6):
    for j in range(6):
        dataDict.append({})
        dataDict[count]['Reynolds number'] = Re[i]
        dataDict[count]['r0/a'] = k0[j]
        count = count + 1
dataDict[0]['Total force'] = 2.44e-9
dataDict[1]['Total force'] = 5.33e-9
dataDict[2]['Total force'] = 6.12e-9
dataDict[3]['Total force'] = 7.72e-9
dataDict[4]['Total force'] = 1.76e-9
dataDict[5]['Total force'] = 1.33e-9
dataDict[6]['Total force'] = 1.30e-8
dataDict[7]['Total force'] = 4.29e-8
dataDict[8]['Total force'] = 1.48e-7
dataDict[9]['Total force'] = 1.43e-8
dataDict[10]['Total force'] = 2.82e-8
dataDict[11]['Total force'] = 1.02e-8
dataDict[12]['Total force'] = 4.27e-8
dataDict[13]['Total force'] = 5.14e-8
dataDict[14]['Total force'] = 7.23e-8
dataDict[15]['Total force'] = 8.37e-8
dataDict[16]['Total force'] = 1.55e-8
dataDict[17]['Total force'] = 7.70e-8
dataDict[18]['Total force'] = 1.93e-8
dataDict[19]['Total force'] = 1.27e-7
dataDict[20]['Total force'] = 2.56e-7
dataDict[21]['Total force'] = 3.68e-9
dataDict[22]['Total force'] = 1.75e-9
dataDict[23]['Total force'] = 1.99e-8
dataDict[24]['Total force'] = 9.83e-9
dataDict[25]['Total force'] = 8.38e-9
dataDict[26]['Total force'] = 4.80e-8
dataDict[27]['Total force'] = 1.37e-8
dataDict[28]['Total force'] = 7.37e-8
dataDict[29]['Total force'] = 4.94e-8
dataDict[30]['Total force'] = 1.89e-8
dataDict[31]['Total force'] = 3.62e-8
dataDict[32]['Total force'] = 1.56e-8
dataDict[33]['Total force'] = 3.11e-8
dataDict[34]['Total force'] = 1.81e-8
dataDict[35]['Total force'] = 7.46e-8
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