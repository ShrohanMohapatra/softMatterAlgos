#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:56:43 2021

@author: shrohanmohapatra
"""


import mph
from pprint import pprint
client = mph.start(cores=1)
model = client.load('2DGeometryExample.mph')
#print(client.names())
#print(client.models())
print(model.parameters())
for (name, value) in model.parameters().items():
    description = model.description(name)
    print(f'{description:20}{name} = {value}')
print(model.materials())
print(model.physics())
print(model.studies())
print(model.parameter('r0'))
print(model.datasets())
print(mph.tree(model))
try:
    model.solve()
except Exception as e:
    print(e)
    pass
result = model.evaluate('integrate(subst(abs(mu*comp1.vy),y,0),x,r0,2*a-r0)')
result1 = result.tolist()
pprint(result1)
print(len(result1))
print('Sum of the elements = ',sum(result1))
model.save()