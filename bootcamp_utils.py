import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ecdf(filename):
    '''
    template for ECDF plotting
    '''

    # load data
    xa_high = np.loadtxt(filename, comments='#')

    #calculate X and Y values for ECDF
    #rank order data for X, assign Y value as same spacing from 0 - 1
    fig, ax = plt.subplots(1,1)
    ax.set_ylabel('ECDF')
    ax.set_xlabel('Cross-sectional Area')

    high_x = np.sort(xa_high)
    high_y = np.arange(1,len(xa_high)+1)/ len(xa_high)

    ax.plot(high_x, high_y, marker = '.', linestyle = 'none')

    plt.show()
