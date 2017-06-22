import numpy as np
import os
# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

fig, ax = plt.subplots(1,1)

def get_data():
    '''
    import data from the three files and read to np variable
    '''
    wt_dataset = np.loadtxt('data/wt_lac.csv', comments = '#',
                            skiprows = 3, delimiter = ',')
    q18a_dataset = np.loadtxt('data/q18a_lac.csv', comments = '#',
                            skiprows = 3, delimiter = ',')
    q18m_dataset = np.loadtxt('data/q18m_lac.csv', comments = '#',
                            skiprows = 3, delimiter = ',')

    return (wt_dataset, q18a_dataset, q18m_dataset)

def fold_change_by_IPTG(wt, q18a, q18m,ax = ax):
    '''
    plot fold change by IPTG concentration
    '''
    ax.set_xlabel('[IPTG] mM')
    ax.set_ylabel('Expression Fold Change')
    ax.set_xscale('log')
    for dataset in [wt, q18a, q18m]:
        x = dataset[:,0]
        y = dataset[:,1]
        dataset = ax.plot(x, y, marker='.', linestyle='none')


def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''
    calculate the theoretical fold Change
    c - IPTG concentration (scalar or np array)
    RK - r/k ratio (scalar)
    '''
    FC = (1 + RK * (1+c/KdA) ** 2 / \
        ((1+c / KdA) ** 2 + Kswitch * (1+c/KdI)**2))**-1
    return FC

def theoretical_fold_change_by_IPTG(ax = ax):
    '''
    plot theoretical fold change by IPTG concentration
    '''
    wt, q18a, q18m = get_data()
    fold_change_by_IPTG(wt, q18a, q18m)
    iptg = np.logspace(-5,2,1000)
    ax.set_xlabel('[IPTG] mM')
    ax.set_ylabel('Expression Fold Change')
    ax.set_xscale('log')
    for dataset in [('wt',141.5), ('q18a',16.56), ('q18m',1332)]:
        theoreticalFC = fold_change(iptg, dataset[1])
        ax.plot(iptg, theoreticalFC, marker='.', linestyle='none', label = dataset[0])
    ax.legend()
    plt.show()

def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''
    calculate the bohr parameter
    '''
    bohr = - np.log(RK) - np.log((1+c/KdA) ** 2 / \
        ((1+c / KdA) ** 2 + Kswitch * (1+c/KdI)**2))
    return bohr

def fold_change_bohr(bohr_parameter):
    '''
    calculate fold change as a factor of bohr parameter
    '''
    FC = 1/(1+np.exp(-bohr_parameter))
    return FC

def bohr_plot(ax = ax):
    '''
    plot theoretical fold change as a factor of bohr parameter
    '''
    BP = np.linspace(-6,6,200)
    theoreticalFC = fold_change_bohr(BP)
    ax.set_xlabel('Bohr Parameter')
    ax.set_ylabel('Expression Fold Change')
    ax.plot(BP, theoreticalFC, marker = '.', linestyle = 'none', color = 'gray')

def bohr_by_IPTG(ax = ax):
    '''
    calculate and plor bohr by IPTG concentration and r/k
    '''
    iptg = np.logspace(-5,2,1000)
    for dataset in [('wt',141.5), ('q18a',16.56), ('q18m',1332)]:
        BP = bohr_parameter(iptg,dataset[1])
        FC = fold_change_bohr(BP)
        ax.plot(BP, FC, marker = '.', linestyle = 'none', label = dataset[0], alpha = 0.5)
    plt.legend()
    plt.show()
