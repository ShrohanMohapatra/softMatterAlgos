#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 19:16:05 2021

@author: shrohanmohapatra
"""

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
import numpy as nm
# Mesh dimensions.
dims = [0.1, 0.1]

# Mesh resolution: increase to improve accuracy.
shape = [75, 75]

def mesh_hook(mesh, mode):
    """
    Generate the block mesh.
    """
    if mode == 'read':
        mesh = gen_block_mesh(dims, shape, [0, 0], 
                              name='user_block', verbose=False)
        return mesh

    elif mode == 'write':
        pass

filename_mesh = UserMeshIO(mesh_hook)
print('Just a check if the mesh is generated ...')
def get_circle(coors, domain=None):
    r = nm.sqrt(coors[:,0]**2.0 + coors[:,1]**2.0)
    return nm.where(r < 0.09)[0]

functions = {
    'get_circle' : (get_circle,),
}
print('Checked in a function ...')
regions = {
    'Omega' : 'all',
    'Walls' : ('vertices by get_circle', 'facet'),
}
print('Checked in the definition of regions ...')
materials = {
    'fluid' : ({'viscosity' : 8.917e-7},),
}
print('Checked in the definition of the material params ...')
fields = {
    'velocity': ('real', 'vector', 'Omega', 2),
    'pressure': ('real', 'scalar', 'Omega', 1),
}
print('Checked in the definition of u, v, p ...')
variables = {
    'u' : ('unknown field', 'velocity', 0),
    'v' : ('test field', 'velocity', 'u'),
    'p' : ('unknown field', 'pressure', 1),
    'q' : ('test field', 'pressure', 'p'),
}

ebcs = {
    '1_Wall': {'Walls': {'u.all':10}}
}
print('Checked in the boundary conditions ...')
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
        'eps_a'      : 1e-10,
        'eps_r'      : 1.0,
    }),
}