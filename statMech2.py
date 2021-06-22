#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:32:39 2021

@author: shrohanmohapatra
"""
from random import random
from math import pi, sin, exp, cos
def integrand(g):
    sum1 = 0
    n = 0
    err = 1e-12
    A = []
    while True:
        t1 = random()*pi
        t2 = random()*pi
        f1 = random()*2*pi
        f2 = random()*2*pi
        r1 = random()
        r2 = random()
        if (t1,t2,f1,f2,r1,r2) in A: continue
        sum2 = sum1
        A.append((t1,t2,f1,f2,r1,r2))
        n = n + 1
        p1 = r1**2*r2**2*sin(t1)*sin(t2)
        p2 = r1**2+r2**2
        p2 = p2 - 2*r1*r2*(cos(t1)*cos(t2)+sin(t1)*sin(t2)*cos(f1-f2))
        p1 = p1*exp(-g*(p2)**(-0.5))
        sum1 = sum1 + p1
        print('Particle 1',r1,t1/pi,f1/(2*pi))
        print('Particle 2',r2,t2/pi,f2/(2*pi))
        err1 = abs(sum1-sum2)/(sum1+0.01)
        print('Iteration', n, sum1, err1)
        print()
        if err1 < err: break
    return 4*pi**2*sum1/n
print(integrand(1.25))
A = [
     5,3,5,145,81,
     408,141,83,33,47,
     64,130,8,131,73,
     73,223,168,94,39,
     77,149,270,178,229
     ]
print(sum(A)/25)