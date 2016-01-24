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
<img src="/nleehone/RMgSn_Transferred_Hyperfine_field/raw/master/plots/NdMgSn_4K.png?raw=true" alt="NdMgSn 4K" title="NdMgSn T=4K" style="max-width:250px;">