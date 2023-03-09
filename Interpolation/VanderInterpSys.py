
#  do polynomial interpolation problem
#   using monomial (standard) basis for P_N (vector space of polynomials of degree <= N)
#    i.e. using Vandermonde matrix

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from VanderMatrixBuild import VanderMatrix
from VanderMatrixBuild import MonoPolyEval

#  use a function f(x) to generate data points
stpt = 0
endpt = 10
NumIterPts = 10

x = np.linspace(stpt,endpt,num=NumIterPts, endpoint = True)
y = np.cos(-x**2/9.0)


#  build interpolation linear system and solve for the coefficients of the interpolant
V = VanderMatrix(x)
a_coeff = scipy.linalg.solve(V,y)

#  evaluate interpolant

xx = np.linspace(stpt,endpt, num = 100, endpoint = True)
yy = MonoPolyEval(a_coeff,xx)

#  for plotting the actual function
yy2 = np.cos(-xx**2/9.0)

plt.plot(x,y,'ro',xx,yy,'-b',xx,yy2,'m--')
plt.legend(['data','interpolant','f(x)'])
plt.show()
