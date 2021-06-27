#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 12:23:12 2021

@author: shrohanmohapatra
"""

import mph
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
print(model.evaluate('integrate(spf.U,x,0,2*a,y,0,2*a)'))
model.save()