import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import animation as anim
import numpy as np
import sys
import math
import random
import time

np.set_printoptions(threshold=np.nan)

length = int(sys.argv[1])
density = float(sys.argv[2])

fig = plt.figure()
ax = plt.axes(xlim=(0, length-1), ylim=(0, length-1))
arr = np.zeros((length, length), dtype = int)
for i in range(length):
	for j in range(length):
			if np.random.random_sample() <= density:
				arr[i][j] = 100

cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                                    ['black','lightgreen'],
                                                    256)
bounds=[0,0,10,10]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

im = plt.imshow(arr, interpolation='nearest',
              cmap = cmap,
              origin = 'lower',
			  vmin = 0, vmax = 255,
			  animated= True)

# r pentanimo
"""arr[1][2] = 1
arr[1][3] = 1
arr[2][1] = 1
arr[2][2] = 1
arr[3][2] = 1"""

def sum_neighbors(arr, i, j):

	left = j - 1
	right = j + 1
	below = i + 1
	above = i - 1

	if right >= length:
		right = 0
	if below >= length:
		below = 0
	if left < 0:
		left = length - 1
	if above < 0:
		above = length - 1

	the_sum = arr[below][right] + arr[i][right] + arr[above][right] + arr[below][j] + arr[below][left] + arr[i][left] + arr[above][j] + arr[above][left]
	return the_sum

# Conway rules

def update(arr):
	status_arr = np.zeros((length, length), dtype = int)

	for i in range(length):
		for j in range(length):
			# underpopulation
			if sum_neighbors(arr,i,j) < 200:
				status_arr[i][j] = 0
			# overpopulation
			if sum_neighbors(arr,i,j) > 300:
				status_arr[i][j] = 0
			# cohabitation
			if sum_neighbors(arr,i,j) == 200 and arr[i][j] == 100:
				status_arr[i][j] = 100
			# reproduction
			if sum_neighbors(arr,i,j) == 300:
				status_arr[i][j] = 100

	# update arr according to status
	for i in range(length):
		for j in range(length):
			arr[i][j] = status_arr[i][j]

	return arr

def animate(i):
    arr=im.get_array()
    arr = update(arr)
    im.set_array(arr)
    return [im]

anim = anim.FuncAnimation(fig, animate, frames=10, interval=1, blit=True)
plt.show()
