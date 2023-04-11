# least-squares  question 3 from Assignment 4

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


#  builds the matrix for the system of equations
def LS_Matrix(xd):
    
    N = xd.shape[0]

    A = np.zeros((N,2))
    
    A[:,0] = np.ones(N)
    A[:,1] = xd
    
    print(A.shape)
    
    return A


#  the data

xd =  np.array([0,    0.50,    1.10,    1.30,    1.90,   2.20,    2.60,    3.10,    3.80, 4.10,    5.00])
yd =  np.array([0.98,   1.03,    1.29,    1.12,    1.44,    1.49,   1.55,    1.87,    2.06,  2.13,    2.29])


#  gets the matrix
A = LS_Matrix(xd);

#  compute matrices least-squares system
M = A.T @ A
b = A.T @ yd

#  solve for least-squares solution
xstar = scipy.linalg.solve(M,b)

print(xstar)

#  for plotting least-squares solution
xx = np.linspace(0,5)
yy = xstar[0] + xstar[1]*xx


plt.plot(xd,yd,'o',xx,yy)
plt.xlabel('x')
plt.ylabel('y')
#plt.title('Linear Least-Squares Fit to Data: y = '+str(xstar[0])+' + '+str(xstar[1])+' x')
plt.title('Linear Least-Squares Fit to Data: y = 0.8980 + 0.2880 x')
plt.legend(['data','y = 0.8980 + 0.2880 x'])