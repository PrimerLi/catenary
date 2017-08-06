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

delta = 1.e-6        
def fx(x, y):
    return (f(x + delta, y) - f(x, y))/delta

def fy(x, y):
    return (f(x, y + delta) - f(x, y))/delta
