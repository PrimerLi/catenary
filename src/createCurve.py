import readParameters
import numpy as np

def createCurve(v):
    a, Delta, N = readParameters.readParameters()
    x = []
    y = []
    theta = []
    for k in range(1, N+1):
        theta.append(np.arctan((0.5 + N - k)*v[0] + v[1]))
    sx = 0
    sy = 0
    x.append(sx)
    y.append(sy)
    for i in range(len(theta)):
        sx = sx + Delta*np.cos(theta[i])
        sy = sy + Delta*np.sin(theta[i])
        x.append(sx)
        y.append(-abs(sy))
    return x, y
