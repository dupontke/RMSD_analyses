#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
##!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:
# from distance_functions import *

# PREAMBLE:

import numpy as np

sqrt = np.sqrt
sums = np.sum
square = np.square
zeros = np.zeros

# SUBROUTINES:

def RMSD(x,y):
	""" Calculates the Root Mean Squared Distance between two arrays of the same size

	Usage: rmsd = RMSD(x,y)

	Arguments:
	x, y: numpy arrays with the same shape
	
	"""
	
	return sqrt(sums(square(x-y))/len(x))

def MSD(x,y):
	""" Calculates the Root Mean Squared Distance between two arrays of the same size

	Usage: msd = MSD(x,y)

	Arguments:
	x, y: numpy arrays with the same shape
	
	"""

	return sums(square(x-y))/len(x)

def wrapping(x,dim):
	""" Calculates the translation matrix needed to wrap a particle back into the original periodic box
	
	Usage: t = wrapping(x,dim)

	Arguments:
	x: a numpy array of size (3) that corresponds to the xyz coordinates of an ATOM/COM/COG of a residue
	dim: a numpy array of size (3) that holds the xyz dimensions of the periodic box at that timestep

	"""
	
	t = zeros(3)
	dim2 = dim/2.
	for i in range(3):
		if (x[i]<-dim2[i]) or (x[i]>dim2[i]):
			t[i] = -dim[i]*round(x[i]/dim[i])
	return t

def Euclid_distance(x,y,dist2=False):
	""" Calculates the Euclidian Distance between two arrays of the same size

	Usage: dist = Euclid_distance(x,y)

	Arguments:
	x, y: numpy arrays with the same size
	dist2: if False, this function will not output the dist2 value; if True, this function will output the distance as well as the distance^2 values (allows for variance/standard deviation analyses)

	"""

	if dist2 == True:
		x2 = sums(square(x-y))
		x = sqrt(x2)
		return x, x2

	else:
		return sqrt(sums(square(x-y)))

