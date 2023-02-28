
#  Code for computing solution of f(x) = 0 using
#    the Newton-Raphson method
#  Input: function f, its derivative fprime, and an initial guess x0
#    also need max iteration k_max, tolerances eps_x, eps_f

import numpy as np
import matplotlib.pyplot as plt

def NewtRaph(f,fprime,x0,k_max,eps_x,eps_f):
    
    conv = False                        # flag for convergence, default is "not converged"
    
    x = x0
    
    iteration_history = []              # to hold a list
    
    for k in range(k_max):              # loop over at most k_max Newton steps
        res = f(x)                      # compute the residual
        delta_x = - res/fprime(x)       # comput the Newton-Raphson update
        x = x + delta_x
           # compute the approximate error 
        err = abs(delta_x)
        iteration_history.append([k+1, x, err, res])
        
        print(f'iteration {k+1}, x* = {x:.8f}, approx error={err:.4e} and res={res:.4e}')  # Since k starts at 0, I added 1 to k to make the first iteration 1

        if (err < eps_x) and (abs(res) < eps_f):     # if both are less than their tolerance, stop iterations
            conv=True                                  # set the convergence flag to "converged"
            break

    if (conv==False):                       # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')

    it_hist = np.array(iteration_history)  # plot will need this to be an array not a list

    return x,it_hist,conv                   # return the approximate solution, maximal error and convergence flag


def f(x):                               # function definition of f(x), where we are solving f(x)=0
    return  x*np.exp(x) - 1

def fprime(x):                          # function definition of f(x), where we are solving f(x)=0
    return np.exp(x)+x*np.exp(x) 


x0 = 1.0;
k_max=1000                              # maximum number of iterations
eps_x = 1.0e-14                        # tolerance on x
eps_f = 1.0                             # tolerance of function value

xstar,it_hist,conv=NewtRaph(f,fprime,x0,k_max,eps_x,eps_f)

if (conv==True):
    print(f'\n x* = {xstar}')
    
    
xx = it_hist[:,0]
yy = it_hist[:,2]
#plt.plot(xx,np.log(yy))
plt.semilogy(xx,yy)

plt.xlabel('iteration (k)')
plt.ylabel('approx error')

plt.show()