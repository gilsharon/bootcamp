import bootcamp_utils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas, conventionally imported as pd

# Plotting modules and settings.

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
#get data
weights_df = pd.read_csv('data/bee_weight.csv', comment= '#')
sperm_df = pd.read_csv('data/bee_sperm.csv', comment= '#')

def plot_ECDF(df):
    '''
    plot ECDF of df
    '''
    fig, ax = plt.subplots(1,1)
    ax.set_xlabel('Weight (mg)')
    x, y = bootcamp_utils.ecdf(df.loc[(df['Treatment']=='Control'),'Weight'],
            formal=True)
    ax.plot(x,y,marker='.',linestyle='none')
    x, y = bootcamp_utils.ecdf(df.loc[(df['Treatment']=='Pesticide'),'Weight'],
            formal=True)
    ax.plot(x,y,marker='.',linestyle='none')
    plt.show()

#plot_ECDF(weights_df)

def plot_mean(df):
    '''
    plot mean weights with bootstrap confidence intervals
    '''
    grouped_df = df.groupby('Treatment')
    means_df = grouped_df.apply(np.mean)

    bootstrap_control = bootcamp_utils.draw_bs_reps(df.loc[df['Treatment']=='Control', 'Weight'], func = np.mean)
    bootstrap_pesticide = bootcamp_utils.draw_bs_reps(df.loc[df['Treatment']=='Pesticide', 'Weight'], func = np.mean)
    conf_int_control = np.percentile(bootstrap_control,[2.5,97.5])
    conf_int_pesticide = np.percentile(bootstrap_pesticide,[2.5,97.5])
    err_control = (conf_int_control[1] - conf_int_control[0])/2
    err_pesticide = (conf_int_pesticide[1] - conf_int_pesticide[0])/2
    yerr = [err_control,err_pesticide]
    fig, ax = plt.subplots(1,1)
    categories = [['Control'],['Pesticide']]
    y = [means_df.loc['Control']['Weight'], means_df.loc['Pesticide']['Weight']]
    ax.plot(categories, y,)
    plt.show()

plot_mean(weights_df)
