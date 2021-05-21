from scipy.optimize import curve_fit
from random import random as randReal
from matplotlib import pyplot
from numpy import random, linspace
def modelFunc1(x,*A):
    s, p = 0, 1
    for k in range(len(A)):
        s = s + A[k]*p
        p = p * x
    return s
def modelFunc2(x,A):
    s, p = 0, 1
    for k in range(len(A)):
        s = s + A[k]*p
        p = p * x
    return s
numberOfPoints = 100
guessDegree = 10
guessPoly = [randReal() for k in range(guessDegree)]
x = linspace(1,numberOfPoints,numberOfPoints)
graph = random.uniform(-5,5,numberOfPoints)
pyplot.plot(x,graph)
fit = curve_fit(modelFunc1,x,graph,guessPoly)
graphFit = modelFunc2(x,fit[0])
pyplot.plot(x,graph)
pyplot.plot(x,graphFit)
pyplot.legend(['original','fitCurve'])
pyplot.show()
