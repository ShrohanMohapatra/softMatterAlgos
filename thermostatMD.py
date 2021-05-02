# Applying Nose-Hoover thermostat to an MCE of ions
# in molten NaCl with periodic boundary conditions
#                                     - Shrohan Mohapatra
#                                     University of Massachusetts, Amherst

# The methodology uses Euler forward integration technique ....
# Here for molten NaCl I am borrowing some data from the following papers:
# 1. "Conductivity of molten NaCl and its supercritical values in strong dc 
# electric field", J. Petravic, J. Delhommelle, Journal of 
# Chemical Physics, 2013
# 2. "Shear viscosity of molten sodium chloride", J. Petravic, J. Delhommelle, 
# Journal of Chemical Physics, 2003
# 3. "Thermodynamic analysis of molecular dynamics simulation of evaporation
# and condensation", E. A. T. van der Akken, A. J. H. Frijns, A. A. van 
# Steenhoven, P. A. J. Hilbers, 5th European Thermal-Science Conference, 2006

from random import random
from matplotlib import pyplot as plt
from math import sqrt, atan, tan
pi = 3.141592
def periodicBC(x, Lx): # This function is meant to restrict the molecules in
    # the box meant for MCE .....
    return 2*Lx/pi*atan(tan(x*pi/Lx))
Np = 100 # Number of particles
Lx = 0.1 # Length of the box
Ly = Lx # Width of the box
Lz = Lx # Breadth of the box
box = [{} for k in range(Np)] # The box of particles
e = 1.6*10**(-19) # Electronic charge in Coulombs
Q = 10**(-19) # I have just an arbitrary energy constant Q in Joules
kB = 1.38*10**(-23) # Boltzmann constant in Joules per Kelvin
T = 1200 # Temperature in Kelvin, 1074K is the melting point of NaCl
Nsteps = 100 # Number of time steps
delt = 10**(-6) # Each time step is of about 1 us
epsilon_0 = 8.85*10**(-12) # Vaccuum permittivity in Farads per meters
eta = 7.82*10**(-4) # dynamic viscosity of molten NaCl
# Half of the particles in the box are Na+
xi = random() # dragging/pumping coefficient of the particle
for k in range(int(Np/2)):
    box[k]['m'] = 3.82*10**(-26) # mass of an Na+ ion in kg
    box[k]['q'] = 1
    box[k]['R'] = 102*10**(-12) # ionic radius of Na+ is 102 pm
    box[k]['r'] = [
        (random()-0.5)*Lx,(random()-0.5)*Ly,(random()-0.5)*Lz
        ] # position of the particle
    box[k]['v'] = [random(),random(),random()] # velocity of the particle
for k in range(int(Np/2),Np):
    box[k]['m'] = 5.81*10**(-26) # mass of an Cl- ion in kg
    box[k]['q'] = -1 # mass of an Cl- ion in kg
    box[k]['R'] = 181*10**(-12) # ionic radius of Cl- is 181 pm
    box[k]['r'] = [
        (random()-0.5)*Lx,(random()-0.5)*Ly,(random()-0.5)*Lz
        ] # position of the particle
    box[k]['v'] = [random(),random(),random()] # velocity of the particle
Temp = [0 for k in range(Nsteps)] # Kinetic temperature
for k in range(Nsteps):
    print(k,'->')
    xi2= 0
    for k1 in range(Np):
        v1 = 0
        for l in range(3): v1 = v1 + (box[k1]['v'][l]**2)*box[k1]['m']/2/Q
        xi2 = xi2 + delt*v1
    tem = 2*Q*v1/3/Np/kB
    xi2 = xi2 - delt*1.5*Np*kB*T/Q
    Temp[k] = tem
    for k1 in range(Np):
        print(k1,':::')
        r = [0 for l in range(3)]
        v = [0 for l in range(3)]
        for l in range(3):
            r[l] = box[k1]['r'][l] + delt*box[k1]['v'][l]
            print(r[l],end=',')
            r[l] = periodicBC(r[l],Lx)
        f1 = [0 for l in range(3)]
        for k2 in range(Np):
            if k2!=k1:
                f2 = box[k1]['q']*box[k2]['q']*e**2
                rij = [box[k2]['r'][l]-box[k1]['r'][l] for l in range(3)]
                r12 = 0
                for l in range(3): r12 = r12 + rij[l]**2
                r12 = sqrt(r12)
                print('Force',(f2/4/pi/epsilon_0/r12**3),r12)
                for l in range(3):
                    f1[l] = f1[l] + (f2/4/pi/epsilon_0/r12**3)*rij[l]
        for l in range(3):
            f1[l] = f1[l] - 6*pi*eta*box[k1]['R']*box[k1]['v'][l]
        for l in range(3):
            v[l] = box[k1]['v'][l] - delt*f1[l]/box[k1]['m']
            v[l] = v[l] - delt*xi/box[k1]['m']*box[k1]['v'][l]
            v[l] = periodicBC(v[l],3*10**6)
        for l in range(3):
            box[k1]['r'][l] = r[l]
            box[k1]['v'][l] = v[l]
    xi = xi2
plt.plot(Temp)
plt.xlabel('No of time steps')
plt.ylabel('Temperature')
plt.show()