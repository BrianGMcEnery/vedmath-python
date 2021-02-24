from sympy import Basic, S, Expr, latex
from .vdigits import *

def _to_vinculum(ds):
    '''
    Returns the digits ds in vinculum form.
    '''
    def all_from_9(d):
        return 9 - d

    def last_from_10(d):
        return 10 - d
    
    def one_more_than(d):
        return d + 1

    dt = list(map(lambda e: e > 5, ds))
    if max(ds) <= 5:
        return ds
    elif len(ds) == 1:
        return [one_more_than(0)] + [-last_from_10(ds[-1])]
    elif len(ds) == 2 and ds[0] <= 5:
        return [one_more_than(ds[0])] + [-last_from_10(ds[-1])]
    elif len(ds) == 2 and ds[1] <= 5:
        return [one_more_than(0)] + [-last_from_10(ds[0])] + [ds[-1]]
    elif len(ds) == 2:
        return [one_more_than(0)] + [-all_from_9(ds[0])] + [-last_from_10(ds[-1])]
    

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
