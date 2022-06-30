EPSILON = 1e-10

def approx_equal(a, b, epsilon=EPSILON):
    '''Return true if a and b are approximately equal.'''
    return(abs(a - b) <= epsilon)

