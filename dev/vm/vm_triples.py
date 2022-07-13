from math import sqrt, gcd

from .vm_approx import approx_equal

class Triple:
    '''
    Class for computing with Pythagorean Triples. For reference see the 
    book Triples by Kenneth Williams.
    '''
    def __init__(self, x, y, r):
        '''
        Initialise the attributes of a triple, where x is the base, 
        y is the height and r is the hypotenuse.
        '''
        self.x = x
        self.y = y
        self.r = r

    def __repr__(self) -> str:
        ''' Return canonical string representation.'''
        return f'Triple{self.get_values()}'

    def __eq__(self, other) -> bool:
        ''' Comparison based on the values.'''
        x1, y1, z1 = self.get_values()
        x2, y2, z2 = other.get_values()
        return (approx_equal(x1, x2) and approx_equal(y1, y2) and 
                approx_equal(z1, z2))

    def __add__(self, other):
        '''Addition of triples, using formula on pp8 of book on Triples.'''
        x, y, r = self.get_values()
        bx, by, br = other.get_values()
        return Triple(x * bx - y * by, y * bx + x * by, r * br).reduce()

    def __sub__(self, other):
        '''Subtraction of triples, using method on pp10 of book on Triples.'''
        x, y, r = self.get_values()
        bx, by, br = other.get_values()
        return Triple(x * bx + y * by, y * bx - x * by, r * br).reduce()

    def double(self):
        '''Double angle formula, pp9 in Triple book.'''
        x, y, r = self.get_values()
        return Triple(x * x - y * y, 2 * x * y, r * r).reduce()

    def half(self):
        '''Half angle method, pp17 in Triple Book'''
        x, y, r = self.get_values()
        hx = x + r
        hy = y
        hr = sqrt(hx * hx + hy * hy)
        return Triple(hx, hy, hr).reduce()

    def get_values(self):
        '''
        Return a tuple of the attributes x, y, r.
        '''
        return (self.x, self.y, self.r)

    def is_valid(self):
        '''
        Tests for the validity of the triple.
        '''
        (x, y, r) = self.get_values()
        return approx_equal(x ** 2 + y ** 2, r ** 2)

    def base(self):
        return self.x

    def height(self):
        return self.y

    def hypotenuse(self):
        return self.r

    def cos(self):
        '''
        Cosine of the angle of the triple.
        '''
        return self.x / self.r

    def sin(self):
        '''
        Sine of the angle of the triple.
        '''
        return self.y / self.r

    def tan(self):
        '''
        Tan of the angle of the triple.
        '''
        return self.y / self.x

    def cosec(self):
        '''
        Cosec of the angle of the triple.
        '''
        return self.r / self.x

    def sec(self):
        '''
        Sec of the angle of the triple.
        '''
        return self.r / self.y

    def cot(self):
        '''
        Cot of the angle of the triple.
        '''
        return self.x / self.y

    def complimentary(self):
        '''
        Returns the complimentary triple.
        '''
        x, y, r = self.get_values()
        return Triple(y, x, r)

    def is_similar(self, other):
        ''' Test for similarity between triples.'''
        s = self.get_values()
        o = other.get_values()
        ratios = [e[0] / e[1] for e in zip(s, o)]
        return all([r == ratios[0] for r in ratios])

    def divide(self, c):
        '''Divide elements by a common factor.'''
        x, y, r = self.get_values()
        return Triple(x / c, y / c, r / c)

    def multiply(self, c):
        '''Multiply elements by a common factor.'''
        x, y, r = self.get_values()
        return Triple(x * c, y * c, r * c)

    def reduce(self):
        '''
        Reduce to the form where the first elements have no common factors.
        '''
        x, y, r = self.get_values()
        if type(x) == int and type(y) == int:
            d = gcd(x, y)
            if d > 1:
                x, y, r = x / d, y / d, r / d

        return Triple(x, y, r)

    def normalise(self):
        '''
        Normalise to the form where the radius is one.
        '''
        x, y, r = self.get_values()
        return Triple(x / r, y / r, 1)


