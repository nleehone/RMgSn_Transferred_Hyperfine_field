# Transferred hyperfine field calculation based on atom positions and description of magnetic moments

import numpy as np
import sys
import os.path


if len(sys.argv) != 3:
    print("Program requires two arguments. E.g.:\npython3 RMgSn_Transferred_Bhf.py config.py output.dat")
    exit()
elif not os.path.isfile(sys.argv[1]):
    print("The configuration file you specified ({file}) does not exist.".format(file=sys.argv[1]))
    exit()


# Read the configuration file and execute the program
# This is an unsafe operation as it executes arbitrary code. Please only run configuration files you trust!
exec(compile(open(sys.argv[1], "rb").read(), sys.argv[1], 'exec'))


def add_moment(pos, Sn_pos, i, j, k, R_ph):
    """Create a moment if the position of the rare earth atom is close to the Sn atom
    pos: position or the rare earth atom
    Sn_pos: position of the Sn atom
    i, j, k: indices of the unit cell the rare earth atom is in
    R_ph: phase of the rare earth moment relative to the R1 rare earth moment (in the first unit cell)

    returns: (np.array) vector moment if within nearest_neighbour_radius, otherwise None
    """
    dist = np.linalg.norm(pos - Sn_pos)
    if dist < nearest_neighbour_radius:
        return R_moment(i, j, k, R_ph)


# Calculate the position of each Sn atom and keep track of the unit cell index (i, j, k)
Sn_positions = []
for i in range(num_cells_a):
    for j in range(num_cells_b):
        for k in range(num_cells_c):
            Sn_positions.append(((i, j, k), ((0.5 + i)*a, (0.5 + j)*b, (0.5 - z_Sn + k)*c)))
            Sn_positions.append(((i, j, k), ((0 + i)*a, (0 + j)*b, (z_Sn + k)*c)))
            Sn_positions.append(((i, j, k), ((0 + i)*a, (0 + j)*b, (-z_Sn + k)*c)))
            Sn_positions.append(((i, j, k), ((0.5 + i)*a, (0.5 + j)*b, (0.5 + z_Sn + k)*c)))
Sn_positions = np.array(Sn_positions)
Sn_positions_length = len(Sn_positions)


num_nearest_cells_a = 2*int(nearest_neighbour_radius/a) + 1
num_nearest_cells_b = 2*int(nearest_neighbour_radius/b) + 1
num_nearest_cells_c = 2*int(nearest_neighbour_radius/c) + 1


prev_completed_percent = 0
moments = []

print('Calculating Transferred Hyperfine Field for RMgSn')
print('Progress will be shown below. Please be patient if you specified a large number of cells.')

for index, ((ii, jj, kk), Sn_pos) in enumerate(Sn_positions):
    found_moment = False # Track if there are any moments within nearest_neighbour_radius
    moment = np.array((0.0, 0.0, 0.0))

    # Iterate through each unit cell that is near the Sn atom
    for i in range(int(ii - num_nearest_cells_a), int(ii + num_nearest_cells_a) + 1):
        for j in range(int(jj - num_nearest_cells_b), int(jj + num_nearest_cells_b) + 1):
            for k in range(int(kk - num_nearest_cells_c), int(kk + num_nearest_cells_c) + 1):
                # Calculate the positions of the rare earth atoms
                R_positions = ((i*a, j*b, (z_R + k)*c),
                             ((0.5 + i)*a, (0.5 + j)*b, (0.5 + z_R + k)*c),
                             (i*a, j*b, (1 - z_R + k)*c),
                             ((0.5 + i)*a, (0.5 + j)*b, (0.5 - z_R + k)*c))
                for R_pos, R_phase in zip(R_positions, R_phases):
                    m = add_moment(R_pos, Sn_pos, i, j, k, R_phase)
                    if m is not None:
                        moment += m
                        found_moment = True

    # If we did find a moment in nearest_neighbour_radius, add a moment to the list.
    # Otherwise, don't add a (0,0,0) moment
    if found_moment:
        moments.append(np.linalg.norm(moment))

    # Track the calculation progress and output to the terminal each time the percentage (rounded to int) changes
    completed_percent = int((index/Sn_positions_length) * 100)
    if completed_percent != prev_completed_percent:
        print('{completed} %'.format(completed=completed_percent))
        prev_completed_percent = completed_percent

print('Transferred Hyperfine Field Calculation - COMPLETE')
print('Results will be saved in {filename}'.format(filename=sys.argv[2]))
print('To view results, run "python3 RMgSn_Transferred_Bhf_plot.py {filename}"'.format(filename=sys.argv[2]))

np.savetxt(sys.argv[2], moments)
