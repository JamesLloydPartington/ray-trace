import numpy as np
from grad import dfdx_xy, dfdy_xy

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
    


def is_in_xy_interval(pos, intervals):
    
    for i, interval in enumerate(intervals):
        if not is_in_interval(pos[i], interval):
            return False
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



# Finds possible intercepts in an interval for a function
def estimate_all_intercepts(ray: Ray, # The light ray
                            func, # The function of the surface
                            interval, # The rectangle defining where x and y can exist
                            n_tests = 100, # Number of points to test inside interval
                            n_iter = 100, # Number of iterations to converge to a solution
                            error = 1e-10 # The acceptable error for a correct solution
                           ):
    
    x_interval = np.sort(interval[0])
    y_interval = np.sort(interval[1])
    
    
    x0_interval_intercept_dist = ray.where(x = x_interval[0])
    x1_interval_intercept_dist = ray.where(x = x_interval[1])
    
    y0_interval_intercept_dist = ray.where(y = y_interval[0])
    y1_interval_intercept_dist = ray.where(y = y_interval[1])
    
    dist_array = np.array([x0_interval_intercept_dist,
                           x1_interval_intercept_dist,
                           y0_interval_intercept_dist,
                           y1_interval_intercept_dist])
    
    # Remove Nones from array
    dist_array[dist_array != np.array(None)]
    
    dist_array_sorted = np.sort(dist_array)
    
    if len(dist_array_sorted) == 0:
        return None
    
    # Check if Ray's starting position is inside the boundary
    
    is_inside = is_in_xy_interval(ray.start_pos, [x_interval, y_interval])
    
    
    dist_interval = np.array([])
    
    if is_inside:
        # First distance in dist_array_sorted must exit boundary
        dist_interval = np.array([0, dist_array_sorted[0]])
        
    else:
        if len(dist_array_sorted) < 2:
            # Ray must enter and exit object, so must have atleast 2 elements
            return None
        
        
        for i, val in enumerate(dist_array_sorted):
            if i == 0:
                continue
            
            ave_dist = (dist_array_sorted[i] + dist_array_sorted[i-1]) / 2
            
            if is_in_xy_interval(ray.pos_from_distance(ave_dist), [x_interval, y_interval]):
                dist_interval = np.array([dist_array_sorted[i], dist_array_sorted[i-1]])
                break
                
            if i == len(dist_array_sorted) - 1:
                return None
            
            
    
    # Can tell which distances are actually inside the object
    # dist_array_sorted defines where the ray enters/exits the boundary
    
    

    # Now x_interval and y_interval have their spread reduced (if needed)
    
    test_length = ((x_interval[1] - x_interval[0]) ** 2 + (y_interval[1] - y_interval[0]) ** 2) ** 0.5
    
    test_length_
    
    
    
    
    
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

def nearest_point(current_pos, possible_pos, error = 1e-10, exclude_current_pos = True):
    if len(possible_pos) == 0:
        return None
    else:
        # Subtract all current position from all possible positions
        # Square all values
        # Sum x^2 + y^2 (axis = 1)
        dist_squ = np.sum(np.square(np.subtract(np.array(possible_pos), np.array(current_pos))), axis=1)
        
        # Find min sum arguments (just 2)
        # Get 2 because if nearest possible position = current position,
        # then we may need to use the 2nd nearest point
        nearest_args = np.argpartition(dist_squ, 2)
        
        if exclude_current_pos and (dist_squ[nearest_args[0]]) ** 0.5 <= 2 * error:
            # Nearest point is current position
            
            if len(possible_pos) == 1:
                # There is no alternative nearest point, therefor there is none
                return None
            else:
                return possible_pos[nearest_args[1]]
        else:
            return possible_pos[nearest_args[0]]


    
    
    