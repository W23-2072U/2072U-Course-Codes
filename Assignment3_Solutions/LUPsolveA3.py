#  solves Ax=b by via the decomposition PA = LU

import numpy as np
import scipy.linalg

def LUPsolve(A,b):    # inputs n x n numpy array A, and n x 1 numpy array b

    Pt,L,U = scipy.linalg.lu(A)
    P = Pt.T
    Pb = scipy.matmul(P,b)
    y = scipy.linalg.solve_triangular(L,Pb,lower=True)
    x = scipy.linalg.solve_triangular(U,y,lower=False)
    
    return x, L, U, P     # outputs solution x, and numpy arrays L, U and P from PA = LU decomposition







