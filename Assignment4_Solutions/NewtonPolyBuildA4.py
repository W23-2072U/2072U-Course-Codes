
#  Newton polynomials for interpolation

import numpy as np


def NewtonPolyBuild(xs):
    
    Np1=xs.shape[0]
    V = np.zeros((Np1,Np1))
    
    for i in range(0,Np1):
        
        V[i,0] = 1
        
        for j in range(1,i+1):
            V[i,j] = V[i,j-1]*(xs[i]-xs[j-1])
    
    return V

