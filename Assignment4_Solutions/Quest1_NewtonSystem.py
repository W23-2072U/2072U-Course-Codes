import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt          # For plotting 

from NewtSysSolve import NewtSysSolve
from NonLinEqnsA4 import NonLinEqns
from JacobianA4 import Jacobian


# def f(x):                                       #  defines the function 
#     x1 = x[0]
#     x2 = x[1]
#     f1=x1*x2**2 + x1**2*x2 + x1**3 - 1.0
#     f2=x1**3*x2**2 - 2.0*x1**5*x2-x1**2 + 1.0
#     fval = np.array([f1,f2])
#     return fval

# def Df(x):                                      #  defines the Jacobian
#     x1 = x[0]
#     x2 = x[1]    
#     J11 = x2**2 + 2.0*x1*x2 + 3.0*x1**2 
#     J12 = 2.0*x1*x2 + x1**2
#     J21 = 3.0*x1**2*x2**2 - 10.0*x1**4*x2-2.0*x1
#     J22 = 2.0*x1**3*x2 - 2.0*x1**5
#     Jac = np.array([[J11,J12],[J21,J22]])
#     return Jac


# Parameters of Newton iteration
epsf = 1.0e-9
epsx = 1.0e-12
itmx = 15
# Initial guess
x0 = np.ones((2,1))

#  call Newton iteration function NewtSysSolve defined in NewtonSystemIteration.py
x, err, res, its = NewtSysSolve(NonLinEqns,Jacobian,x0,epsx,epsf,itmx)

print('\n')
print('The solution is: \n'+str(x))
print(f'That is, we have x1 = {x[0,0]:.8f}, x2 = {x[1,0]:.8f}')
print('\n')


plt.figure
plt.semilogy(range(0,its),err[0:its],'-*k')
#plt.semilogy(range(0,its),res[0:its],'-*r')
plt.xlabel('Nr. of iterations')
plt.ylabel('approximate error')
plt.title('Convergence of Newton Iterations for System (Question 1)')
plt.show()


