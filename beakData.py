import bootcamp_utils
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Plotting modules and settings.


colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

def bs_replicate(data, func = np.mean):
    '''
    compute a bootstrap replicate from data
    '''

    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)


bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)

#bs_2012 = np.random.choice(bd_2012, replace = True, size = len(bd_2012))
n_reps = 100000
bs_reps = [bs_replicate(bd_2012, func = np.mean) for _ in list(range(n_reps))]

#x_bs, y_bs = bootcamp_utils.ecdf(bs_2012)
#
# fig, ax = plt.subplots(1, 1)
# _ = ax.set_xlabel('Beak depth (mm)')
# _ = ax.set_ylabel('ECDF')
# #_ = ax.plot(x_1975, y_1975, marker='.', linestyle='none', label='1975')
# _ = ax.plot(x_2012, y_2012, marker='.', linestyle='none', label='2012')
# _ = ax.plot(x_bs, y_bs, marker='.', linestyle='none')
# _ = ax.legend(loc='lower right')
#
# plt.show()
