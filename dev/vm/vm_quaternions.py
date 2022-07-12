class Quaternion:
    '''A class to play around with quaternions. For details see
    the Wikipedia entry, https://en.wikipedia.org/wiki/Quaternion.'''

    def __init__(self, a, b, c, d):
        '''Initialize the four components.'''
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
        return self.get_components() == other.get_components()

    def __neg__(self):
        a, b, c, d = self.get_components()
        return Quaternion(-a, -b, -c, -d)

    def __add__(self, other):
        a1, b1, c1, d1 = self.get_components()
        a2, b2, c2, d2 = other.get_components()
        return Quaternion(a1 + a2, b1 + b2, c1 + c2, d1 + d2)

    def __mul__(self, other):
        a1, b1, c1, d1 = self.get_components()
        a2, b2, c2, d2 = other.get_components()
        return Quaternion(
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
        )

    def get_components(self):
        return self.a, self.b, self.c, self.d



QUATERNION_1 = Quaternion(1, 0, 0, 0)
QUATERNION_I = Quaternion(0, 1, 0, 0)
QUATERNION_J = Quaternion(0, 0, 1, 0)
QUATERNION_K = Quaternion(0, 0, 0, 1)
