# Question 3b from Assignment 5
# Composite trapezoidal rule for different number of subintervals

import numpy as np
import matplotlib.pyplot as plt

from CompTrapA5 import CompTrap

#  define function

def f(x):
    return np.exp(np.sin(x)+1)


# define and initialize variables

a = 0.0
b = 2.0

kmax = 10
M = 2
h = (b - a)/float(M)

h_all = np.zeros(kmax)
Error_all = np.zeros(kmax)


#  compute trapezoidal approximation for all number of subintervals 
#    (i.e. loop through all number of subintervals)  

I_prev = CompTrap(f,a,b,M)


for k in range(kmax):
    M = M * 2
    h = (b -a)/float(M)
    Itrap = CompTrap(f,a,b,M)
    print(f'The approximation is {Itrap:.8f} with {M} subintervals')
    h_all[k]= h
#    Error_all[i] = abs(Itrap-I_final)
    Error_all[k] = abs(Itrap-I_prev)
    I_prev = Itrap


#  plot your results

plt.loglog(h_all,Error_all)
plt.title('$O(h^2)$ Error using composite trapezoidal rule')
plt.xlabel('h')
plt.ylabel('approximate error')
plt.legend(['linear on log-log with slope 2'])
plt.show()
