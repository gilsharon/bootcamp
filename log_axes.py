import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set up plotting style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#load data
data = np.loadtxt('data/collins_switch.csv', skiprows = 2,
                    delimiter=',')
iptg = data[:,0]
norm_gfp = data[:,1]
norm_gfp_sem = data[:,2]

# make figure
fig, ax = plt.subplots(1,1)
ax.set_xlabel('[IPTG] (mM)')
ax.set_ylabel('Normalized GFP expression (A.U.)')
ax.set_xscale('log')

ax.errorbar(iptg, norm_gfp,norm_gfp_sem, marker='.', markersize=10, linestyle='none')
plt.show()
