# Starter code for Python function for finding 
#   Condition number of specified matrix as
#     a function of the parameter a

import numpy as np

def CondNumFunc(a): 
    
    A = np.array([[1,2,4],[3,a,1],[1,-2,3]])
    K = np.linalg.cond(A)
    
    return K    # Condition Number of specified matrix



