#  examples of piece-wise polynomial interpolation

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import UnivariateSpline

# data
x = np.linspace(0,10,10)
y = np.cos(-x**2/9.0)

#  points for plotting
xx = np.linspace(0,10,100)
# for plotting the original function
#yy = np.cos(-xx**2/9.0)


# piecewise linear interpolation
f_lin = interp1d(x,y)
#f_cub = interp1d(x,y,kind='cubic')   #  can change 'kind' to do cubic spline

print(f_lin(1.3))    #  can evaluate f_lin at values between x_0 and x_n

# cubic spline interpolation
f_cub = CubicSpline(x,y)

# compute first derivative of cubic spline
f_cub_d = f_cub.derivative()

# shape-preserving cubic interpolation
f_pchip = PchipInterpolator(x,y)

# compute first derivative of the interpolant
#f_cub_d = f_pchip.derivative()

# Also cubic interpolation (using a more general function)
f_uni = UnivariateSpline(x,y,k=3,s=0)

# compute first derivative of the cubic spline
#fd1 = f_uni.derivative()


plt.plot(x,y, 'o',xx,f_lin(xx),'-b')
plt.legend(['data','f'])
plt.show()