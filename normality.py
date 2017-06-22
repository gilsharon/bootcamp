import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import bootcamp_utils

# set up plotting style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#load data
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
# Make smooth x-values
x = np.linspace(1600, 2500, 400)

# Compute theoretical Normal distribution
cdf_theor_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))
cdf_theor_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))
edcf_low = bootcamp_utils.ecdf('data/xa_low_food.csv')
edcf_high = bootcamp_utils.ecdf('data/xa_high_food.csv')

fig, ax = plt.subplots(1,1, figsize=(10,4.25))
ax.set_xlabel('Cross-sectional Area')
ax.set_ylabel('ECDF')

# plot..
tcdf_low, = ax.plot(x, cdf_theor_low, color = 'gray', label = 'Low - theoretical cdf',
        marker = '.', linestyle='none')
ecdf_low, = ax.plot(edcf_low[0], edcf_low[1], label = 'Low Food',
        marker = '.', linestyle='none')
tcdf_high, = ax.plot(x, cdf_theor_high, color = 'darkgray', label = 'High - theoretical cdf',
        marker = '.', linestyle='none')
ecdf_high, = ax.plot(edcf_high[0], edcf_high[1], label = 'High Food',
        marker = '.', linestyle='none')

legend = ax.legend(loc ='lower right', handles=[tcdf_high,ecdf_high,tcdf_low,ecdf_low])
plt.show()
