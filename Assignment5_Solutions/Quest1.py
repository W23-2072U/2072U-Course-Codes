import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline


# define some parameters
startpoint = -3          #  left endpoint of interval 
endpoint = 3           #  right endpoint of interval
NumIterpPts = 13        #  = N+1 = number of interpolation points (nodes)


#   define function f(x)
def f(xs):
    return np.arctan(3*xs-2)


#  construct data points  
x = np.linspace(startpoint,endpoint,NumIterpPts)    # x coords of data points: equally spaced interpolation points
y = f(x)                                            # y coords of data points

#  calculate data for plotting f(x)
xx = np.linspace(startpoint, endpoint, 100)     #  x points where I want to plot 
y_f = f(xx)                                     #  values of original function for plotting comparison



############  polynomial interpolat  #########################

#  construct the polynomial interpolant P_12(x)
Q_N = BarycentricInterpolator(x, y)             # Q_N is Python function for interpolating polynomial 

# calculate data for plotting polynomial interpolant P_12(x)
y_poly = Q_N(xx)                                #  function values of interpoloting polynomial at x values in xx (for plotting)                 



############  piecewise linear interpolat  #########################

# construct the piecewise linear interpolant P_lin(x)
P_lin = interp1d(x, y)             # P_lin is Python function for piecewise linear interpolant 

# calculate data for plotting polynomial interpolant P_lin(x)
y_lin = P_lin(xx)                  #  function values of piecewise linear interpolant at x values in xx (for plotting)                 



############  cubic spline interpolat  #########################

# construct the cubic spline interpolant P_cub(x)
P_cub = CubicSpline(x, y)             # P_cub is Python function for cubic spline interpolant 

# calculate data for plotting polynomial interpolant P_cub(x)
y_cub = P_cub(xx)                                    #  function values of cubic spline at x values in xx (for plotting)                 




#######  code for plotting polynomial interpolant P_12(x)  ##########
plt.figure(1)

plt.subplot(2,1,1)
plt.plot(x, y, 'o',xx,y_poly, '-b',xx, y_f, '--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Interpolation with polynomial of degree '+str(NumIterpPts-1))
plt.legend(['data','interpolating polynomial','f(x)=arctan(3x-2)'], loc='best')

plt.subplot(2,1,2)
plt.plot(xx,abs(y_poly-f(xx)))

plt.xlabel('x')
plt.ylabel('Error | f(x) - P_12 |')

plt.show()

#######  code for plotting piecewise linear P_lin(x)     #######
plt.figure(2)

plt.subplot(2,1,1)
plt.plot(x, y, 'o',xx,y_lin, '-b',xx, y_f, '--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Linear Interpolation')
plt.legend(['data','piecewise linear','f(x)=arctan(3x-2)'], loc='best')

plt.subplot(2,1,2)
plt.plot(xx,abs(y_lin-f(xx)))

plt.xlabel('x')
plt.ylabel('Error | f(x) - P_lin |')

plt.show()


#######  code for plotting cubic spline interpolant P_cub(x)   #######
plt.figure(2)

plt.subplot(2,1,1)
plt.plot(x, y, 'o',xx,y_cub, '-b',xx, y_f, '--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation')
plt.legend(['data','cubic spline','f(x)=arctan(3x-2)'], loc='best')

plt.subplot(2,1,2)
plt.plot(xx,abs(y_cub-f(xx)))

plt.xlabel('x')
plt.ylabel('Error | f(x) - P_cub |')

plt.show()


