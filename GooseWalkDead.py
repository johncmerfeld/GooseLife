import matplotlib as mpl
from matplotlib import pyplot
from matplotlib import animation as anim
import numpy as np
import sys
import random
import time

# make values from -5 to 5, for this example
length = int(sys.argv[1])
lifespan = int(sys.argv[2])
boundaries_are_continuous = int(sys.argv[3])
zvals = np.zeros((length, length), dtype = int)

x = int(np.random.random_sample() * length)
y = int(np.random.random_sample() * length)

if boundaries_are_continuous: # continuous
	for i in range(lifespan):

		zvals[x][y] = zvals[x][y]+1
		rand = np.random.random_sample()
		if rand < 0.25 :
			if x == length - 1:
				x = 0
			else: x = x + 1
		elif rand < 0.5 :
			if x == 0:
				x = length - 1
			else: x = x - 1
		elif rand < 0.75 :
			if y == length - 1:
				y = 0
			else: y = y + 1
		else:
			if y == 0:
				y = length - 1
			else: y = y - 1

else: # discrete
	for i in range(lifespan):

		zvals[x][y] = zvals[x][y]+1
		rand = np.random.random_sample()
		if rand < 0.25 :
			if x == length - 1:
				continue
			else: x = x + 1
		elif rand < 0.5 :
			if x == 0:
				continue
			else: x = x - 1
		elif rand < 0.75 :
			if y == length - 1:
				continue
			else: y = y + 1
		else:
			if y == 0:
				continue
			else: y = y - 1

# make a color map of gradient colors
cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                           ['black','green','white'],
                                           256)
bounds=[0,0,10,10]
norm = mpl.colors.BoundaryNorm(bounds, cmap2.N)

# tell imshow about color map so that only set colors are used
img2 = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap2,
                    origin='lower')

# make a color bar
pyplot.colorbar(img2,cmap=cmap2,
                norm=norm,boundaries=bounds,ticks=[-5,0,5])

pyplot.colorbar(img2,cmap=cmap2)
pyplot.show()
