# polynomial interpolation

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from scipy.interpolate import BarycentricInterpolator

# data: (1,1),(2,0.3),(3,0.6),(4,0.1)  ->  n = 3

x = np.array([1.0,2.0,3.0,4.0])
y = np.array([1.0,0.3,0.6,0.1])

#  use built-in scipy function to find interpolant
Q_N = BarycentricInterpolator(x,y)   # Q_N  is a Python function for the interpolant

xx = np.linspace(1,4,num=100,endpoint=True)
yy = Q_N(xx)                        #  evaluate the interpolate at values from xx

#  use Vandermonde matrix to find interpolant
V = np.vander(x)
a_coeff = scipy.linalg.solve(V,y)    #  gives coefficients of the polynomial interpolant

# evaluate the interpolant at values from xx;
#   note the order in which a_ceoff stores coefficients when we use np.vander to get Vandermonde matrix
yy2 = a_coeff[0]*xx*xx*xx + a_coeff[1]*xx*xx + a_coeff[2]*xx + a_coeff[3]

#  the two polynomial interpolants (i.e yy and yy2) are the same (because the interpolant is unique)
plt.plot(x,y,'ro',xx,yy,'-b',xx,yy2,'-m')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
