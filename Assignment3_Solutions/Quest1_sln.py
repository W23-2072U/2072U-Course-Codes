#  Starter code for Question 1 of Assignment 3 

import numpy as np

# Import the function you wrote for part 1(a) and the secant iteration function.
from CondNumFuncA3 import CondNumFunc
from Secant import secant_method


def f(x):
    return CondNumFunc(x)-4 

# Set parameters and initial values for secant iteration.

x0=0.
x1=5.
kMax=50
max_err=10e-8
max_res=1

# Do secant iteration.

solution_secant, record_secant, flag_secant = secant_method( f, x0, x1, kMax, max_err, max_res )

# write out the solution

print(solution_secant)

