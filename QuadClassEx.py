
import numpy as np
from scipy import integrate

def f(x,p):
    return np.sqrt(1+x**p)

a = 0.0
b = 1.0

p=2

#I_out = integrate.quadrature(f,a,b)
I_out = integrate.quad(f,a,b, args=(p))

print(I_out)
