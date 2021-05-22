#  A modified SCFT algorithm for a dilute homopolymer solution with
#  the power law mean-field
#                                - Shrohan Mohapatra
#                                  University of Massachusetts, Amherst

# Here I will be using power law model for modelling the
# guess potentials,
# U(r) = A0 + A1/r + A2/r^2 + A3/r^3 + A4/r^4 + B1 r + B2 r**2 .....

from random import random
from math import sqrt
from scipy.optimize import curve_fit
from numpy import array
N1 = 6 # Number of terms in the power law potential
f = 250 # The amplitude parameter of the energy terms
A = [f*random() for k in range(N1)] # the list of Ais ....
n = 10 # The number of segments
Lx = 5 # The size of the box
Ly = Lx
Lz = Ly
delx = 0.25 # The resolution of the box
Nx = int(Lx/delx)
k = 0.9 # The Hookean constant of the spring box ...
kB = 1.38*10**(-23) # Boltzmann constant
T = 300 # Temperature in kelvin ....
b2 = 3*kB*T/k # Kuhn segment size ....
err = 10**(-2) # Allowable error
# The function that computes the potential ....
def potentialEnergy(r,A):
    E1 = 0
    n = len(A)
    f = int(n/2)
    r1 = sqrt(r[0]**2+r[1]**2+r[2]**2)+0.01
    for k in range(f):
        E1 = E1 + A[k]/r1**k
    for k in range(f,n):
        E1 = E1 + A[k]*r1**(k-f+1)
    return E1
def potentialEnergy1(r1,*A):
    E1 = 0
    n = len(A)
    f = int(n/2)
    for k in range(f):
        E1 = E1 + A[k]/r1**k
    for k in range(f,n):
        E1 = E1 + A[k]*r1**(k-f+1)
    return E1
counter = 0 # just for a test ....
while True:
    q = [
        [[[0 for k3 in range(Nx)] for k2 in range(Nx)] for k1 in range(Nx)]
        for k0 in range(n)]
    # Imposing the boundary conditions, q(n=0,x,y,z) = 1 ....
    for k1 in range(Nx):
        for k2 in range(Nx):
            for k3 in range(Nx):
                q[0][k1][k2][k3] = 1
    # Now I am implementing a cellular automata that solves the PDE ...
    for k0 in range(n-1):
        for k1 in range(1,Nx-1):
            for k2 in range(1,Nx-1):
                for k3 in range(1,Nx-1):
                    q[k0+1][k1][k2][k3] = q[k0+1][k1][k2][k3]+q[k0][k1][k2][k3]
                    s = ( q[k0][k1+1][k2][k3]-2*q[k0][k1][k2][k3] \
                        + q[k0][k1-1][k2][k3])
                    s = s/delx**2
                    q[k0+1][k1][k2][k3] = q[k0+1][k1][k2][k3] + s*b2/6
                    s = ( q[k0][k1][k2][k3]-2*q[k0][k1][k2+1][k3] \
                        + q[k0][k1][k2-1][k3] )
                    s = s/delx**2
                    q[k0+1][k1][k2][k3] = q[k0+1][k1][k2][k3] + s*b2/6
                    s = ( q[k0][k1][k2][k3]-2*q[k0][k1][k2][k3+1] \
                        + q[k0][k1][k2][k3-1] )
                    s = s/delx**2
                    q[k0+1][k1][k2][k3] = q[k0+1][k1][k2][k3] + s*b2/6
                    # write a function that computes the potential
                    x = [delx*k1,delx*k2,delx*k3]
                    e = potentialEnergy(x, A)
                    q[k0+1][k1][k2][k3] = q[k0+1][k1][k2][k3] - \
                    q[k0][k1][k2][k3]*e/kB/T
    Q = 0
    vol = Lx*Ly*Lz
    elem = delx**3
    for k1 in range(Nx):
            for k2 in range(Nx):
                for k3 in range(Nx):
                    Q = Q + elem/vol*q[n-1][k1][k2][k3]
    avg_phi = [[[0 for k3 in range(Nx)] for k2 in range(Nx)] for k1 in range(Nx)]
    Ueff = [[[0 for k3 in range(Nx)] for k2 in range(Nx)] for k1 in range(Nx)]
    radiusFromCenter = []
    graphOfPotential = []
    for k0 in range(int(n/2)):
        for k1 in range(Nx):
            for k2 in range(Nx):
                for k3 in range(Nx):
                    avg_phi[k1][k2][k3] = avg_phi[k1][k2][k3] + \
                        q[k0][k1][k2][k3]*q[n-1-k0][k1][k2][k3]/Q
    for k1 in range(Nx):
            for k2 in range(Nx):
                for k3 in range(Nx):
                    Ueff[k1][k2][k3] = kB*T*elem*avg_phi[k1][k2][k3]
                    r3 = delx*sqrt(k1**2+k2**2+k3**2)
                    if r3 not in radiusFromCenter:
                        radiusFromCenter.append(r3+0.01)
                        graphOfPotential.append(Ueff[k1][k2][k3])
    radius1 = array(radiusFromCenter)
    graph1 = array(graphOfPotential)
    fit = curve_fit(potentialEnergy1,radius1,graph1,A)
    flag = True
    for k in range(len(A)): flag = flag and abs(fit[0][k]-A[k])/abs(A[k])<err
    if flag: break
    else:
        for k in range(len(A)): A[k] = fit[0][k]
    counter = counter + 1
    print(counter,A)
