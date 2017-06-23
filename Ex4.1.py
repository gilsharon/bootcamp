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

# df_frog = pd.DataFrame(index=['I', 'II', 'III', 'IV'],
#                        data={'age': ['adult', 'adult', 'juvenile', 'juvenile'],
#                              'SVL (mm)': [63, 70, 28, 31],
#                              'weight (g)': [63.1, 72.7, 12.7, 12.7],
#                              'species': ['cross', 'cross', 'cranwelli', 'cranwelli']})

df_frog = pd.DataFrame(data={'ID' : ['I', 'II', 'III', 'IV'],
                         'age': ['adult', 'adult', 'juvenile', 'juvenile'],
                         'SVL (mm)': [63, 70, 28, 31],
                         'weight (g)': [63.1, 72.7, 12.7, 12.7],
                         'species': ['cross', 'cross', 'cranwelli', 'cranwelli']})

concat_df = pd.merge(df, df_frog)
