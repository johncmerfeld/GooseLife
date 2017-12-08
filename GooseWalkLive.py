#!/usr/bin/env python3
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation as anim
import numpy as np
import sys
import random

length = int(sys.argv[1])
boundaries_are_continuous = bool(sys.argv[2])

fig = plt.figure()
ax = plt.axes(xlim=(0, length-1), ylim=(0, length-1))
arr = np.zeros((length, length), dtype = int)

cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                                    ['black','green','white'],
                                                    256)
bounds=[0,0,10,10]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

im = plt.imshow(arr, interpolation='nearest',
              cmap = cmap,
              origin = 'lower',
			  vmin = 0, vmax = 255,
			  animated= True)

x = int(np.random.random_sample() * length)
y = int(np.random.random_sample() * length)

def walk_c():
	global x, y
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
	return

def walk_d():
	global x, y
	rand = np.random.random_sample()
	if rand < 0.25 :
		if x == length - 1:
			return
		else: x = x + 1
	elif rand < 0.5 :
		if x == 0:
			return
		else: x = x - 1
	elif rand < 0.75 :
		if y == length - 1:
			return
		else: y = y + 1
	else:
		if y == 0:
			return
		else: y = y - 1
	return

def stand(arr):
    global x,y
    arr[x][y] += 10
    return arr

def animate(i):
    arr=im.get_array()
    if boundaries_are_continuous:
        walk_c()
    else:
        walk_d()
    #print(a)
    arr = stand(arr)
    im.set_array(arr)
    return [im]

anim = anim.FuncAnimation(fig, animate, frames=10, interval=1, blit=True)
plt.show()
