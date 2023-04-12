
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
from NewtonPolyBuildA4 import NewtonPolyBuild
from NewtonPolyEvalA4 import NewtonPolyEval


#endpoint = np.pi/2.0
endpt = 4.0
NumIterpPts= 6

#x = np.array([0,np.pi/6,np.pi/4,np.pi/3,np.pi/2])
#y = np.array([0,1.0/2.0,1.0/np.sqrt(2),np.sqrt(3)/2,1.0])

x = np.linspace(0,endpt,NumIterpPts)
xx = np.linspace(0, endpt, num=100, endpoint=True)

#y = np.sin(x)
#y = np.cos(-x**2/9.0)
#yy2 = np.sin(xx)
yy2 = np.cos(-xx**2/9.0)

y = np.array([1.00,  0.90, -0.21,  -0.65,  0.68,   0.11])


V = NewtonPolyBuild(x)
a_coeff = scipy.linalg.solve(V,y)


yy = NewtonPolyEval(a_coeff,x,xx)


plt.plot(x, y, 'o',xx,yy, '-b') #, xx, yy2, '--')

#plt.legend(['data', 'polynomial interpolant','f(x)'], loc='best')
plt.title('polynomial interpolation using Newton basis (question 3)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()