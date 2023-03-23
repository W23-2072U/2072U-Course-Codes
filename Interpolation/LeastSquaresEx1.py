
# linear least-squares

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


#  builds the matrix for the linearsystem that defines the coefficients 
#    (this matrix is refered to as V in the final slide of Lecture 19)
def LS_Matrix(xd):
    
    N = xd.shape[0]

    A = np.zeros((N,2))
    
    A[:,0] = np.ones(N)      #   first column of A
    A[:,1] = xd              #   second column of A 
    
    print(A.shape)
    
    return A


#  the data
xd =  np.array([0.1,  0.9,    1.3,    2.1,    2.6,  3.1,   4.0 ])
yd =  np.array([ 0.88,    1.08,    1.37,    1.50,    1.63,  1.91,   2.02  ])


#  gets the matrix
A = LS_Matrix(xd);

#  compute matrices for the least-squares system  A^T A x = A^T y
M = A.T @ A
b = A.T @ yd

#  solve for least-squares approximation 
xstar = scipy.linalg.solve(M,b)

print(xstar)

#  or get least-squares solution directly from A and yd using scipy
#xstar,res, rnk,s = scipy.linalg.lstsq(A,yd)


#  for plotting least-squares approximation
xx = np.linspace(0,4)
yy = xstar[0] + xstar[1]*xx


plt.plot(xd,yd,'o',xx,yy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Least-Squares')
plt.legend(['data','y = 0.8735 + 0.3032 x'])