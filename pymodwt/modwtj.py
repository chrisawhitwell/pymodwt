'''
Originally created on May 16, 2013 by A. Cimatoribus

'''

import numpy as np
DTYPE = np.float64

def modwtj(Vin, j,  ht, gt):
    """
    MODWT transform pyramid algorithm
    see pag.178 WMTSA
    """

    N = Vin.shape[0]
    L = ht.shape[0]
    Wout = np.zeros(N, dtype=DTYPE)
    Vout = np.zeros(N, dtype=DTYPE)

    if L!=gt.shape[0]: raise ValueError('filters ht and gt must have the same length')
    
    for t in range(N):
        k = t
        Wout[t] = ht[0] * Vin[k]
        Vout[t] = gt[0] * Vin[k]
        for n in range(1,L):
            k -= 2**(j - 1)
            if (k < 0):
                k = k%N
            Wout[t] += ht[n] * Vin[k]
            Vout[t] += gt[n] * Vin[k]
    return Wout, Vout

def imodwtj(Win, Vin, j, ht, gt):
    """
    MODWT inverse transform pyramid algorithm
    see pag.178 WMTSA
    """

    N = Vin.shape[0]
    L = ht.shape[0]
    Vout = np.zeros(N, dtype=DTYPE)

    if L!=gt.shape[0]: raise ValueError('filters ht and gt must have the same length')
    
    for t in range(N):
        k = t
        Vout[t] = (ht[0] * Win[k]) + (gt[0] * Vin[k])
        for n in range(1,L):
            k += 2**(j - 1)
            if (k >= N):
                k = k%N
            Vout[t] += (ht[n] * Win[k]) + (gt[n] * Vin[k])
    return Vout
