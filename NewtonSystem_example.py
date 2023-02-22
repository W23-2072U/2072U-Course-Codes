import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt          # For plotting 

def NewtSysSolve(f,Df,x0,epsx,epsf,itmx):                      # Newton iteration for systems of nonlinear equations

    conv = False                                               # Set convergence flag
    err=np.ones(itmx)
    res=np.ones(itmx)
    x = x0                                                     # Sets starting point as initial guess x0
    
    for k in range(0,itmx):                                    # Loop over Newton iterates
        
        r_vec = -f(x)                                          # Compute residual vector
        res[k] = scipy.linalg.norm(r_vec,2)                    # Compute residual
        J = Df(x)                                              # Evaluate Jacobian
        
        dx = scipy.linalg.solve(J,r_vec)                        # solve system J dx = -f

        err[k] = scipy.linalg.norm(dx,2)                       # Estimate of error
        
        print(f'Iter. {k}, err = {err[k]:.4e}, res = {res[k]:.4e}' )    # Print error and residual
        
        x = x + dx                                             # Apply update step
        
        if res[k] < epsf and err[k] < epsx:                    # Test for convergence
            conv = True
            its = k+1
            print("Converged, exiting...")
            break


    if conv==False:
        print("No convergece!")
        its=itmx

    return x,err,res,its


def f(x):                                       #  defines the function 
    x1 = x[0]
    x2 = x[1]
    f1=2.0*np.exp(x1*x2) - 2.0*x1 + 2.0*x2 - 2.0
    f2=x1**5 + x1*x2**5 - 2.0*x2
    fval = np.array([f1,f2])
    return fval

def Df(x):                                      #  defines the Jacobian
    x1 = x[0]
    x2 = x[1]    
    J11 = 2.0*np.exp(x1*x2)*x2 - 2.0
    J12 = 2.0*np.exp(x1*x2)*x1 + 2.0
    J21 = 5.0*x1**4 + x2**5
    J22 = 5.0*x1*x2**4 - 2.0
    Jac = np.array([[J11,J12],[J21,J22]])
    return Jac


# Parameters of Newton iteration
epsf = 1.0e-9
epsx = 1.0e-12
itmx = 15
# Initial guess
x0 = np.ones((2,1))

#  call Newton iteration function NewtSysSolve defined in NewtonSystemIteration.py
x, err, res, its = NewtSysSolve(f,Df,x0,epsx,epsf,itmx)

print('\n')
print('The solution is: \n'+str(x))
print(f'That is, we have x1 = {x[0,0]:.8f}, x2 = {x[1,0]:.8f}')
print('\n')


print("Note the solution is not [0,0] as expected.  \n Try a different guess to see if you get the zero solution instead")

plt.figure
plt.semilogy(range(0,its),err[0:its],'-*k')
#plt.semilogy(range(0,its),res[0:its],'-*r')
plt.xlabel('Nr. of iterations')
plt.ylabel('residual (red) and error (black)')
plt.title('Convergence for 2 x 2 test problem')
plt.show()


