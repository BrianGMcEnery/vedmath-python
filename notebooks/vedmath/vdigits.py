from sympy import Basic, S
from sympy.core.singleton import Singleton

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
    
    if vd == S.VPosZero:
        return 0
    elif vd == S.VNegZero:
        return 0
    elif vd == S.VPosOne:
        return 1
    elif vd == S.VNegOne:
        return -1
    elif vd == S.VPosTwo:
        return 2
    elif vd == S.VNegTwo:
        return -2
    elif vd == S.VPosThree:
        return 3
    elif vd == S.VNegThree:
        return -3
    elif vd == S.VPosFour:
        return 4
    elif vd == S.VNegFour:
        return -4
    elif vd == S.VPosFive:
        return 5
    elif vd == S.VNegFive:
        return -5
    elif vd == S.VPosSix:
        return 6
    elif vd == S.VNegSix:
        return -6
    elif vd == S.VPosSeven:
        return 7
    elif vd == S.VNegSeven:
        return -7
    elif vd == S.VPosEight:
        return 8
    elif vd == S.VNegEight:
        return -8
    elif vd == S.VPosNine:
        return 9
    elif vd == S.VNegNine:
        return -9
    else:
        raise ValueError(f"{vd} is of wrong type.")

def digit_to_vdigit(d):
    '''
    Returns a singleton vdigit of d.
    '''
    if d == 0:
        return S.VPosZero
    elif d == 1:
        return S.VPosOne
    elif d == -1:
        return S.VNegOne
    elif d == 2:
        return S.VPosTwo
    elif d == -2:
        return S.VNegTwo
    elif d == 3:
        return S.VPosThree
    elif d == -3:
        return S.VNegThree
    elif d == 4:
        return S.VPosFour
    elif d == -4:
        return S.VNegFour
    elif d == 5:
        return S.VPosFive
    elif d == -5:
        return S.VNegFive
    elif d == 6:
        return S.VPosSix
    elif d == -6:
        return S.VNegSix
    elif d == 7:
        return S.VPosSeven
    elif d == -7:
        return S.VNegSeven
    elif d == 8:
        return S.VPosEight
    elif d == -8:
        return S.VNegEight
    elif d == 9:
        return S.VPosNine
    elif d == -9:
        return S.VNegNine
    else:
        raise ValueError(f"{d} is not a single digit.")


class VDigit(Basic):
    """
    Root class for all digits in vedmath.
    """
    pass

class VPosZero(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 0

    def _latex(self, printer):
        return r"0"

class VNegZero(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 0

    def _latex(self, printer):
        return r"\bar{0}"

class VPosOne(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 1
    
    def _latex(self, printer):
        return r"1"


class VPosTwo(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 2
    
    def _latex(self, printer):
        return r"2"


class VPosThree(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 3

    def _latex(self, printer):
        return r"3"

class VPosFour(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 4

    def _latex(self, printer):
        return r"4"

class VPosFive(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 5

    def _latex(self, printer):
        return r"5"

class VPosSix(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 6

    def _latex(self, printer):
        return r"6"

class VPosSeven(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 7

    def _latex(self, printer):
        return r"7"

class VPosEight(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 8

    def _latex(self, printer):
        return r"8"

class VPosNine(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = 9

    def _latex(self, printer):
        return r"9"

class VNegOne(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -1

    def _latex(self, printer):
        return r"\bar{1}"


class VNegTwo(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -2
    
    def _latex(self, printer):
        return r"\bar{2}"


class VNegThree(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -3

    def _latex(self, printer):
        return r"\bar{3}"

class VNegFour(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -4

    def _latex(self, printer):
        return r"\bar{4}"

class VNegFive(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -5

    def _latex(self, printer):
        return r"\bar{5}"

class VNegSix(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -6

    def _latex(self, printer):
        return r"\bar{6}"

class VNegSeven(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -7

    def _latex(self, printer):
        return r"\bar{7}"

class VNegEight(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -8

    def _latex(self, printer):
        return r"\bar{8}"

class VNegNine(VDigit, metaclass=Singleton):
    __slots__ = ()

    _val = -9

    def _latex(self, printer):
        return r"\bar{9}"

