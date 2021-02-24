from sympy import Basic, S
from sympy.core.singleton import Singleton

def get_digits(n):
    '''
    Returns a list of digits in an integer
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

class VDigit(Basic):
    pass

class VPosZero(VDigit, metaclass=Singleton):

    def _latex(self, printer):
        return r"0"

class VNegZero(VDigit, metaclass=Singleton):

    def _latex(self, printer):
        return r"\bar{0}"

class VPosOne(VDigit, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"1"


class VPosTwo(VDigit, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"2"


class VPosThree(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"3"

class VPosFour(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"4"

class VPosFive(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"5"

class VPosSix(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"6"

class VPosSeven(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"7"

class VPosEight(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"8"

class VPosNine(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"9"

class VNegOne(VDigit, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"\bar{1}"


class VNegTwo(VDigit, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"\bar{2}"


class VNegThree(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{3}"

class VNegFour(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{4}"

class VNegFive(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{5}"

class VNegSix(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{6}"

class VNegSeven(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{7}"

class VNegEight(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{8}"

class VNegNine(VDigit, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{9}"

