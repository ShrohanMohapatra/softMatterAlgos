# Molecular dynamics of an MCE of ions in molten
# NaCl with periodic boundary conditions
#                                     - Shrohan Mohapatra
#                                     University of Massachusetts, Amherst

# The methodology uses Verlet integration technique ....
# ri(t+del t) = 2ri(t) - ri(t-del t) + (del t)^2 fi(t)/m
# vi(t) = (ri(t+del t)-ri(t-del t))/(2 del t)
# fi = sum_{j} (q_i q_j e^2)/(4 pi eps_0 |r_ij|^3) r_ij - 6 pi mu Ri vi
# Here for molten NaCl I am borrowing some data from the following papers:
# 1. "Conductivity of molten NaCl and its supercritical values in strong dc 
# electric field", J. Petravic, J. Delhommelle, Journal of 
# Chemical Physics, 2013
# 2. "Shear viscosity of molten sodium chloride", J. Petravic, J. Delhommelle, 
# Journal of Chemical Physics, 2003
# 3. "Thermodynamic analysis of molecular dynamics simulation of evaporation
# and condensation", E. A. T. van der Akken, A. J. H. Frijns, A. A. van 
# Steenhoven, P. A. J. Hilbers, 5th European Thermal-Science Conference, 2006

from math import sqrt
from random import random
from pprint import pprint
from matplotlib import pyplot as plt
def potentialU(q1,q2,r1,r2):
    e = 1.6*10**(-19) # Charge of the electron
    eps0 = 8.85*10**(-12) # Permittivity of vaccuum
    pi = 3.141592
    U = q1*q2*e**2
    U = U/(4*pi*eps0)
    r12 = (r1[0]-r2[0])**2
    r12 = r12 + (r1[1]-r2[1])**2
    r12 = r12 + (r1[2]-r2[2])**2
    r12 = sqrt(r12)
    U = U/r12
    return U
def electroF(q1,q2,r1,r2): # Coulombic force
    e = 1.6*10**(-19) # Charge of the electron in C
    eps0 = 8.85*10**(-12) # Permittivity of vaccuum
    pi = 3.141592
    F1 = q1*q2*e**2
    F1 = F1/(4*pi*eps0)
    r12 = (r1[0]-r2[0])**2
    r12 = r12 + (r1[1]-r2[1])**2
    r12 = r12 + (r1[2]-r2[2])**2
    r12 = sqrt(r12)**3
    F1 = F1/r12
    return [F1*(r2[k]-r1[k]) for k in range(3)]
def dragF(mu,R,v):
    pi = 3.141592
    return [-6*pi*mu*R*v[k] for k in range(3)]
def boxOfParticles(Np,Lx,Ly,Lz):
    # Initiate the box
    box = [{} for k in range(Np)]
    k1 = int(Np/2) # the number of posivitely/negatively
    # charged particles
    # Assign all the positively charged particles first
    for k in range(k1):
        box[k]['q'] = 1 # Charge
        box[k]['r'] = [
            (random()-0.5)*Lx,(random()-0.5)*Ly,(random()-0.5)*Lz
            ] # position of particle
        box[k]['v'] = [random(),random(),random()] # velocity of particle
        box[k]['R'] = 102*10**(-12) # ionic radius of Na+ is 102 pm
        box[k]['m'] = 23*10**(-3)/(6.023*10**23) # mass of Na+ ion in kg
    # Assign all the negatively charged particles next
    for k in range(k1,Np):
        box[k]['q'] = -1 # Charge
        box[k]['r'] = [
            (random()-0.5)*Lx,(random()-0.5)*Ly,(random()-0.5)*Lz
            ] # position of particle
        box[k]['v'] = [random(),random(),random()] # velocity of particle
        box[k]['R'] = 181*10**(-12) # ionic radius of Cl- is 181 pm
        box[k]['m'] = 35*10**(-3)/(6.023*10**23) # mass of Cl- ion in kg
    return box
