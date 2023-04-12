
import numpy as np

def NonLinEqns(x):                                       #  defines the function 
    x1 = x[0]
    x2 = x[1]
    f1=x1*x2**2 + x1**2*x2 + x1**3 - 1.0
    f2=x1**3*x2**2 - 2.0*x1**5*x2-x1**2 + 1.0
    fval = np.array([f1,f2])
    return fval



