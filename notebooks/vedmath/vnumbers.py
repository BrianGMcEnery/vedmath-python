from sympy import Basic, S, Expr, latex
from .vdigits import *

class VNumber(Basic):
    '''
    Root class for all numbers in vedmath.
    '''
    pass


class VInteger(VNumber):
    __slots__ = ('d',)

    def __new__(cls, i):
        obj = Expr.__new__(cls)
        obj.d = list(map(to_vdigit, get_digits(i)))
        return obj

    def _latex(self, printer):
        return latex(self.d)

    def vinculum(self):
        '''
        Transforms the digits so the number is written in vinculum form.
        '''
