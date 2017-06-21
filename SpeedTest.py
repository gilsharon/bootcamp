import numpy as np
x = np.random.random(1000)

def python_sum(x):
    x_sum = 0
    for i in x:
        x_sum += i
    return x_sum
