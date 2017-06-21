import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set up plotting style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

x_values = np.linspace(-2*np.pi, 2*np.pi, 250)
y_values = np.sin(x_values)

# set up plot
fig, ax = plt.subplots(1,1)
ax.set_xlabel('X')
ax.set_ylabel('Sin(X)')
ax.set_xticks(np.pi*np.array([-2, -1, 0, 1, 2]))
ax.set_xticklabels(np.array(['-2π', '-π', '0', 'π', '2π']))
# plot
ax.plot(x_values, y_values, marker = '.', linestyle = 'none')

plt.show()
