#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:58:24 2021

@author: shrohanmohapatra
"""

import numpy as np
from sfepy.fem import (Mesh, Domain, Field, FieldVariable,
                       Material, Integral,
                       Equation, Equations,
                       ProblemDefinition)
from sfepy.terms import Term
from sfepy.fem.conditions import Conditions, EssentialBC
from sfepy.solvers.ls import ScipyDirect
from sfepy.solvers.nls import Newton
from sfepy.postprocess import Viewer
mesh = Mesh.from_file('meshes/2d/square_tri2.mesh')
