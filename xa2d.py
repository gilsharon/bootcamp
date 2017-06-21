import numpy as np

def xa_to_diameter(xa):
    '''
    convert an array of cross-sectional areas to diameter
    '''
    diameter = np.sqrt((xa / np.pi)) * 2
    return diameter
