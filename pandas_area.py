import pandas as pd
import numpy as np

#load data
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

# change titles
df_high.columns = ['high']
df_low.columns = ['low']

#concatenate dataframes (axis 1 = side by side)
df = pd.concat((df_low, df_high), axis=1)

#tidy data
df = pd.melt(df, var_name = "food density",
                value_name= "cross-sectional area (µm^2)" ).dropna()

# DONT DROP NA AFTER CONCATENATION!! YOU WOULD LOSE THE ENTIRE ROW!!

#save csv
df.to_csv('xa_combined.csv', index=False)
