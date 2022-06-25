from vector import Vec
import numpy as np

# Calculated the gradient of a line at x
def dydx_x(func, x, dx = 1e-10):
    return (func(x+dx) - func(x)) / dx


def dfdx_xy(func, pos, delta = 1e-10):
    return (func(pos + np.array([delta, 0])) - func(pos)) / delta
    
def dfdy_xy(func, pos, delta = 1e-10):
    return (func(pos + np.array([0, delta])) - func(pos)) / delta  


def norm_of_surface(func, pos, delta = 1e-10):
    delta_unit_x = np.array([delta, 0])
    delta_unit_y = np.array([0, delta])
    pos = np.array(pos)
    
    delta_inv = 1 / delta
    
    f_pos = func(pos)
    
    dfdx = (func(pos + delta_unit_x) - f_pos) * delta_inv
    dfdy = (func(pos + delta_unit_y) - f_pos) * delta_inv
    
    return Vec([-dfdx, -dfdy, 1])