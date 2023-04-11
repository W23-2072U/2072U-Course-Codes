import numpy as np

def CompTrap(f,a,b,n):
    xs = np.linspace(a,b,n+1)
    h = (b-a)/float(n)
    I = (f(a)+f(b)) / 2.0
    for i in range(1,n):
        I = I + f(xs[i])
    I = h * I
    return I