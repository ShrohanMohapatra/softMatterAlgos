from matplotlib import pyplot
import numpy
fileHandler = open('StokesBubble05.txt')
fig = pyplot.figure()
ax = fig.gca(projection='3d')
pts = []
for lines in fileHandler.readlines():
	xTxt, yTxt, zTxt = lines.split(' ')
	zTxt1 = zTxt.split('\n')[0]
	print(xTxt,' <> ',yTxt,' <> ',zTxt1)
	pts.append((float(xTxt),float(yTxt),float(zTxt1)))
for p in pts:
    ax.scatter(p[0], p[1], p[2], zdir='z', c='r')
pyplot.show()
