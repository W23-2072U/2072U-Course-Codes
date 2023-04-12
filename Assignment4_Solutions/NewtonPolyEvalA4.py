
#  Newton polynomials for interpolation

import numpy as np


def NewtonPolyEval(a,xs,xx):
    
    Np1=xs.shape[0]
    qj = np.ones(xx.shape)
    
    Q=a[0]*qj
    
    for j in range(1,Np1):
        qj = qj*(xx - xs[j-1])
        Q=Q+a[j]*qj
        
#    print(Q.shape)
        
    return Q