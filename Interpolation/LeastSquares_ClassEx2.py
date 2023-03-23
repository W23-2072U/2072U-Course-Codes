
# least-squares fit using quadratic function 

import numpy as np
from numpy.random import randn
from numpy.random import seed 
import scipy.linalg
import matplotlib.pyplot as plt


#  builds the matrix for the linear system that defines the coefficients 
def LS_Matrix(xd):
    
    N = xd.shape[0]

    A = np.zeros((N,3))
    
    A[:,0] = np.ones(N)
    A[:,1] = xd
    A[:,2] = xd*xd
    
    print(A.shape)
    
    return A

#   make the data, by taking a quadratic function and adding noise
N = 100
# x coords of data
xd = np.linspace(-1,2,N)

# values of quadratic at data points
y = 1.0 + 2.0*xd - xd*xd

#  add noise
seed(1)
yd = 1.0*randn(N) + y


#  get matrix for system of equations
A = LS_Matrix(xd);

#  compute matrices for the least-squares system  A^T A x = A^T y
M = A.T @ A
b = A.T @ yd

#  solve for least-squares approximation 
xstar = scipy.linalg.solve(M,b)


#  or get least-squares solution directly from A and yd using scipy
#xstar,res, rnk,s = scipy.linalg.lstsq(A,yd)

print('the coefficients of the polynomial:')
print(np.array([1.0, 2.0, -1.0]))


print('the coefficients of the least-squares solution: \n'+str(xstar))
#print('\n the residual is '+str(res))

xx = np.linspace(-1,2)
yy = xstar[0] + xstar[1]*xx + xstar[2]*xx*xx

yy2 = 1.0 + 2.0*xx  -1.0*xx*xx


plt.plot(xd,yd,'o',xx,yy,'r',xx,yy2,'--m')
