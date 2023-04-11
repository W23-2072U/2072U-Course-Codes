import numpy as np

def CompSimpson(f,a,b,n):
    xs = np.linspace(a,b,n+1)
    h = (b-a)/float(n)
    I = 0.0
    for i in range(1,n+1):
        xbar = ( xs[i-1] + xs[i] ) / 2.0
        I = I + ( f(xs[i-1]) + 4.0* f(xbar) + f(xs[i]) )
    I = h * I / 6.0
    return I