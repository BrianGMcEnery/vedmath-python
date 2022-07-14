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