TRIPLE_0 = Triple(1, 0, 1)
TRIPLE_90 = Triple(0, 1, 1)
TRIPLE_180 = Triple(-1, 0, 1)
TRIPLE_270 = Triple(0, -1, 1)
TRIPLE_360 = Triple(1, 0, 1)

TRIPLE_30 = Triple(sqrt(3), 1 ,2)
TRIPLE_45 = Triple(1, 1, sqrt(2))
TRIPLE_60 = Triple(1, sqrt(3) ,2)

class Quadruple:
    '''
    Class for computing with quadruples. For reference see the 
    book Triples by Kenneth Williams.
    '''
    def __init__(self, x, y, z, r):
        '''
        Initialise the attributes of a quadruple.
        '''
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __repr__(self) -> str:
        ''' Return canonical string representation.'''
        return f'Quadruple{self.get_values()}'

    def __eq__(self, other) -> bool:
        ''' Comparison based on the values.'''
        return self.get_values() == other.get_values()

    def get_values(self):
        '''
        Return a tuple of the attributes x, y, z, r.
        '''
        return (self.x, self.y, self.z, self.r)

    def is_valid(self):
        '''
        Tests for the validity of the quadruple.
        '''
        (x, y, z, r) = self.get_values()
        return approx_equal(x ** 2 + y ** 2 + z ** 2, r ** 2)

    def get_composite_triples(self):
        '''Return a list of the four composite triples, as per diagram
        on pp 162 of the Triples book.'''
        x, y, z, r = self.get_values()
        return [
            Triple(x, sqrt(r * r - x * x) ,r), 
            Triple(y, z, sqrt(y * y + z * z)),
            Triple(x, y, sqrt(x * x + y * y)),
            Triple(sqrt(r * r - z * z), z, r)
            ]

    def reduce(self):
        '''
        Reduce to the form where the first elements have no common factors.
        '''
        x, y, z, r = self.get_values()
        if type(x) == int and type(y) == int and type(z) == int:
            d = gcd(gcd(x, y), z)
            if d > 1:
                x, y, z, r = x / d, y / d, z / d, r / d

        return Quadruple(x, y, z, r)

# as per pp164 of the Triples book
QUAD_POSX = Quadruple(1, 0, 0, 1)
QUAD_NEGX = Quadruple(-1, 0, 0, 1)
QUAD_POSY = Quadruple(0, 1, 0, 1)
QUAD_NEGY = Quadruple(0, -1, 0, 1)
QUAD_POSZ = Quadruple(0, 0, 1, 1)
QUAD_NEGZ = Quadruple(0, 0, -1, 1)

class Quintuple:
    '''
    Class for computing with quintuples. For reference see the 
    book Triples by Kenneth Williams. Required for quadruple subtraction pp164.
    '''
    def __init__(self, w, x, y, z, r):
        '''
        Initialise the attributes of a quintuple.
        '''
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __repr__(self) -> str:
        ''' Return canonical string representation.'''
        return f'Quintuple{self.get_values()}'

    def __eq__(self, other) -> bool:
        ''' Comparison based on the values.'''
        return self.get_values() == other.get_values()

    def get_values(self):
        '''
        Return a tuple of the attributes w, x, y, z, r.
        '''
        return (self.w, self.x, self.y, self.z, self.r)

    def is_valid(self):
        '''
        Tests for the validity of the quadruple.
        '''
        (w, x, y, z, r) = self.get_values()
        return approx_equal(w ** 2 + x ** 2 + y ** 2 + z ** 2, r ** 2)

    def reduce(self):
        '''
        Reduce to the form where the first elements have no common factors.
        '''
        w, x, y, z, r = self.get_values()
        if type(x) == int and type(y) == int and type(z) == int:
            d = gcd(gcd(gcd(w, x), y), z)
            if d > 1:
                w, x, y, z, r = w / d, x / d, y / d, z / d, r / d

        return Quintuple(w, x, y, z, r)