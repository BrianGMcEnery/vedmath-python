from sympy import *

class Quadratic:
    '''Class to experiment with quadratics.'''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        a, b, c = self.get_coeffs()
        return f'Quadratic({a}, {b}, {c})'

    def __repr__(self) -> str:
        a, b, c = self.get_coeffs()
        return f'Quadratic({a}, {b}, {c})'

    def get_coeffs(self):
        return self.a, self.b, self.c

    def roots(self):
        a, b, c = self.get_coeffs()
        return ((- b + sqrt(b**2 - 4 * a * c))/(2 * a), 
                (- b - sqrt(b**2 - 4 * a * c))/(2 * a))

    def evaluate(self, x):
        a, b, c = self.get_coeffs()
        return a * x ** 2 + b * x + c


class Cubic:
    '''Class to experiment with cubics.'''
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        a, b, c, d= self.get_coeffs()
        return f'Cubic({a}, {b}, {c}, {d})'

    def __repr__(self) -> str:
        a, b, c, d= self.get_coeffs()
        return f'Cubic({a}, {b}, {c}, {d})'

    def get_coeffs(self):
        return self.a, self.b, self.c, self.d

    def evaluate(self, x):
        a, b, c, d = self.get_coeffs()
        return a * x ** 3 + b * x ** 2 + c * x + d

    def depressed(self):
        a, b, c, d = self.get_coeffs()
        p = (3 * a * c - b ** 2) / (3 * a ** 2)
        q = (2 * b ** 3 - 9 * a * b * c + 27 * (a ** 2) * d)/ (27 * a ** 3)
        return Cubic(1, 0, p, q)

    def roots(self):
        '''Based on the general cubic formula,
        https://en.wikipedia.org/wiki/Cubic_equation#General_cubic_formula
        '''
        a, b, c, d = self.get_coeffs()
        delta0 = b**2 - 3*a*c
        delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d
        big_c = ((delta1 + sqrt(delta1**2 - 4*delta0**3)) / 2) ** (1/3)
        xi = (-1 + sqrt(-3))/2
        roots = [-1/(3*a)*(b + xi**k*big_c + delta0/(xi**k*big_c))
        for k in [0, 1, 2]]

        return tuple(roots)

