#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 00:52:29 2021

@author: shrohanmohapatra
"""
# -*- coding: utf-8 -*-
r"""
Navier-Stokes equations for incompressible fluid flow in 2D.

Find :math:`\ul{u}`, :math:`p` such that:

.. math::
    \int_{\Omega} \nu\ \nabla \ul{v} : \nabla \ul{u}
    + \int_{\Omega} ((\ul{u} \cdot \nabla) \ul{u}) \cdot \ul{v}
    - \int_{\Omega} p\ \nabla \cdot \ul{v}
    = 0
    \;, \quad \forall \ul{v} \;,

    \int_{\Omega} q\ \nabla \cdot \ul{u}
    = 0
    \;, \quad \forall q \;.

The mesh is created by ``gen_block_mesh()`` function.

View the results using::

  $ ./postproc.py user_block.vtk -b
"""
#from __future__ import absolute_import
from sfepy.discrete.fem.meshio import UserMeshIO
from sfepy.mesh.mesh_generators import gen_block_mesh
import numpy as np
# Mesh dimensions.
dims = [0.6, 0.6]

# Mesh resolution: increase to improve accuracy.
shape = [50, 50]

def mesh_hook(mesh, mode):
    """
    Generate the block mesh.
    """
    if mode == 'read':
        mesh = gen_block_mesh(dims, shape, [0, 0], name='user_block',
                              verbose=False)
        return mesh

    elif mode == 'write':
        pass

filename_mesh = UserMeshIO(mesh_hook)

a = 0.6
nu = 8.91e-4
Re = 750
U = Re*nu/a
def circle_function(coors, domain = None):
    return np.where(
        np.sqrt(coors[:,0]**2+coors[:,1]**2) > (a/2)
        )[0]
def componentDescriber2(ts, coors, bc=None, problem=None):
    return (
        U*coors[:,1]/np.sqrt(coors[:,0]**2+coors[:,1]**2),
        -U*coors[:,0]/np.sqrt(coors[:,0]**2+coors[:,1]**2)
        )
functions = {
    'circle_function':(circle_function,),
    'componentDescriber2':(componentDescriber2,)
    }

regions = {
    'Omega' : 'all',
    'Wall': ('vertices by circle_function', 'facet')
}


materials = {
    'fluid' : ({'viscosity' : nu},),
}

fields = {
    'velocity': ('real', 'vector', 'Omega', 2),
    'pressure': ('real', 'scalar', 'Omega', 1),
}

variables = {
    'u' : ('unknown field', 'velocity', 0),
    'v' : ('test field', 'velocity', 'u'),
    'p' : ('unknown field', 'pressure', 1),
    'q' : ('test field', 'pressure', 'p'),
}

ebcs = {
    'No1_Driven' : ('Wall', {'u.[0,1]' : 'componentDescriber2'})
}

# How to define functions for defining the tangential velocity
# precisely because u.all does not work all
# python3 simple.py femTrial3.py
# python3 postproc.py user_block.vtk -o image.jpg -n

integrals = {
    'i' : 4,
}

equations = {
    'balance' :
    """+ dw_div_grad.i.Omega(fluid.viscosity, v, u)
       + dw_convect.i.Omega(v, u)
       - dw_stokes.i.Omega(v, p) = 0""",

    'incompressibility' :
    """dw_stokes.i.Omega(u, q) = 0""",
}

solvers = {
    'ls' : ('ls.scipy_direct', {}),
    'newton' : ('nls.newton', {
        'i_max'      : 15,
        'eps_a'      : 1e-6,
        'eps_r'      : 1.0,
        'macheps'    : 1e-16,
        'lin_red'    : 1000,
    }),
}