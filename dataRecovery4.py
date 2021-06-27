#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 21:25:00 2021

@author: shrohanmohapatra
"""
import mph
client = mph.start(cores=1)
model = client.load('2DGeometryExample.mph')
print(model.parameters())
print('Start of the simulation')
ReList = [10**(-5),10**(-4),10**(-3),10**(-2),10**(-1)]
fileHandle = open('dataStorageFile.txt','w')
try:
    for Re in ReList:
        r0List = [(1.009*k-0.909)*Re for k in range(1,101)]
        for r0 in r0List:
            model.parameter('Re',str(Re))
            model.parameter('r0',str(r0)+'[m]')
            try:
                model.solve()
                result = model.evaluate('integrate(subst(abs(comp1.vy)*Re/rho/a,y,0),x,r0,2*a-r0)')
                result1 = sum(result.tolist())
                result = model.evaluate(
                    'integrate(subst(abs(comp1.ux*(x-r0)^2/r0^2+mu*comp1.vy*(y-r0)^2/r0^2+mu*(comp1.uy+comp1.vy)*(x-r0)*(y-r0)/r0^2)*Re/rho/a,y,r0-sqrt(2*r0*x-x^2)),x,0,r0)'
                    )
                result2 = sum(result.tolist())
                print('Re='+str(Re)+' r0/a='+str(r0)+' F/mu/U='+str(4*(result1+result2)))
                fileHandle.write('Re='+str(Re)+' r0/a='+str(r0)+' F/mu/U='+str(4*(result1+result2))+'\n')
                model.save()
            except:
                pass
    print('End of the simulation')
    fileHandle.close()
except KeyboardInterrupt:
    fileHandle.close()
