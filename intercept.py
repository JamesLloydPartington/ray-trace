import numpy as np
from grad import dydx_x

# False if signs of x and y are the same, True otherwise
# Warning, this does not detect a change in sign between (+/- value) and 0
def sign_change(x, y):
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
        return False
    return True

# Checks if two numbers or two arrays values are all within error
def within_error(thing1, thing2, error):
    diff = np.max(np.absolute(np.array(thing1) - np.array(thing2)))
    if diff <= error:
        return True
    else:
        return False


def is_in_interval(val, interval):
    if val < interval[0] or val > interval[1]:
        return False
    else:
        return True
    

# Newton–Raphson method
# Calculates func(x) = 0 for one value of x
# Returns an intercept x value or None
def calc_intercept(func, interval, n_iter = 100, error = 1e-10, force_find = False):
    
    x_guess = np.mean(interval)
    for i in range(0, n_iter):
        if is_in_interval(x_guess, interval) and (force_find == False):
            return None
        else:
            
            # Check if the intercept is within error of 0
            y = func(x_guess)
            if within_error(y, 0, error):
                if force_find:
                    if is_in_interval(x_guess, interval) == False:
                        # Converged to value outside of interval
                        print("Converged outside of interval")
                        return None
                return x_guess
            
            grad = dydx_x(func, x_guess)
            if within_error(grad, 0, error):
                print("Failed to converge, gradients too similar")
                return None
            
            # Newton–Raphson method here
            x_guess = x_guess - ( y / grad )
    
    print("Failed to converge, too many itterations")      
    return None



# Finds possible intercepts in an interval
def estimate_all_intercepts(f, g, interval, n_tests = 100, n_iter = 100, error = 1e-10):
    
    interval = np.sort(interval)
    
    def diff_func(x):
        return f(x) - g(x)
    
    # Sample n_tests points in the interval
    x_tests = (np.arange(n_tests, dtype = np.float32) / (n_tests - 1)) * (interval[1] - interval[0]) + interval[0]
    # Calculate f(x) - g(x) over the interval
    y_vals = np.fromiter((diff_func(xi) for xi in x_tests), dtype = np.float32)
    
    # Intercepts are found by finding when f(x) - g(x) changes sign
    # Holds a list of intervals where the sign changed
    test_list = []
    for i, val in enumerate(y_vals):
        if(i == 0):
            continue
        
        if sign_change(val, y_vals[i-1]):
            test_list.append([x_tests[i-1], x_tests[i]])
    
    
    intercepts_tests = []
    if len(test_list) == 0:
        # Even if test_list is empty, this could be due to sampling not being fine enough
        intercepts_tests = [calc_intercept(diff_func, interval, n_iter = n_iter, error = error, force_find = False)]
    else:
        for i in test_list:
            intercepts_tests.append(calc_intercept( diff_func, i, n_iter = n_iter, error = error, force_find = True) )
    
    intercepts = []
    for x in intercepts_tests:
        if x is not None:
            intercepts.append([x, f(x)])
        else:
            print("Could not find intercept despite a change of sign")
    return np.array(intercepts)

def nearest_point(current_pos, possible_pos):
    if len(possible_pos) == 0:
        return None
    else:
        # Subtract all current position from all possible positions
        # Square all values
        # Sum x^2 + y^2 (axis = 1)
        # Find min sum argument
        nearest_arg = np.argmin(np.sum(np.square(np.subtract(np.array(possible_pos), np.array(current_pos))), axis=1))
        
        return possible_pos[nearest_arg]


    
    
    