#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 19:47:02 2021

@author: shrohanmohapatra
"""

# parameters
import numpy as nm
a = 1 # Length scale
r0 = 0.1 # Radius of curvature of the rounded corners
Re = 0.1 # Reynold's number .... 
nu = 8.917e-7 # Viscosity ....
def get_circle(coors, domain=None):
    r = nm.sqrt(coors[:,0]**2.0 + coors[:,1]**2.0)
    return nm.where(r < a)[0]
