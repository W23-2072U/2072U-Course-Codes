#  Starter code for Question 2 of Assignment 3 
#  analysis of linear systems involving Vandermonde matrix


import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

#  import function you wrote for solving linear systems
from LUPsolveA3 import LUPsolve

# initialize variables

Nfirst = 15
Nlast = 40
cond_num = np.zeros(Nlast-Nfirst+1)
err = np.zeros(Nlast-Nfirst+1)
maxerr = np.zeros(Nlast-Nfirst+1)

N_list = range(Nfirst,Nlast+1)

# loop over matrix sizes

for N in N_list:
    
    # Define the grid. Condition number grows with the number of grid points.
    xs=np.linspace(-1,1,N+1)       # Regular grid on [-1,1] with N points.

   # call vander to get V

    V = np.vander(xs)
    
   # form the vector c (the right hand side of the equation Vx=c)

    c = V[:,N-1]

   # call LUPsolve to get x

    x,L,U,P = LUPsolve(V,c)

   # compute the error and record 

    x_exact = np.zeros(N+1)
    x_exact[N-1]=1  

    err[N-Nfirst]=scipy.linalg.norm(x_exact-x,2)

   # compute the max relative error and record
    
    cond_num[N-Nfirst] = np.linalg.cond(V)
    
    maxerr[N-Nfirst]=cond_num[N-Nfirst]*scipy.linalg.norm(V@x - c,2)/scipy.linalg.norm(c,2)
    
    
#print(N_list)
#print(cond_num)
#print(err)

# plot error and max relative error versus the matrix size on a logarithmic scale on the y-axis (semilogy) 

plt.semilogy(N_list,err,'b')
plt.semilogy(N_list,maxerr,'r')
plt.title('Error for Solution of Vandermonde System Vx=c')
plt.xlabel('N')
plt.ylabel('relative error')
plt.legend(['true relative error','max relative error'])
plt.show()






