# Applying Nose-Hoover thermostat to an MCE of ions
# in molten NaCl with periodic boundary conditions
#                                     - Shrohan Mohapatra
#                                     University of Massachusetts, Amherst

# The methodology uses Euler forward integration technique ....
# ri(t+del t) = 2ri(t) - ri(t-del t) + (del t)^2 fi(t)/m
# vi(t) = (ri(t+del t)-ri(t-del t))/(2 del t)
# fi = sum_{j} (q_i q_j e^2)/(4 pi eps_0 |r_ij|^3) r_ij - 6 pi mu Ri vi
# + f~/(t), f~(t) being a random Gaussian motion .....

# Here for molten NaCl I am borrowing some data from the following papers:
# 1. "Conductivity of molten NaCl and its supercritical values in strong dc 
# electric field", J. Petravic, J. Delhommelle, Journal of 
# Chemical Physics, 2013
# 2. "Shear viscosity of molten sodium chloride", J. Petravic, J. Delhommelle, 
# Journal of Chemical Physics, 2003
# 3. "Thermodynamic analysis of molecular dynamics simulation of evaporation
# and condensation", E. A. T. van der Akken, A. J. H. Frijns, A. A. van 
# Steenhoven, P. A. J. Hilbers, 5th European Thermal-Science Conference, 2006

# (Under algorithm sketch ....)