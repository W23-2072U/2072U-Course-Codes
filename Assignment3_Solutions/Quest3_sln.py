
#  Starter code for Question 3 of Assignment 3 
# matrix-vector multiplication analysis

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt   #  for plotting
import time                       #  module for timing computations

from GenMatVecA3 import GenMatVec              # import function for general matrix-vector product
from LowTriangMatVecA3 import LowTriangMatVec  # import function for matrix-vector product with unit lower triangular matrix

wtimes_Low = []        #  initialize list for storing computation times for lower triangular matrix
wtimes_Gen = []        #  initialize list for storing computation times for lower triangular matrix
wtimes_BuiltIn = []    #  initialize list for storing computation times for built-in Python function

for k in range(7,13):   # Loop over matrix sizes
    print(k)                  
    n = 2**k
    A = np.random.random((n,n))           # Set up random general matrix
    L,U,P = scipy.linalg.lu(A)            # use LU decomp to get a unit lower triangular matrix L
    x = np.random.rand(n)                 # Set up random vector
   
#  compute products and measure computation time for general matrix A and record result 
    start=time.time()                    # Get start time
    c = GenMatVec(L,x)         # Compute the product
    elapsed = time.time() - start        # Compute and store wall time  
    wtimes_Gen.append([n,elapsed])
 
#  compute products and measure computation time for unit lower triangular matrix L and record result   
    start=time.time()                    # Get start time
    c = LowTriangMatVec(L,x)         # Compute the product
    elapsed = time.time() - start        # Compute and store wall time
    wtimes_Low.append([n,elapsed])

#  compute products and measure computation time using built-in Python function and record result
    start=time.time()                    # Get start time
    c = L @ x
    elapsed = time.time() - start        # Compute and store wall time  
    wtimes_BuiltIn.append([n,elapsed])

    #  end k for loop


#  print out computation times and plot results  

wtimes_Low = np.asarray(wtimes_Low)
wtimes_Gen = np.asarray(wtimes_Gen)
wtimes_BuiltIn = np.asarray(wtimes_BuiltIn)

#print(wtimes_Low)
#print(wtimes_Gen)
#print(wtimes_BuiltIn)

# last plot (red) is the expected O(n**2), i.e. on the loglog plot this has slope = 2
plt.loglog(wtimes_Low[:,0],wtimes_Low[:,1],'-k*', wtimes_Gen[:,0],wtimes_Gen[:,1],'-b*', wtimes_Low[:,0],1E-5*wtimes_Low[:,0]*wtimes_Low[:,0],'r-')
plt.xlabel('matrix size')
plt.ylabel('wall time of product')
plt.title('Computation time for lower triangular matrix-vector product')
plt.legend(['time for lower triangular','time for general matrix','reference slope for $O(n^2)$'])
plt.show()

# end of solution code

####  following code is for checking if mat-vec product functions are working  ####

# n = 10
# A = np.random.rand(n,n)           # Set up random matrix and right hand side
# x = np.random.rand(n,1)
 
# P,L,U = scipy.linalg.lu(A)

# print(np.linalg.norm((np.matmul(A,x) - GenMatVec(A,x)), 2)) # <= 1e-6

# print(np.linalg.norm((np.matmul(L,x) - LowTriangMatVec(L,x)), 2)) # <= 1e-6

    
    
