
def to_digits(n):
    '''
    Returns a list of digits of an integer.
    '''
    digits = []
    def digits_inner(i):
        digits.append(i%10)
        if i == 0:
            return digits
        digits_inner(i//10)
    digits_inner(n)
    digits.reverse()
    return digits[1:]


def digit_from_vdigit(vd):
    '''
    Return a digit from a vdigit
    '''
    if (type(vd) == VDigit):
        return vd.get_val()
    else:
        raise ValueError(f"{vd} is of wrong type.")

def digit_to_vdigit(d):
    '''
    Returns a vdigit of d.
    '''
    return VDigit(d)


class VDigit:
    """
    Root class for all digits in vedmath.
    """
    _val = None

    def __init__(self, d):
        if d in range(-9, 10):
            self._val = d
        else:
            raise ValueError(f'{d} is not a digit.')

    def __str__(self):
        return f"{self.get_val()}"

    def __repr__(self):
        return f"{self.get_val()}"
    
    def get_val(self):
        return self._val
