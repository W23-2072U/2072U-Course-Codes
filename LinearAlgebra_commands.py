#  some examples of using Python for Linear Algebra 

import numpy as np
import scipy.linalg


A = np.array([[-7,-5,3],[-1,-8,2]])   # matrices are defined as numpy arrays


print('The matrix A=')
print(A) 
print('\n')

a13 = A[0,2]        # for accessing the components of A
#or 
a13 = A[0][2]

print(f'The component a_1,3 of A = {a13}\n' )


# find the transpose of A
B = A.T
#  or
B = np.transpose(A)


print('The transpose of A is =')
print (B)
print('\n')


#  sum of matrices  (dimension must be the same)
C = np.add(A,2*A)
# or
C = A + 2*A

print('The sum of A and 2A is =')
print (C)
print('\n')

#  multipy two matrices  (dimensions must be such that the pperation is defined)
C = np.matmul(A,B)
# or
C = np.dot(A,B)  # this is not preferred 
#or
C = A @ B

print('Are dimensions for product right?')
print(np.shape(A)[1]==np.shape(B)[0])
print('\n')


print('The product of A and B =')
print (C)
print('\n')


A = np.array([[-7,-5,3],[-1,-8,2],[4,-1,0]])  

#  find the inverse of A (A needs to be square)
Ainv = scipy.linalg.inv(A)   

#  find the determinant of A (A needs to be square)
d =  scipy.linalg.det(A)

print('New A =')
print(A)
print('\nThe inverse of A = ' )
print(Ainv)
print('\nThe product of A and its inverse is the identity')
print(A@Ainv)
print('\n')


print(f'The det of A = {d}')
print('\n')

#  the identity matrix
Id=np.identity(4)

#  the zero matrix
Zmat=np.zeros((3,3))

print('the 4x4 identity matrix')
print(Id)
print(' and the 3x3 zero matrix')
print(Zmat)
print('\n')


#  the first unit vector (as a column vector)
e1 = Id[:,[0]]

print('The first unit fector is')
print(e1)
print('\n')

#  solve A x = b

A = np.array([[-7,-5],[-1,-8]])
b = np.array([[1],[3]])

xx = scipy.linalg.solve(A,b)

print('Solving A x = b...')
print('x=')
print(xx)
print('\n')



