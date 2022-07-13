from math import sqrt

from .vm_approx import approx_equal

class Quaternion:
    '''A class to play around with quaternions. For details see
    the Wikipedia entry, https://en.wikipedia.org/wiki/Quaternion.'''

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        a, b, c, d = self.get_components()
        return f'{a} + {b}i + {c}j + {d}k'

    def __repr__(self) -> str:
        a, b, c, d = self.get_components()
        return f'Quaternion({a}, {b}, {c}, {d})'

    def __eq__(self, other):
        a1, b1, c1, d1 = self.get_components()
        a2, b2, c2, d2 = other.get_components()
        return (approx_equal(a1, a2) and approx_equal(b1, b2) and
                approx_equal(c1, c2) and approx_equal(d1, d2))

    def __neg__(self):
        a, b, c, d = self.get_components()
        return Quaternion(-a, -b, -c, -d)

    def __add__(self, other):
        a1, b1, c1, d1 = self.get_components()
        a2, b2, c2, d2 = other.get_components()
        return Quaternion(a1 + a2, b1 + b2, c1 + c2, d1 + d2)

    def __sub__(self, other):
        return self + (- other)

    def __mul__(self, other):
        a1, b1, c1, d1 = self.get_components()
        a2, b2, c2, d2 = other.get_components()
        return Quaternion(
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
        )

    def __rmul__(self, o:float):
        a, b, c, d = self.get_components()
        return Quaternion(a * o, b * o, c * o, d * o)


    def __truediv__(self, o:int):
        a, b, c, d = self.get_components()
        return Quaternion(a / o, b / o, c / o, d / o)

    def __truediv__(self, o:float):
        a, b, c, d = self.get_components()
        return Quaternion(a / o, b / o, c / o, d / o)


    def get_components(self):
        return self.a, self.b, self.c, self.d

    def scalar_part(self):
        a, _, _, _ = self.get_components()
        return Quaternion(a, 0, 0, 0)

    def scalar(self):
        a, _, _, _ = self.get_components()
        return a

    def vector_part(self):
        _, b, c, d = self.get_components()
        return Quaternion(0, b, c, d)

    def vector(self):
        _, b, c, d = self.get_components()
        return (b, c, d)

    def conjugate(self):
        a, b, c, d = self.get_components()
        return Quaternion(a, -b, -c, -d)

    def norm(self):
        a, b, c, d = self.get_components()
        return sqrt(a * a + b * b + c * c + d * d)

    def unit(self):
        return self / self.norm()

    def reciprocal(self):
        return self.conjugate()/(self.norm() * self.norm())

    def polar_decomposition(self):
        return (self.norm(), self.unit())



QUATERNION_1 = Quaternion(1, 0, 0, 0)
QUATERNION_I = Quaternion(0, 1, 0, 0)
QUATERNION_J = Quaternion(0, 0, 1, 0)
QUATERNION_K = Quaternion(0, 0, 0, 1)
