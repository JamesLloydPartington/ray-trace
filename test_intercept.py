import numpy as np
import math
from intercept import sign_change, within_error, estimate_all_intercepts, nearest_point

# estimate_all_intercepts(f, g, interval, n_tests = 100, n_iter = 100, error = 1e-10):

def test_sign_change():
    
    assert sign_change(-1, 1) == True
    
    assert sign_change(1, 1) == False
    
    assert sign_change(0, 0) == False
    
    assert sign_change(1, 0) == False
    
    assert sign_change(0, 1) == False

def test_within_error():
    
    no_tests = 2
    err = 1e-10
    a   = [1, -1]
    b   = [1,  1]
    result = [True, False]
    
    for i in range(no_tests):
        assert within_error(a[i], b[i], err) == result[i]
    
    arr1 = np.array([1, 2, 3, 4, 5, 6])
    arr2 = np.array([1 - err/2, 2 + err/2, 3, 4, 5, 6])
    
    assert within_error(arr1, arr2, err)

def sin(x):
    return math.sin(x)

def func_order3(x):
    return -(x * x * x) + (x * x) + x - 0.1

def func_is_0(x):
    return 0

def func_is_0p9(x):
    return 0.9

def func_is_2(x):
    return 2

def func_x(x):
    return x

def func_mx(x):
    return -x

def sin_x_squ(x):
    return math.sin(x * x)

def get_max_diff_of_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    else:
        return np.max( np.absolute(arr1 - arr2) )

def test_estimate_all_intercepts():
    
    # Should be no intercepts
    assert len(estimate_all_intercepts(sin, func_is_2, np.array([-10, 10]))) == 0
    
    
    # Array of n * pi from 0 to 9
    answers = np.array([ np.array([i * math.pi, 0]) for i in range(0, 10)])
    # Test in interval [-0.1, 9 * pi + 0.1], for 100 intervals with an error or 1e-10
    err = 1e-10
    estimates = estimate_all_intercepts(sin, 
                                        func_is_0, 
                                        np.array([-0.1, 9 * math.pi + 0.1]), 
                                        n_tests = 100, 
                                        n_iter = 100, 
                                        error = err)
    
    assert get_max_diff_of_arrays(answers, estimates) <= err
    
    
    
    answers2 = estimate_all_intercepts(sin, 
                                       func_order3, 
                                       np.array([-10, 10]),
                                       n_tests = 200, 
                                       n_iter = 100, 
                                       error = err)
    print(answers2)
    assert len(answers2) == 3
    
    answers3 = estimate_all_intercepts(func_x, 
                                       func_mx, 
                                       np.array([-10, 10]),
                                       n_tests = 200, 
                                       n_iter = 100, 
                                       error = err)
    print(answers3)
    assert len(answers3) == 1
    
    answers4 = estimate_all_intercepts(func_is_0p9, 
                                       sin_x_squ, 
                                       np.array([0, 10]), 
                                       n_tests = 200, 
                                       n_iter = 100, 
                                       error = err)
    print(answers4)
    assert len(answers4) == 32
    
    
    
def test_nearest_point():
    pos1 = [1, 1]
    pos_arr1 = np.array([ [0, 0], [2, 2], [3, 3] ])
    
    assert within_error([0, 0], nearest_point(pos1, pos_arr1), 1e-10)
    
    
    