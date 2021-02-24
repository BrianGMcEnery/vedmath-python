from sympy import Basic, S, Expr, latex
from .vdigits import *

def _to_vinculum(ds):
    '''
    Returns the digits ds in vinculum form.
    '''
    def last_10(d):
        return 10 - d
    dt = list(map(lambda e: e > 5, ds))
    if max(ds) <= 5:
        return ds
    elif len(ds) == 1:
        return [1] + [-last_10(ds[-1])]
    

class VNumber(Basic):
    '''
    Root class for all numbers in vedmath.
    '''
    pass


class VInteger(VNumber):
    __slots__ = ('d',)

    def __new__(cls, i):
        obj = Expr.__new__(cls)
        if isinstance(i, list):
            digits = i
        else:
            digits = get_digits(i)
        obj.d = list(map(digit_to_vdigit, digits))
        return obj

    def _latex(self, printer):
        return latex(self.d)

    def to_vinculum(self):
        '''
        Transforms the digits so the number is written in vinculum form.
        '''
        ds = list(map (digit_from_vdigit, self.d))
        return VInteger(_to_vinculum(ds))
