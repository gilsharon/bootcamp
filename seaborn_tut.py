import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas, conventionally imported as pd

# Plotting modules and settings.

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
# get data..
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

ax = sns.swarmplot(data=df, x='ID', y='impact force (mN)', hue = 'date')
ax.set_ylabel('Force mN')
ax.set_xlabel('Frog ID')
ax.legend_.remove()

plt.show()
