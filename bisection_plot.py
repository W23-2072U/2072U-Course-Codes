
#  Bisection code as programmed in Lecture 3 (by G. Lewis and attending students)
#  Input: function f, starting points a0 and b0,
#    also need max iteration k_max, tolerances eps_x, eps_f

import numpy as np
import matplotlib.pyplot as plt


def bisect(f,a0,b0,k_max,eps_x,eps_f):
    conv = False                            # flag for convergence, default is "not converged"
    
    if ( f(a0)*f(b0) > 0):              # check to see whether we can guarantee convergence
        print('Error. f(a0) f(b0) > 0: Starting condition not satisfied.')
        return None, None, conv         # abort and print message if we can't guarantee convergence
    
    a = a0
    b = b0
    
    iteration_history = []              # to hold a list of 
    
    
    for k in range(k_max):              # loop over at most k_max bisection steps
        c = (a + b)/2.0                 # find the current midpoint
        f_mid = f(c)                    # compute the function value at the midpoint
        f_left=f(a)                     # compute the function value at the current left boundary
        if (f_mid*f_left > 0):          # if they have the same sign...
            a=c                         # update the left boundary, otherwise...
        else:
            b=c                         # update the right boundary
        max_err = abs(b-a)              # compute the maximal error and the residual
        res = abs(f_mid)
        iteration_history.append([k+1, c, max_err, res])
  
        print(f'iteration {k+1}, err={max_err:.4e} and res={res:.4e}')  # Since k starts at 0, I added 1 to k to make the first iteration 1

        if (max_err < eps_x) and (res < eps_f):     # if both are less than their tolerance, stop iterations
            conv=True                                  # set the convergence flag to "converged"
            break

    if not conv:                       # print warning if the iterations did not converge
        print(f'No convergence after {k_max} interations')
        
    it_hist = np.array(iteration_history)  # plot will need this to be an array not a list

    return c, it_hist, conv              # return the approximate solution, maximal error and convergence flag


def f(x):   
    return x**2 - 5                            # function definition of f(x), where we are solving f(x)=0
#    return np.exp(x)-x**3-3/2

a0 = 2.0                                # left end-point
b0 = 3.0                                # right end-point
k_max=100                               # maximum number of iterations
eps_x = 1.0e-6                          # tolerance on x
eps_f = 1.0                             # tolerance of function value

xstar,it_hist,conv=bisect(f,a0,b0,k_max,eps_x,eps_f)

if conv:
    print(f'\n x* = {xstar}')
    
xx = it_hist[:,0]
yy = it_hist[:,2]
#plt.plot(xx,np.log(yy))
plt.semilogy(xx,yy)

plt.xlabel('iteration (k)')
plt.ylabel('maximum error')

plt.show()




    
    
