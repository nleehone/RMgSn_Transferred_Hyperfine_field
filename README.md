# Transferred Hyperfine Field Calculation for RMgSn

This is a Python implementation of the method for calculating the transferred hyperfine field at the Sn site in the tetragonal RMgSn compounds described in [N. R. Lee-Hone et al., Hyperfine Interactions **226** 309-319 (2014)](http://www.physics.mcgill.ca/~dominic/papers201x/Sn119Bhf_HypInt_226_2014_p309.pdf).

## How it works
The RMgSn_Transferred_Bhf.py script reads the configuration file and then generates Sn atoms based on the parameters in the configuration file. Then for each Sn atom, it generates the nearest neighbour rare earth atoms and assigns a magnetic moment to each based on the description in the configuration file. The moments are then vector summed and the magnitude of the vector sum is recorded.

Once the magnitude of the transferred moments has been saved the RMgSn_Transferred_Bhf_plot.py script can read the file and generate a smoothed distribution. The smoothing is done using Kernel Density Estimation (KDE) and the smoothing parameter (KDE bandwidth) can be chosen by the user. **Be careful choosing the KDE bandwidth as it can have a large effect on the final distribution.**

## Usage
### Manual:
**Calculating the distribution of transferred hyperfine fields at the Sn site:**

python3 RMgSn_Transferred_Bhf.py {config.py} {results.dat}

**Plotting the distribution:**

python3 RMgSn_Transferred_Bhf_plot.py {results.dat} {plot.png} {KDE bandwidth (optional. defaults to 0.05)}

### Automatic:
**Shell script (run.sh):**
run.sh is a convenience script that will run all the configuration files and create all the plots.
Configuration files are found in the config/ directory, the results are saved in the results/ directory, and the plots are created in the plots/ directory.

## Results
The following plots were generated using these scripts. They do not *exactly* match the plots found in the paper since the moment magnitude is modulated randomly.

#### NdMgSn T=4 K
![NdMgSn 4K](plots/NdMgSn_4K.png?raw=true "NdMgSn T=4 K")

#### HoMgSn T=4 K
![HoMgSn 4K](plots/HoMgSn_4K.png?raw=true "HoMgSn T=4 K")

#### DyMgSn T=4 K
![DyMgSn 4K](plots/DyMgSn_4K.png?raw=true "DyMgSn T=4 K")

#### DyMgSn T=14.8 K
![DyMgSn 14.8K](plots/DyMgSn_14p8K.png?raw=true "DyMgSn T=14.8 K")

#### TbMgSn Cycloidal T=4 K
![TbMgSn Cycloidal 4K](plots/TbMgSn_cycloidal_4K.png?raw=true "TbMgSn Cycloidal T=4 K")

#### TbMgSn Sine T=4 K
![DyMgSn Sine 4K](plots/TbMgSn_sine_4K.png?raw=true "TbMgSn Sine T=4 K")

#### ErMgSn k=(0.800, 0, 0) T=4 K
![ErMgSn k=(0.800, 0, 0) 4K](plots/ErMgSn_k0p8_4K.png?raw=true "ErMgSn k=(0.800, 0, 0) 4K")

#### ErMgSn k=(0.801, 0, 0) T=4 K
![ErMgSn k=(0.801, 0, 0) 4K](plots/ErMgSn_k0p801_4K.png?raw=true "ErMgSn k=(0.801, 0, 0) 4K")
