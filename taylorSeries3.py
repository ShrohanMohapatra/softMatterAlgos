from sympy import *
beta = Symbol('beta')
phi, gam, x, r, n, k = symbols('phi gam x r n k')
print(series(beta/(beta-I),beta,0,4))
print(integrate(exp(exp(x)),x))
#print(integrate(exp(-I*x*r*cos(phi))*sin(phi)**n,(phi,0,pi)))
#print(integrate((1-x**2)**n*exp(I*r*x),(x, -1, 1)))
m = Symbol('m')
#print(integrate(sin(x)**m,(x, 0, pi)))
#print(residue(x**(n-1)/(x**2+1)*exp(-I*k*x),x,I))
rho = Symbol('rho')
d, a, s = Symbol('d'), Symbol('a'), Symbol('s')
print(integrate(rho**n*exp(-I*rho*cos(phi)),(rho, 0, x/a)))
#pprint(integrate(rho**(d-3)*exp(-I*rho*cos(phi)),(rho, 0, x/a)))
#print(integrate((1-x**2)**((d-3)/2)*exp(-I*rho*x),(x,-1,1)))
#print(integrate((1-x**2)**n*exp(-s*x),(x,-1,1)).doit())
from matplotlib import pyplot
import numpy
sigma, gamma, u, v = 1, 4, 0.3, 3
x = numpy.linspace(0, (sigma**2*gamma**2-2*u)**2/12/v, 100)
y = numpy.sqrt((sigma**2*gamma**2-2*u)**2/6/v + numpy.sqrt(
	((sigma**2*gamma**2-2*u)**2/6/v)**2-x/3/v
	))
pyplot.plot(x, y)
pyplot.xlabel('v')
pyplot.ylabel('x*')
pyplot.xlim(0, (sigma**2*gamma**2-2*u)**2/12/v)
pyplot.ylim(0, numpy.sqrt(2*(sigma**2*gamma**2-2*u)**2/3/v))
pyplot.show()

