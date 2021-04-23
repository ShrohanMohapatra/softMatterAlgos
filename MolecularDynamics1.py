# the monte carlo molecular dynamics for vaporized NaCl
from math import sqrt
from random import random, randint
def potentialU(q1,q2,r1,r2):
    e = 1.6*10**(-19) # Charge of the electron
    eps0 = 8.85*10**(-12) # Permittivity of vaccuum
    pi = 3.141592
    U = q1*q2*e**2
    U = U/(4*pi*eps0)
    r12 = r1[0]**2 + r1[1]**2 + r1[2]**2
    r12 = r2 + r2[0]**2 + r2[1]**2 + r2[2]**2
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
        box[k]['r'] = [random()*Lx,random()*Ly,random()*Lz] # position of particle
    # Assign all the negatively charged particles first
    for k in range(k1,Np):
        box[k]['q'] = -1 # Charge
        box[k]['r'] = [random()*Lx,random()*Ly,random()*Lz] # position of particle
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
Np = 250 # Number of particles
Lx = 0.10 # Length of the box
Ly = 0.15 # Width of the box
Lz = 0.20 # Breadth of the box
# Import the box of particles with randomly assigned positions.
box = boxOfParticles(Np,Lx,Ly,Lz)
delta = 0.02 # The range of collisions
Etotal = TotalInternalEnergy(box) # Total Internal Energy
while True:
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
    remainE = 0
    for k in range(Np):
        for m in range(Np):
            if k!=i and m!=k:
                E1total = E1total + potentialU(
                box[k]['q'], box[m]['q'], box[k]['r'], box[m]['r']
                )
                remainE = remainE + potentialU(
                box[k]['q'], box[m]['q'], box[k]['r'], box[m]['r']
                )
    delE = E1total - Etotal
    if delE<0:
        for k in range(3): box[i]['r'][k] = xi_next[k]
        Etotal = delE + remainE
    else:
        threshold = 0
        pass