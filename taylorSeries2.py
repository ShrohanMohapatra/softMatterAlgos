from sympy import *
beta = Symbol('beta')
z1 = Symbol('z1')
x1 = Symbol('x1', real = True)
p = [Symbol('p'+str(k)) for k in range(5)]
expr1 = (I+beta+beta**2*z1)*(
	beta**(1/2)*(p[0]+beta*p[1]+beta**2*p[2]+beta**3*p[3]+beta**4*p[4])
	)**4 - I*beta**2*(
	beta**(1/2)*(p[0]+beta*p[1]+beta**2*p[2]+beta**3*p[3]+beta**4*p[4])
	)**2 + I*(beta**2)/4
series(expr1, beta, 0, 7)
p0Soln = solve(p[0]**4+1.0/4,p[0])
print(p0Soln)
p1Soln = [
	solve((p[0]**4-I*p[0]**2+4*I*p[0]**3*p[1]).subs(p[0],p0Soln[3]),p[1])[0],
	solve((p[0]**4-I*p[0]**2+4*I*p[0]**3*p[1]).subs(p[0],p0Soln[2]),p[1])[0],
	solve((p[0]**4-I*p[0]**2+4*I*p[0]**3*p[1]).subs(p[0],p0Soln[1]),p[1])[0],
	solve((p[0]**4-I*p[0]**2+4*I*p[0]**3*p[1]).subs(p[0],p0Soln[0]),p[1])[0],
	]
print(p1Soln)
p2Soln = [
	collect(solve(
		(
			p[0]**4*(x1+I/4)+I*p[0]**4*(4*p[2]/p[0]+6*p[1]**2/p[0]**2)+
			4*p[0]**3*p[1] -2*I*p[0]*p[1]
		).subs(
			[(p[0],p0Soln[3-k]),(p[1],p1Soln[k])]
			)
		,p[2]
	)[0], x1) for k in range(4)
]
print(p2Soln)
