from sympy import Basic, S
from sympy.core.singleton import Singleton

class VZero(Basic, metaclass=Singleton):
    pass

class VPosZero(Basic, metaclass=Singleton):

    def _latex(self, printer):
        return r"0"

class VNegZero(Basic, metaclass=Singleton):

    def _latex(self, printer):
        return r"\bar{0}"

class VPosOne(Basic, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"1"


class VPosTwo(Basic, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"2"


class VPosThree(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"3"

class VPosFour(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"4"

class VPosFive(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"5"

class VPosSix(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"6"

class VPosSeven(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"7"

class VPosEight(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"8"

class VPosNine(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"9"

class VNegOne(Basic, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"\bar{1}"


class VNegTwo(Basic, metaclass=Singleton):
    
    def _latex(self, printer):
        return r"\bar{2}"


class VNegThree(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{3}"

class VNegFour(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{4}"

class VNegFive(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{5}"

class VNegSix(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{6}"

class VNegSeven(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{7}"

class VNegEight(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{8}"

class VNegNine(Basic, metaclass=Singleton):
    def _latex(self, printer):
        return r"\bar{9}"

