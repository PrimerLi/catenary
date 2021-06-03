import numpy as np
import os
import sys
import readParameters

def f(alpha, beta):
    a, Delta, N = readParameters.readParameters()
    s = 0
    for k in range(1, N+1):
        s = s + 1/np.sqrt(1 + ((0.5 + N - k)*alpha + beta)**2)
    s = s - a/Delta
    return s

def fx(x, y):
    a, Delta, N = readParameters.readParameters()
    s = 0
    for k in range(1, N+1):
        c = (0.5 + N - k) * x + y
        s -= (1 + c**2)**(-1.5) * c * (0.5 + N - k)
    return s

def fy(x, y):
    a, Delta, N = readParameters.readParameters()
    s = 0
    for k in range(1, N+1):
        c = (0.5 + N - k) * x + y
        s -= (1 + c**2)**(-1.5) * c
    return s
