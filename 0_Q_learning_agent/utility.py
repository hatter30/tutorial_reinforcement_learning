import numpy as np

def movingAverage(x, N):
    y = np.zeros(len(x))
    for ctr in range(len(x)):
        y[ctr] = np.sum(x[ctr:ctr+N])
    return y/N
