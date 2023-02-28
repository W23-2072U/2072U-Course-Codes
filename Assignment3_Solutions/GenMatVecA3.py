
# matrix-vector multiplication for a square matrix
# implementation of psuedo-code from Lecture 8 Slides

import numpy as np

def GenMatVec(A,x):
    
    n = A.shape[0]  #  get number of rows/columns
    c = np.zeros((n,1))   # initialize resultant vector
    
    for j in range(n):
        
        c[j] = A[j,0]*x[0]
        
        for k in range(1,n):
            
            c[j]=c[j]+A[j,k]*x[k]
            
    return c   # c = Ax


# A = np.array([[1,2,4],[3,3,1],[1,-2,3]])
# x = np.array([[3,2,-1]])
    
# c = GenMatVec(A,x)
    
# print(c)

# x = np.array([3,2,-1])
    
# print(A@x)
    
    
