# Calculated the gradient of a line at x
def dydx_x(func, x, dx = 1e-10):
    return (func(x+dx) - func(x)) / dx