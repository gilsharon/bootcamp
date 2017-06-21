import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set up plotting style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


def ecdf(filename):
    '''
    return X and y values for ECDF plotting
    '''

    # load data
    data = np.loadtxt(filename, comments='#')

    x = np.sort(data)
    y = np.arange(1,len(data)+1)/ len(data)

    return x, y

def normality(filename):
    '''
    check normal distribution for dataset
    '''
    data = np.loadtxt(filename,comment='#')

    # Make smooth x-values
    x = np.linspace(1600, 2500, 400)

    # Compute theoretical Normal distribution
    cdf_theor = scipy.stats.norm.cdf(x, loc=np.mean(data), scale=np.std(data))
