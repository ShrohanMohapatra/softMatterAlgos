#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 11:17:13 2021

@author: shrohanmohapatra
"""

### Thanks to https://stackoverflow.com/questions/3160699/python-progress-bar
import mph
import sys
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
client = mph.start(cores=1)
model = client.load('2DGeometryExample.mph')
print(model.parameters())
print('Start of the simulation')
ReList = [10**(-5),10**(-4),10**(-3),10**(-2),10**(-1)]
fileHandle = open('dataStorageFile.txt','w')
ndp = 40
try:
    for Re in progressbar(ReList,"Progress 1: ",25):
        r0List = [(0.1*ndp+9.9*k-10)*Re/(ndp-1) for k in range(1,ndp+1)]
        for r0 in progressbar(r0List,"Progress 2: ",25):
            model.parameter('Re',str(Re))
            model.parameter('r0',str(r0)+'[m]')
            try:
                model.solve()
            except:
                pass
            try:
                result = model.evaluate('integrate(subst((comp1.vy)*Re/rho/a,y,0),x,r0,2*a-r0)')
            except:
                pass
            result1 = sum(result.tolist())
            try:
                result = model.evaluate(
                    'integrate(subst((comp1.ux*(x-r0)^2/r0^2+mu*comp1.vy*(y-r0)^2/r0^2+mu*(comp1.uy+comp1.vx)*(x-r0)*(y-r0)/r0^2)*Re/rho/a,y,r0-sqrt(2*r0*x-x^2)),x,0,r0)'
                    )
            except:
                pass
            result2 = sum(result.tolist())
            print('Re='+str(Re)+' r0/a='+str(r0)+' F/mu/U='+str(4*abs(result1+result2)))
            fileHandle.write('Re='+str(Re)+' r0/a='+str(r0)+' F/mu/U='+str(4*abs(result1+result2))+'\n')
            model.save()
    print('End of the simulation')
    fileHandle.close()
except KeyboardInterrupt:
    fileHandle.close()
