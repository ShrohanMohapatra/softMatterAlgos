#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:22:10 2021

@author: shrohanmohapatra
"""
import numpy as np
import matplotlib.pyplot as plt
fileReader = open('dataStorageFile.txt')
pointerGroups = {
    'Re1':[[],[]],'Re2':[[],[]],
    'Re3':[[],[]],'Re4':[[],[]],
    'Re5':[[],[]]
    }
ReList = [1e-5,0.0001,0.001,0.01,0.1]
for lines in fileReader.readlines():
    extraction = lines.split(' ')
    xPointer = float((extraction[0].split('='))[1])
    if xPointer == 1e-5:
        pointerGroups['Re1'][0].append(
            float((extraction[1].split('='))[1])
            )
        pointerGroups['Re1'][1].append(
            float((extraction[2].split('='))[1])
            )
    elif xPointer == 0.0001:
        pointerGroups['Re2'][0].append(
            float((extraction[1].split('='))[1])
            )
        pointerGroups['Re2'][1].append(
            float((extraction[2].split('='))[1])
            )
    elif xPointer == 0.001:
        pointerGroups['Re3'][0].append(
            float((extraction[1].split('='))[1])
            )
        pointerGroups['Re3'][1].append(
            float((extraction[2].split('='))[1])
            )
    elif xPointer == 0.01:
        pointerGroups['Re4'][0].append(
            float((extraction[1].split('='))[1])
            )
        pointerGroups['Re4'][1].append(
            float((extraction[2].split('='))[1])
            )
    elif xPointer == 0.1:
        pointerGroups['Re5'][0].append(
            float((extraction[1].split('='))[1])
            )
        pointerGroups['Re5'][1].append(
            float((extraction[2].split('='))[1])
            )
for k in range(1,6):
    xData = np.array(pointerGroups['Re'+str(k)][0])
    yData = np.array(pointerGroups['Re'+str(k)][1])
    plt.scatter(xData, yData)
    plt.xlabel('r0/a')
    plt.ylabel('Fint/mu/U')
    plt.title('Re = '+str(ReList[k-1]))
    plt.show()

