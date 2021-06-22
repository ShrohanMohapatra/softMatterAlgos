#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:06:16 2021

@author: shrohanmohapatra
"""

from sympy import symbols, integrate, exp, oo
x1, x2, y1, y2, g = symbols('x1 x2 y1 y2 g')
print(integrate(exp(-g*((x2-x1)**2+(y2-y1)**2)**(-1/2)),(x1,-oo,oo)))
r1, r2, t1, t2 = symbols('r1 r2 t1 t2')
from sympy import cos, pi
print(
      integrate(r1*r2*exp(-g*(r1*r1+r2*r2-2*r1*r2*cos(t2-t1))**(-1/2)),
                (t1,0,2*pi)))
print(
      integrate(r1*r2*exp(-g*(r1*r1+r2*r2-2*r1*r2*cos(t2-t1))**(-1/2)),
                (r1,0,oo)))
#print(
#      integrate(r1*r2*exp(-g*(r1*r1+r2*r2-2*r1*r2*cos(t2-t1))**(-1/2)),
#                (r1,0,1),(r2,0,1),(t1,0,2*pi),(t2,0,2*pi)))
print((1.6e-19)**2/(4*3.14*8.85e-12*1.38e-23*273.15))
print(
      integrate(r1*r2*exp(-g*(r1*r1+r2*r2-2*r1*r2*cos(t2-t1))**(-1/2)),
                (r2,0,1)))