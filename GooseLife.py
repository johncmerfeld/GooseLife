
import numpy as np
import sys
import math
import random
import time
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan)

length = int(sys.argv[1])
max_time = int(sys.argv[2])
density = float(sys.argv[3])
speed = float(sys.argv[4])

lattice = np.zeros((length, length), dtype = int)

for i in range(length):
	for j in range(length):
			if np.random.random_sample() <= density:
				lattice[i][j] = 1

print lattice

def sum_neighbors(lattice, i, j):
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

	the_sum = 	lattice[below][right] + lattice[i][right] + lattice[above][right] + lattice[below][j] + lattice[below][left] + lattice[i][left] + lattice[above][j] + lattice[above][left]
	return the_sum

# Conway rules

for t in xrange(max_time):
	status_lattice = np.zeros((length, length), dtype = int)

	for i in xrange(length):
		for j in xrange(length):
			# underpopulation
			if sum_neighbors(lattice,i,j) < 2:
				status_lattice[i][j] = 0
			# overpopulation
			if sum_neighbors(lattice,i,j) > 3:
				status_lattice[i][j] = 0
			# cohabitation
			if sum_neighbors(lattice,i,j) == 2 and lattice[i][j] == 1:
				status_lattice[i][j] = 1
			# reproduction
			if sum_neighbors(lattice,i,j) == 3:
				status_lattice[i][j] = 1

	# update lattice according to status
	for i in xrange(length):
		for j in xrange(length):
			lattice[i][j] = status_lattice[i][j]

	time.sleep(speed)

	print lattice
