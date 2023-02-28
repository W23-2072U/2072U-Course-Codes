# function for computing the matrix vector product 
#    where L is a unit lower triangular matrix

import numpy as np

def LowTriangMatVec(A,x):
    
    n = A.shape[0]  #  get number of rows/columns
    c = np.zeros((n,1))   # initialize resultant vector
    
    for j in range(n):
        
        c[j] = x[j]
        
        for k in range(0,j):
            
            c[j]=c[j]+A[j,k]*x[k]
            
    return c    # c = Ax
