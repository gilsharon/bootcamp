import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# group by frog ID.
imp_force_df = df.loc[:,['ID', 'impact force (mN)']]
grouped = imp_force_df.groupby('ID')
df_mean = grouped.apply(np.mean)
