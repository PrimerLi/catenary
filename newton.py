import numpy as np
import f
import g

def newton(x0, y0):
    count = 0
    iterationMax = 20
    eps = 1.0e-16
    vector = np.zeros(2)
    J = np.zeros((2,2))
    vector[0] = x0
    vector[1] = y0
    fg = np.zeros(2)
    while (count < iterationMax):
        count = count + 1
        old = vector
        x = vector[0]
        y = vector[1]
        J[0,0] = f.fx(x, y)
        J[0,1] = f.fy(x, y)
        J[1,0] = g.gx(x, y)
        J[1,1] = g.gy(x, y)
        fg[0] = f.f(x, y)
        fg[1] = g.g(x, y)
        det = np.linalg.det(J)
        if (abs(det) < 1.e-16):
            break
        vector = vector - np.linalg.inv(J).dot(fg)
        diff = vector - old
        error = diff.dot(diff)
        #print "count = ", count, ", error = ", error, ", det = ", det
        if (error < eps):
            break
    return vector