def periodicBC(x, Lx): # This function is meant to restrict the molecules in
    # the box meant for MCE .....
    while not(-Lx/2<=x<=Lx/2):
        if x > Lx/2: x = Lx-x
        elif x < (-1)*Lx/2: x = -Lx-x
    return x
# Now begins the simulation
Np = 10 # Number of particles
Lx = 0.70 # Length of the box
Ly = Lx # Width of the box
Lz = Ly # Breadth of the box
# Import the box of particles with randomly assigned positions.
box = boxOfParticles(Np,Lx,Ly,Lz)
delt = 10**(-12) # 1 ps between the successive time steps
eta = 7.82*10**(-4) # dynamic viscosity of molten NaCl
Nstep = 10000 # Number of steps
kB = 1.38*(10**(-23)) # Boltzmann constant in J K^-1
Temp = [] # Temperature plots
UEInt = [] # Internal energy plots
for k in range(Nstep):
    if k == 0:
        prev_r = [[box[i]['r'][j] for j in range(3)] for i in range(Np)]
        prev_r2 = [[box[i]['r'][j] for j in range(3)] for i in range(Np)]
        for k1 in range(Np):
            for k2 in range(3):
                box[k1]['r'][k2] = box[k1]['r'][k2] + delt*box[k1]['v'][k2]
                # Now we will add the periodic boundary conditions
                box[k1]['r'][k2] = periodicBC(box[k1]['r'][k2],Lx)
    else:
        for k1 in range(Np):
            for k2 in range(3): prev_r2[k1][k2] = box[k1]['r'][k2]
        for k1 in range(Np):
            f_k1 = [0 for k in range(3)]
            for k3 in range(Np):
                if k1!=k3:
                    f_k2 = electroF(
                        box[k1]['q'],box[k3]['q'],
                        box[k1]['r'],box[k3]['r']
                    )
            for k4 in range(3): f_k1[k4] = f_k1[k4] + f_k2[k4]
            f_k4 = dragF(eta,box[k1]['R'],box[k1]['v'])
            for k4 in range(3): f_k1[k4] = f_k1[k4] + f_k4[k4]
            for k2 in range(3):
                s_1 = 2*box[k1]['r'][k2] - prev_r[k1][k2]
                box[k1]['r'][k2] = s_1 + f_k1[k2]*(delt**2)/box[k1]['m']
                # Now we will add the periodic boundary conditions
                box[k1]['r'][k2] = periodicBC(box[k1]['r'][k2],Lx)
                box[k1]['v'][k2] = (box[k1]['r'][k2]-prev_r[k1][k2])/(2*delt)
        for k1 in range(Np):
            for k2 in range(3): prev_r[k1][k2] = prev_r2[k1][k2]
    # Compute the Temperature and internal energy ....
    KEcalc, UEcalc, work = 0, 0, 0
    for k1 in range(Np):
        for k2 in range(3):
            KEcalc = KEcalc + 1/2*box[k1]['m']*box[k1]['v'][k2]**2
        for k3 in range(Np):
            if k3!=k1: UEcalc = UEcalc + potentialU(
                box[k1]['q'],box[k3]['q'],box[k1]['r'],box[k3]['r']
                )
        force = dragF(eta,box[k1]['R'],box[k1]['v'])
        work = work + force[0]*(box[k1]['r'][0]-prev_r[k1][0])
        work = work + force[1]*(box[k1]['r'][1]-prev_r[k1][1])
        work = work + force[2]*(box[k1]['r'][2]-prev_r[k1][2])
    Temp.append(KEcalc/3/kB)
    UEInt.append(KEcalc+UEcalc+work)
plt.plot(Temp)
plt.xlabel('Time steps')
plt.ylabel('Temperature (in K)')
plt.show()
plt.plot(UEInt)
plt.xlabel('Time steps')
plt.ylabel('Total internal energy (in J)')
plt.show()