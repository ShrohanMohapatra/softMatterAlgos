#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:58:24 2021

@author: shrohanmohapatra
"""

import numpy as np
from sfepy.discrete.fem import (Mesh, domain, Field, FieldVariable,
                       Material, Integral,
                       Equation, Equations,
                       ProblemDefinition)
from sfepy.terms import Term
from sfepy.discrete.fem.conditions import Conditions, EssentialBC
from sfepy.solvers.ls import ScipyDirect
from sfepy.solvers.nls import Newton
from sfepy.postprocess import Viewer
mesh = Mesh.from_file('meshes/2d/square_tri2.mesh')
domain1 = domain('domain',mesh)
omega = domain1.create_region('Omega','all')
left = domain1.create_region('Left','vertices in x<-0.999','facet')
right = domain1.create_region('Right','vertices in x > 0.999','facet')
bottom = domain1.create_region('Bottom','vertices in y < -0.999','facet')
top = domain1.create_region('Top','vertices in y > 0.999','facet')
domain1.save_regions_as_groups('regions.vtk')
field_t = Field.from_args('temperature',np.float64,'scalar',omega,2)
t = FieldVariable('t','unknown',field_t,1)
s = FieldVariable('s','test',field_t,1,primary_var_name='t')
integral = Integral('i',order=2)
term = Term.new('dw_laplace(s,t)',integral,omega,s=s,t=t)
eq = Equation('temperature', term)
eqs = Equations([eq])
t_left = EssentialBC('t_left',left,{'t.0':10.0})
t_right = EssentialBC('t_right',right,{'t.0':30.0})
ls = ScipyDirect({})
nls = Newton({}, lin_solver=ls)
pb = ProblemDefinition('temperature',equations=eqs,nls=nls,ls=ls)
pb.time_update(ebcs=Conditions([t_left, t_right]))
temperature = pb.solve()
out = temperature.create_output_dict()
pb.save_state('thermoelasticity.vtk', out=out)
