# Configuration file for TbMgSn at T=4 K with sine wave magnetic moments
# The k-vector is (0.828, 0, 0) (incommensurate)

import numpy as np
from numpy import sin, cos, abs, sign, pi

Degree = pi/180.0

a = 4.359  # a lattice constant (Angstrom)
b = 4.359  # b lattice constant (Angstrom)
c = 15.798  # c lattice constant (Angstrom)
z_R = 0.333  # Position of the rare earth atom in cell units
z_Sn = 0.136  # Position of the Sn atom in cell units

num_cells_a = 10000  # Number of unit cells to create along a
num_cells_b = 1  # Number of unit cells to create along b
num_cells_c = 1  # Number of unit cells to create along c

# Description of the magnetic structure
kvector = (0.828, 0, 0)
theta_c = 90 * Degree
theta = 0 * Degree
phi = 0 * Degree

# Phases of the magnetic atoms. Use the 'pos' line to determine which phase to associate with each atom
R_ph1 = 0  # pos: (i*a, j*b, (z_R + k)*c)
R_ph2 = 0.5  # pos: ((0.5 + i)*a, (0.5 + j)*b, (0.5 + z_R + k)*c)
R_ph3 = 0.5  # pos: (i*a, j*b, (1 - z_R + k)*c)
R_ph4 = 0  # pos: ((0.5 + i)*a, (0.5 + j)*b, (0.5 - z_R + k)*c)
# Pack the phases into a tuple for better looping in the program
R_phases = (R_ph1, R_ph2, R_ph3, R_ph4)


# Size of the rare earth moment
R_moment_mag = 7
# Standard deviation to apply to the rare earth moment magnitude (Gaussian random deviation)
R_moment_stdev = 0.5

# How far to look for nearest neighbours (Angstrom)
nearest_neighbour_radius = 3.5

# Calculate basis vectors from the given angles
v1 = np.array((0, 0, cos(theta_c)))
v2 = np.array((sin(theta_c), 0, 0))
v3 = np.array((0, sin(theta_c), 0))
# Rotation matrices in 3D
rot_y = np.array(((cos(theta), 0, sin(theta)), (0, 1, 0), (-sin(theta), 0, cos(theta))))
rot_z = np.array(((cos(phi), -sin(phi), 0), (sin(phi), cos(phi), 0), (0, 0, 1)))
rot = np.dot(rot_z, rot_y)

V1 = np.dot(rot, v1)
V2 = np.dot(rot, v2)
V3 = np.dot(rot, v3)

if theta_c == 0:
    basis_R = V1 + V2 + V3
    basis_I = np.zeros(3)
else:
    basis_R = V3
    basis_I = -V2


def F(index, kvector, phi):
    return cos(-2*pi*(np.dot(kvector, index) + phi))


def R_moment(i, j, k, phi):
    return np.random.normal(R_moment_mag, R_moment_stdev)*np.real((basis_R + 1.j*basis_I)*F((i,j,k), kvector, phi))