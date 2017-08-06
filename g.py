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

delta = 1.e-6
def gx(x, y):
    return (g(x + delta, y) - g(x, y))/delta

def gy(x, y):
    return (g(x, y+delta) - g(x, y))/delta

def main():
    print g(1,2)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
