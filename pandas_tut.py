

import numpy as np

# Pandas, conventionally imported as pd
import pandas as pd

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# make data
# Dictionary of top men's World Cup scorers and how many goals
wc_dict = {'Klose': 16,
           'Ronaldo': 15,
           'Müller': 14,
           'Fontaine': 13,
           'Pelé': 12,
           'Kocsis': 11,
           'Klinsmann': 11}

#convert dictionary into a Series
s_goals = pd.Series(wc_dict)

# Dictionary of nations
nation_dict = {'Klose': 'Germany',
               'Ronaldo': 'Brazil',
               'Müller': 'Germany',
               'Fontaine': 'France',
               'Pelé': 'Brazil',
               'Kocsis': 'Hungary',
               'Klinsmann': 'Germany'}

s_nations = pd.Series(nation_dict)

df_wc = pd.DataFrame({'nation':s_nations, 'goals':s_goals})
