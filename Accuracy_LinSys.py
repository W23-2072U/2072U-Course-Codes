
# Illustration of linear solving of ill-conditioned systems. 
#  Uses the Vandermonde matrix for a regular grid.


import numpy as np
import scipy.linalg

# Define the grid. Condition number grows with the number of grid points.
N = 20                       # Number of grid points (set N>1). 
xs=np.linspace(-1,1,N+1)       # Regular grid on [-1,1] with N points.

V = np.vander(xs)

# Set a right-hand-side.
def f(x):
    return x-x**2
R = np.reshape(f(xs),(N+1,1))

# Solve the linear equation.
y = np.linalg.solve(V,R)

# This example is derives from a polynomial interpolation problem and we know that the exact solution is
# y = [[0, 0, 0, 0, 0, ..., -1, 1, 0]] for N > 1.
y_exact = np.zeros((N+1,1));y_exact[N-1] = 1.0;y_exact[N-2] = -1;

K = np.linalg.cond(V)
print(f'The condition number of V for N = {N} is {K:.4e}.')
err = scipy.linalg.norm(y-y_exact,2)
rel_err = err/scipy.linalg.norm(y_exact,2)
res = scipy.linalg.norm(V@y-R,2)
rel_res = res/scipy.linalg.norm(R,2)
print("Verify the upper bound of the error:")
print(f'Relative error = {rel_err:.6e} < (condition number) x (relative residual) = {K*rel_res:.6e}')

