import numpy as np
import os
import sys
import readParameters

def g(alpha, beta):
    a, Delta, N = readParameters.readParameters()
    s = 0
    for k in range(1, N+1):
        s = s + ((0.5 + N - k)*alpha + beta)/np.sqrt(1 + ((0.5 + N - k)*alpha + beta)**2)
    return s

def gx(x, y):
    a, Delta, N = readParameters.readParameters()
    s = 0
    for k in range(1, N+1):
        c = (0.5 + N - k) * x + y
        s += (0.5 + N - k) * (1 + c**2)**(-1.5)
    return s

def gy(x, y):
    a, Delta, N = readParameters.readParameters()
    s = 0
    for k in range(1, N+1):
        c = (0.5 + N - k) * x + y
        s += (1 + c**2)**(-1.5)
    return s

