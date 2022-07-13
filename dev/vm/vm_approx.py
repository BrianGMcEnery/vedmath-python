from math import isclose
EPSILON = 1e-10

def approx_equal(a, b, epsilon=EPSILON):
    '''Return true if a and b are approximately equal.'''
    return isclose(a, b, abs_tol=epsilon)