import numpy as np
import newton
import readParameters as rps
import createCurve
import matplotlib.pyplot as plt

def main():
    a, Delta, N = rps.readParameters()
    v = newton.newton(0.6, -5)
    x, y = createCurve.createCurve(v)
    plt.plot(x, y, "b-o")
    plt.grid()
    plt.xlim(min(x) - 0.05, max(x) + 0.05)
    plt.ylim(min(y) - 0.05, max(y) + 0.05)
    plt.show()
    return 0

if __name__=='__main__':
    import sys
    sys.exit(main()) 

