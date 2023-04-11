import numpy as np
import matplotlib.pyplot as plt

from CompSimpsonA5 import CompSimpson

def f(x):
    return np.exp(np.sin(x)+1)


a = 0.0
b = 2.0

kmax = 10
M = 2
h = (b - a)/float(M)

h_all = np.zeros(kmax)
Error_all = np.zeros(kmax)


I_prev = CompSimpson(f,a,b,M)


for k in range(kmax):
    M = M * 2
    h = (b -a)/float(M)
    Itrap = CompSimpson(f,a,b,M)
    print(f'The approximation is {Itrap:.16f} with {M} subintervals')
    h_all[k]= h
    Error_all[k] = abs(Itrap-I_prev)    # approximate error for previous approximation based on current approximation
    I_prev = Itrap


plt.loglog(h_all,Error_all)
plt.title('$O(h^4)$ Error using composite Simpsons rule')
plt.xlabel('h')
plt.ylabel('approximate error')
plt.legend(['linear with slope 4 on log-log plot'])
plt.show()
