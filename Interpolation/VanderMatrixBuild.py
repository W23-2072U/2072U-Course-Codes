
#  Build the Vandermonde matrix given
#    the interpolating points

import numpy as np

def VanderMatrix(xs):    # xs is an array with interpolating points

    Np1 = xs.shape[0]       # to determine size of Vandermonde matrix (N+1 x N+1)
    V = np.ones((Np1,Np1))  #  initialize V to a matrix of ones

    for i in range(Np1):         #  loop over rows of V
        for j in range(1,Np1):   #  loop over columns 2 to N+1 of V
            V[i,j] = V[i,j-1]*xs[i]

    return V

#  also need a function for evaluating the interpolant
#   our Vandermonde matrix is organized differently
#   than np.vander (backwards), so we need to evaluate the interpolant
#   in a different way

def MonoPolyEval(a_coeff,xx):

    Np1 = a_coeff.shape[0]   # get degree (+1) of polynomial

    p = 1             #  p will hold value of x**j
    q = a_coeff[0]    #  q will hold value of polynomial; initialize to first term (i.e. x**0 term)

    for j in range(1,Np1):
        p = p*xx  #  gives x**j
        q = q + a_coeff[j]*p   # adding a_j x**j to the running sum

    return q
