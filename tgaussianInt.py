from sympy import *
a1, l1, x = Symbol('a1'), Symbol('l1'), Symbol('x')
k, T, Tc = Symbol('k'), Symbol('T'), Symbol('Tc')
n = Symbol('n')
facts = Q.positive(l1)
with assuming(Q.positive(l1)):
	print(
		integrate(exp(-1/2*a1**2*l1),(a1,-oo,oo))
		)
print(Sum(x**k/factorial(k),(k,0,oo)).doit())
print(series(exp(x**2/2),x, 0, 7))
print(simplify(Derivative((Tc - T)**(2*n/(2*n-2)), T, T).doit()))
r, phi, d, n = symbols('r phi d n')
print(
	simplify(
		integrate(sin(phi)**n,(phi,0,pi))
	)
)
print(
	simplify(
		integrate(cos(phi)**n*sin(phi)**(d-2),(phi,0,pi))
	)
)
