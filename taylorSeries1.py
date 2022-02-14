from sympy import *
from random import randint
x, y = symbols('x y')
assert x+y
# Taylor series for addition of two functions
def productSeries(Aseries, Bseries):
	N, M = len(Aseries)-1, len(Bseries)-1
	result = [0 for k in range(M+N+1)]
	for m in range(M):
		for n in range(N):
			result[m+n] = result[m+n] + Aseries[n]*Bseries[m]
	return result
# Taylor series for composition of two functions (For f, g: R -> R, (f o g)(x) = f(g(x))
# ), f(x) = \sum_{n=0}^{N} a_n x^n, g(x) = \sum_{m = 0}^{M} b_m x^m
def compositionSeries(Aseries, Bseries):
	N, M = len(Aseries)-1, len(Bseries)-1
	result = [0 for k in range(int(M*(M+1)*N/2)+1)]
	for n in range(N+1):
		counterLoop = factorial(M+n)/factorial(n)/factorial(M)
		nk = [0 for k in range(M+1)]
		while counterLoop >= 0:
			for k in range(M+1): nk[k] = randint(0, n)
			if sum(nk)!=n: continue
			else:
				counterLoop = counterLoop - 1
				productFactorial = 1
				productCoeff = 1
				indexPower = 0
				for k in range(M+1):
					productFactorial = productFactorial*factorial(nk[k])
					productCoeff = productCoeff*(Bseries[k]**nk[k])
					indexPower = indexPower + k*nk[k]
				if indexPower < int(M*(M+1)*N/2)+1:
					summand = factorial(n)*Aseries[n]*productCoeff
					summand = summand/productFactorial
					result[indexPower] = result[indexPower] + summand
	return result

# Generating a list of coefficients in Taylor series
def seriesCoeffs(func, var, point, M):
	expansion = series(func(var), var, point, M)
	return [expansion.coeff((var-point),k) for k in range(M+1)]

# Some test cases ....
numOfCoeffs = 5
print(seriesCoeffs(tan, x, 0, numOfCoeffs))
print(seriesCoeffs(atan, x, 0, numOfCoeffs))
print(compositionSeries(
	seriesCoeffs(tan, x, 0, numOfCoeffs), 
	seriesCoeffs(atan, x, 0, numOfCoeffs)
	))
print(series(tan(atan(x)),x,0,numOfCoeffs+6))
print(seriesCoeffs(sin, x, 0, numOfCoeffs))
print(seriesCoeffs(asin, x, 0, numOfCoeffs))
print(compositionSeries(
	seriesCoeffs(sin, x, 0, numOfCoeffs), 
	seriesCoeffs(asin, x, 0, numOfCoeffs)
	))
print(series(sin(asin(x)),x,0,numOfCoeffs+6))

# Some beta tests before writing the original code to see if it works ....

# # Can I generate nth coefficient in Taylor series?
# for k in range(11):
# 	gk = series(tan(x), x, 0, 10).coeff(x, k)
# 	print('-------------------')
# 	print('Series until k = ', k, ' -> ', gk)
# 	print('-------------------')

# print(series(tan(x), x, 1, 10))

# # Just seeing if I can generate an array of variables (unknowns)
# arrIndex = [Symbol('i'+str(k)) for k in range(3)]

# for arrIndex[0] in range(2):
# 	 for arrIndex[1] in range(2):
# 	 	k, m = arrIndex[0], arrIndex[1]
# 	 	print(k,' + ',m,' = ',k+m)

# factorial(800)
# for k in range(11):
# 	gk = series(tan(x), x, 1, 10).coeff((x-1)**k)
# 	print('-------------------')
# 	print('Series until k = ', k, ' -> ', gk)
# 	print('-------------------')
