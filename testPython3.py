import numpy, matplotlib, sympy
print('NoErrorIfPrinted')
from IPython.display import YouTubeVideo
# a short video about using NumPy arrays, from Enthought
YouTubeVideo('vWkb7VahaXQ')
myvals = numpy.array([1, 2, 3, 4, 5])
print(myvals[0:3])
print(numpy.linspace(0,5,11))
a, b, c = sympy.symbols('a b c')
