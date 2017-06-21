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

#calculate X and Y values for ECDF
#rank order data for X, assign Y value as same spacing from 0 - 1
fig, ax = plt.subplots(1,1)
ax.set_ylabel('ECDF')
ax.set_xlabel('Cross-sectional Area')

high_x = np.sort(xa_high)
high_y = np.arange(1,len(xa_high)+1)/ len(xa_high)

low_x = np.sort(xa_low)
low_y = np.arange(1,len(xa_low)+1)/ len(xa_low)

ax.plot(low_x, low_y, marker = '.', linestyle = 'none')
ax.plot(high_x, high_y, marker = '.', linestyle = 'none')

plt.show()
