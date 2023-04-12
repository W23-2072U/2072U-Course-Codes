
import numpy as np

def Jacobian(x):                                      #  defines the Jacobian
    x1 = x[0]
    x2 = x[1]    
    J11 = x2**2 + 2.0*x1*x2 + 3.0*x1**2 
    J12 = 2.0*x1*x2 + x1**2
    J21 = 3.0*x1**2*x2**2 - 10.0*x1**4*x2-2.0*x1
    J22 = 2.0*x1**3*x2 - 2.0*x1**5
    Jac = np.array([[J11,J12],[J21,J22]])
    return Jac


x = np.array([np.sqrt(5), 0.31])
J = Jacobian(x)

print(J)    