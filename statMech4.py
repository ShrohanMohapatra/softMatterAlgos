#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:24:03 2021

@author: shrohanmohapatra
"""

from random import random
from math import pi, sin, exp, cos
from matplotlib import pyplot
def integrand(g):
    sum1 = 0
    n = 0
    A = []
    while n<=114:
        t1 = random()*pi
        t2 = random()*pi
        f1 = random()*2*pi
        f2 = random()*2*pi
        r1 = random()
        r2 = random()
        if (t1,t2,f1,f2,r1,r2) in A: continue
        A.append((t1,t2,f1,f2,r1,r2))
        n = n + 1
        p1 = r1**2*r2**2*sin(t1)*sin(t2)
        p2 = r1**2+r2**2
        p2 = p2 - 2*r1*r2*(cos(t1)*cos(t2)+sin(t1)*sin(t2)*cos(f1-f2))
        p1 = p1*exp(-g*(p2)**(-0.5))
        sum1 = sum1 + p1
    return 4*pi**2*sum1/n
xAxis = [k for k in range(1,41)]
yAxis = [integrand(k) for k in range(1,41)]
pyplot.plot(xAxis, yAxis)
pyplot.show()