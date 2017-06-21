import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set up plotting style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# set up plot
fig, ax = plt.subplots(1,1)
ax.set_xlabel('Cross-sectional area(µ$^2$)')
ax.set_ylabel('Counts')
bins = np.arange(1700, 2501, 50)

# plot the data as a histogram by bins
ax.hist((xa_low), bins = bins, alpha = 0.5)
ax.hist((xa_high), bins = bins, alpha = 0.5)
plt.show()

# save figure
fig.savefig('plotting.PDF', dpi = 600, transparent = True)
