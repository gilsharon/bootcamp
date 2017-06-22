import numpy as np
import os
# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

def dot_ecdf(data):
    '''
    return x , y values for a dor ecdf
    '''
    x = np.sort(data)
    y = np.arange(1,len(data)+1)/ len(data)
    return x,y

def ecdf(data, formal=False, buff=0.1, min_x=None, max_x=None):
    """
    Generate `x` and `y` values for plotting an ECDF.

    Parameters
    ----------
    data : array_like
        Array of data to be plotted as an ECDF.
    formal : bool, default False
        If True, generate `x` and `y` values for formal ECDF.
        Otherwise, generate `x` and `y` values for "dot" style ECDF.
    buff : float, default 0.1
        How long the tails at y = 0 and y = 1 should extend as a
        fraction of the total range of the data. Ignored if
        `formal` is False.
    min_x : float, default None
        Minimum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    max_x : float, default None
        Maximum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.

    Returns
    -------
    x : array
        `x` values for plotting
    y : array
        `y` values for plotting
    """
    x = []
    y = []
    data = np.sort(data)
    if formal == False:
        print('DOT!!')
        return dot_ecdf(data)
    else:
        print('Formal!!')
        if min_x != None:
            data = data[data > min_x]
        if max_x != None:
            data = data[data < max_x]
        step = 1 / len(data)
        curr_y = 0
        ends_buffer = (data.max() - data.min()) * buff
        for point in data:
            x += [point, point]
            y += [curr_y, curr_y + step]
            curr_y += step
        if min_x == None:
            x = [data.min() - ends_buffer] + x
            y = [0] + y
        if max_x == None:
            x = x + [data.max() + ends_buffer]
            y = y + [1]
    return x, y, data

def plot_ecdf(x,y,data):
    '''
    plot ecdf by x, y
    '''
    print(len(x),len(y))
    print(len(data))
    fig, ax = plt.subplots(1,1)
    ax.plot(x, y, marker = 'None', linestyle = 'solid')
    x_dot, y_dot = dot_ecdf(data)
    ax.plot(x_dot, y_dot, marker = '.', linestyle = 'None')
    #plt.show()

def ecdf_by_choice(data, formal=False, buff=0.1, min_x=None, max_x=None):
    x, y, data = ecdf(data, formal, buff, min_x, max_x)
    plot_ecdf(x,y,data)
    plt.show()
