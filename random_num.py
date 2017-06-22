import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu = 10
sigma = 1

def ecdf(data):
    '''
    return x , y values for a dor ecdf
    '''
    x = np.sort(data)
    y = np.arange(1,len(data)+1)/ len(data)
    return x,y

# Plotting modules and settings.
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

x_rnd = np.random.normal(mu,sigma,size = 10000)

#make ecdf
x, y = ecdf(x_rnd)

fig, ax = plt.subplots(1,1)
# _ = ax.plot(x, y, marker='.', linestyle='none')
ax.hist(x, bins = 100)

plt.show()
