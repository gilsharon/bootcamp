import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data

# group by frog ID.
imp_force_df = df.loc[:,['ID', 'impact force (mN)']]
grouped = imp_force_df.groupby('ID')
df_mean = grouped.apply(np.mean)
