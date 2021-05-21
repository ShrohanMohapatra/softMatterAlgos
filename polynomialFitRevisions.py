from scipy.optimize import curve_fit
from random import randint, random
from matplotlib import pyplot
from numpy import random, linspace
def modelFunc1(x,a,b,c):
    return a*x**2+b*x+c
N1 = 100
x = linspace(1,N1,N1)
graph = random.uniform(-5,5,N1)
fit = curve_fit(modelFunc1,x,graph,(1,1,2))
print(fit[0])
print(fit[1])
graphFit = modelFunc1(x,fit[0][0],fit[0][1],fit[0][2])
pyplot.plot(x,graph)
pyplot.plot(x,graphFit)
pyplot.show()
