import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import sys

if len(sys.argv) < 3:
    print('Program requires at least two argument. E.g.:\npython3 RMgSn_Transferred_Bhf_plot.py results.dat out.png {KDE bandwidth}"')
    exit()

data = np.loadtxt(open(sys.argv[1], 'rb'), delimiter=',')

kde_bandwidth = float(sys.argv[3]) if len(sys.argv) > 3 else 0.05

density = gaussian_kde(data, kde_bandwidth)
xs = np.linspace(0, max(data) + 1,200)

plt.plot(xs/max(xs), density(xs))
plt.xlabel('B$_{hf}$/B$_{max}$')
plt.ylabel('P(B)')

plt.savefig(sys.argv[2])