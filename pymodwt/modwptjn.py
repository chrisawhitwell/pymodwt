
'''
Originally created on May 16, 2013 by A. Cimatoribus

'''

import numpy as np

def modwptjn(Win, j0, ht, gt):
    """
    MODWPT transform pyramid algorithm
    see pag.231 WMTSA
    """
    N = Win.shape[1]
    L = ht.shape[0]
    
    if L!=gt.shape[0]: raise ValueError('filters ht and gt must have the same length')

    for j in range(1,j0+1):
        Wout = np.ndarray((2**j,N), dtype=np.float64)
        for n in range(0,2**j,4):
            for t in range(N):
                k = t
                Wout[n,t] = gt[0] * Win[n/2,k]
                for l in range(1,L):
                    k -= 2**(j - 1)
                    if (k < 0):
                        k += N
                    Wout[n,t] += gt[l] * Win[n/2,k]
        for n in range(3,2**j,4):
            for t in range(N):
                k = t
                Wout[n,t] = gt[0] * Win[n/2,k]
                for l in range(1,L):
                    k -= 2**(j - 1)
                    if (k < 0):
                        k += N
                    Wout[n,t] += gt[l] * Win[n/2,k]
        for n in range(1,2**j,4):
            for t in range(N):
                k = t
                Wout[n,t] = ht[0] * Win[n/2,k]
                for l in range(1,L):
                    k -= 2**(j - 1)
                    if (k < 0):
                        k += N
                    Wout[n,t] += ht[l] * Win[n/2,k]
        for n in range(2,2**j,4):
            for t in range(N):
                k = t
                Wout[n,t] = ht[0] * Win[n/2,k]
                for l in range(1,L):
                    k -= 2**(j - 1)
                    if (k < 0):
                        k += N
                    Wout[n,t] += ht[l] * Win[n/2,k]
        Win = Wout
    return Wout
