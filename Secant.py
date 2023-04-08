# Python function for Secant iterations
import numpy as np

def secant_method(function, approximation_previous, approximation_current, max_iterations, maximum_error, maximum_residual):

    iteration_history = []

    f_previous = function(approximation_previous)                                   #previous function value

    converged = False                                                               # Convergence flag
    
    for iter in range(max_iterations):

        f_current = function(approximation_current)                                         # Function value at current approximation

        Secant_step = -f_current * (approximation_current - approximation_previous) / (f_current - f_previous)                         # Update step

        iteration_history.append([iter, abs(Secant_step), abs(f_current)])          # Error, Residual

        if iteration_history[iter][1] < maximum_error and iteration_history[iter][2] < maximum_residual:               # Convergence check
            converged = True
            break

        approximation_previous = approximation_current
        approximation_current = approximation_current + Secant_step
        f_previous = f_current

    if not converged:                                                               # print warning if the iterations did not converge
        print("Secant method did not converge after %d interations." % (max_iterations))


    return approximation_current, np.array(iteration_history), converged