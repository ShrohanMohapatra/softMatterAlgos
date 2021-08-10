#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 20:29:05 2021

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

# Mesh dimensions.
dims = [0.1, 0.1]

# Mesh resolution: increase to improve accuracy.
shape = [51, 51]

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

a = 0.1
nu = 1.00e-2
Re = 1e8
err = 1.00e-2
U = Re*nu/a

regions = {
    'Omega' : 'all',
    'Left' : ('vertices in (x < -'+str(a*(1-err)/2)+')', 'facet'),
    'Right' : ('vertices in (x > '+str(a*(1-err)/2)+')', 'facet'),
    'Bottom' : ('vertices in (y < -'+str(a*(1-err)/2)+')', 'facet'),
    'Top' : ('vertices in (y > '+str(a*(1-err)/2)+')', 'facet')
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
    'No1_Driven' : ('Top', {'u.0' : -1.0, 'u.1' : 0.0}),
    'No2_Driven' : ('Bottom', {'u.0' : 1.0, 'u.1' : 0.0}),
    'No3_Driven' : ('Left', {'u.0' : 0.0, 'u.1' : -1.0}),
    'No4_Driven' : ('Right', {'u.0' : 0.0, 'u.1' : 1.0})
}

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