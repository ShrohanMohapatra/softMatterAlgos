#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 20:02:48 2021

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
import numpy as np
# Mesh dimensions.
dims = [1.0, 1.0]

# Mesh resolution: increase to improve accuracy.
shape = [60, 60]

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

a = 0.9
r0 = 0.2*a/2
nu = 8.91e-4
Re = 1500
U = Re*nu/a
k = a/2-r0
def belt1_fun(coors, domain = None):
    return np.where(
        np.logical_and(
            ((coors[:,0]+k)**2+(coors[:,1]+k)**2>=r0**2),
            np.logical_and(-a/2<=coors[:,0],coors[:,0]<=-k),
            np.logical_and(-a/2<=coors[:,1],coors[:,1]<=-k)
            )
        )[0]
def belt2_fun(coors, domain = None):
    return np.where(
        np.logical_and(
            ((coors[:,0]-k)**2+(coors[:,1]+k)**2>=r0**2),
            np.logical_and(k<=coors[:,0],coors[:,0]<=a/2),
            np.logical_and(-a/2<=coors[:,1],coors[:,1]<=-k)
            )
        )[0]
def belt3_fun(coors, domain = None):
    return np.where(
        np.logical_and(
            ((coors[:,0]-k)**2+(coors[:,1]-k)**2>=r0**2),
            np.logical_and(k<=coors[:,0],coors[:,0]<=a/2),
            np.logical_and(k<=coors[:,1],coors[:,1]<=a/2)
            )
        )[0]
def belt4_fun(coors, domain = None):
    return np.where(
        np.logical_and(
            ((coors[:,0]+k)**2+(coors[:,1]-k)**2>=r0**2),
            np.logical_and(-a/2<=coors[:,0],coors[:,0]<=-k),
            np.logical_and(k<=coors[:,1],coors[:,1]<=a/2)
            )
        )[0]
def top1_definer(coors, domain = None):
    return np.where(
        np.logical_and(
            np.logical_and(-k<=coors[:,0],coors[:,0]<=k),
            coors[:,1] >= a/2
            )
        )[0]
def bottom1_definer(coors, domain = None):
    return np.where(
        np.logical_and(
            np.logical_and(-k<=coors[:,0],coors[:,0]<=k),
            coors[:,1] <= -a/2
            )
        )[0]
def right1_definer(coors, domain = None):
    return np.where(
        np.logical_and(
            np.logical_and(-k<= coors[:,1],coors[:,1] <= k),
            (coors[:,0] >= a/2)
            )
        )[0]
def left1_definer(coors, domain = None):
    return np.where(
        np.logical_and(
        np.logical_and(-k<= coors[:,1],coors[:,1] <= k),
        coors[:,0] <= -a/2
        ))[0]
def componentDescriber2(ts, coors, bc=None, problem=None):
    return np.array((
        -U*coors[:,1]/np.sqrt(coors[:,0]**2+coors[:,1]**2),
        U*coors[:,0]/np.sqrt(coors[:,0]**2+coors[:,1]**2)
        ))
functions = {
    'componentDescriber2':(componentDescriber2,),
    'belt1_fun':(belt1_fun,),
    'belt2_fun':(belt2_fun,),
    'belt3_fun':(belt3_fun,),
    'belt4_fun':(belt4_fun,),
    'top1_definer':(top1_definer,),
    'bottom1_definer':(bottom1_definer,),
    'right1_definer':(right1_definer,),
    'left1_definer':(left1_definer,),
    }

regions = {
    'Omega' : 'all',
    'Top': ('vertices by top1_definer','facet'),
    'Bottom': ('vertices by bottom1_definer','facet'),
    'Right': ('vertices by right1_definer','facet'),
    'Left': ('vertices by left1_definer','facet'),
    'Belt1': ('vertices by belt1_fun','facet'),
    'Belt2': ('vertices by belt2_fun','facet'),
    'Belt3': ('vertices by belt3_fun','facet'),
    'Belt4': ('vertices by belt4_fun','facet'),
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
    'DrivenTop' : ('Top', {'u.0' : -U, 'u.1': 0}),
    'DrivenBot' : ('Bottom', {'u.0' : U, 'u.1': 0}),
    'DrivenRig' : ('Right', {'u.0' : 0, 'u.1': U}),
    'DrivenLef' : ('Left', {'u.0' : 0, 'u.1': -U}),
    'Drive1': ('Belt1',{'u.[0,1]' : 'componentDescriber2'}),
    'Drive2': ('Belt2',{'u.[0,1]' : 'componentDescriber2'}),
    'Drive3': ('Belt3',{'u.[0,1]' : 'componentDescriber2'}),
    'Drive4': ('Belt4',{'u.[0,1]' : 'componentDescriber2'}),
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
        'macheps'    : 1e-8,
    }),
}