# the monte carlo molecular dynamics for vaporized NaCl
from math import sqrt,exp
from random import random, randint
from pprint import pprint
from matplotlib import pyplot as plt
def potentialU(q1,q2,r1,r2):
    e = 1.6*10**(-19) # Charge of the electron
    eps0 = 8.85*10**(-12) # Permittivity of vaccuum
    pi = 3.141592
    U = q1*q2*e**2
    U = U/(4*pi*eps0)
    r12 = r1[0]**2 + r1[1]**2 + r1[2]**2
    r12 = r12 + r2[0]**2 + r2[1]**2 + r2[2]**2
    r12 = sqrt(r12)
    U = U/r12
    return U
def boxOfParticles(Np,Lx,Ly,Lz):
    # Initiate the box
    box = [{} for k in range(Np)]
    k1 = int(Np/2) # the number of posivitely/negatively charged particles
    # Assign all the positively charged particles first
    for k in range(k1):
        box[k]['q'] = 1 # Charge
        box[k]['r'] = [
            (random()-0.5)*Lx,(random()-0.5)*Ly,(random()-0.5)*Lz
            ] # position of particle
    # Assign all the negatively charged particles first
    for k in range(k1,Np):
        box[k]['q'] = -1 # Charge
        box[k]['r'] = [
            (random()-0.5)*Lx,(random()-0.5)*Ly,(random()-0.5)*Lz
            ] # position of particle
    return box
def TotalInternalEnergy(box): # Total internal energy
    sum1 = 0
    Np = len(box) # total number of particles
    for i in range(Np):
        for j in range(i+1,Np):
            sum1 = sum1 + potentialU(
                box[i]['q'],box[j]['q'],box[i]['r'],box[j]['r']
                )
    return sum1
# Now begins the simulation
Np = 100 # Number of particles
Lx = 0.70 # Length of the box
Ly = 0.75 # Width of the box
Lz = 0.80 # Breadth of the box
T = 1700 # Temperature in Kelvin
# Boiling point of NaCl is 1686 K
# Import the box of particles with randomly assigned positions.
box = boxOfParticles(Np,Lx,Ly,Lz)
delta = 0.12 # The range of collisions
Etotal = TotalInternalEnergy(box) # Total Internal Energy
kB = 1.38*10**(-23) # Boltzmann constant
Nstep = 10 # Number of steps
for y in range(Nstep):
    i = randint(0,Np-1)
    xi_next = [
        box[i]['r'][0]+delta*(random()-0.5),
        box[i]['r'][1]+delta*(random()-0.5),
        box[i]['r'][2]+delta*(random()-0.5)
    ]
    E1total = 0
    for j in range(Np):
        if i!=j:
            E1total = E1total + potentialU(
                box[j]['q'], box[i]['q'], box[j]['r'], xi_next
                )
    for k in range(Np):
        for m in range(Np):
            if k!=i and m!=k:
                E1total = E1total + potentialU(
                box[k]['q'], box[m]['q'], box[k]['r'], box[m]['r']
                )
    delE = E1total - Etotal
    if delE<0:
        for k in range(3): box[i]['r'][k] = xi_next[k]
        Etotal = E1total
    else:
        threshold = random()
        if threshold<exp(-delE/kB/T):
            for k in range(3): box[i]['r'][k] = xi_next[k]
            Etotal = E1total
    # pprint(box)
    x1 = [box[i]['r'][0] for i in range(Np)]
    y1 = [box[i]['r'][1] for i in range(Np)]
    z1 = [box[i]['r'][2] for i in range(Np)]
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter3D(x1,y1,z1)
    plt.savefig('plot'+str(y)+'.png', dpi=300, bbox_inches='tight')
    print('Figure no.'+str(y)+' done')