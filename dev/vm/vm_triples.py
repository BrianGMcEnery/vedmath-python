from math import sqrt, gcd


APPROX_ZERO = 1e-10

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
        return self.get_values() == other.get_values()

    def __add__(self, other):
        '''Addition of triples, using formula on pp8 of book on Triples.'''
        x, y, r = self.get_values()
        bx, by, br = other.get_values()
        return Triple(x * bx - y * by, y * bx + x * by, r * br)

    def __sub__(self, other):
        '''Subtraction of triples, using method on pp10 of book on Triples.'''
        x, y, r = self.get_values()
        bx, by, br = other.get_values()
        return Triple(x * bx + y * by, y * bx - x * by, r * br)

    def double(self):
        '''Double angle formula, pp9 in Triple book.'''
        x, y, r = self.get_values()
        return Triple(x * x - y * y, 2 * x * y, r * r)

    def half(self):
        '''Half angle method, pp17 in Triple Book'''
        x, y, r = self.get_values()
        hx = x + r
        hy = y
        hr = sqrt(hx * hx + hy * hy)
        return Triple(hx, hy, hr)

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
        return abs(x ** 2 + y ** 2 - r ** 2) <= APPROX_ZERO

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
        d = gcd(x, y)
        if d > 1:
            x, y, r = x / d, y / d, r / d

        return Triple(x, y, r)

TRIPLE_0 = Triple(1, 0, 1)
TRIPLE_90 = Triple(0, 1, 1)
TRIPLE_180 = Triple(-1, 0, 1)
TRIPLE_270 = Triple(0, -1, 1)
TRIPLE_360 = Triple(1, 0, 1)

TRIPLE_30 = Triple(sqrt(3), 1 ,2)
TRIPLE_45 = Triple(1, 1, sqrt(2))
TRIPLE_60 = Triple(1, sqrt(3) ,2)

class CodeNumber:
    ''' Class to compute with the code numbers of triples. For details
    see chapter 6 of the Triples book.
    '''

    def __init__(self, c, d):
        '''Initialise attributes.'''
        self.c = c
        self.d = d

    def __repr__(self) -> str:
        '''Return canonical string representation.'''
        return f'CodeNumber{self.get_values()}'

    def __eq__(self, other) -> bool:
        '''Comparison of codenumbers.'''
        return self.get_values() == other.get_values()

    def get_values(self):
        '''Return a tuple of the attributes c, d.'''
        return (self.c, self.d)

    def get_triple(self):
        '''Return a triple corresponding to the codenumbers c and d, as per 
        formula on pp67 of the Triple book.'''
        c, d = self.get_values()
        return Triple(c * c - d * d, 2 * c * d, c * c + d * d)

    def reduce(self):
        '''
        Reduce to the form where the elements have no common factors.
        '''
        c, d = self.get_values()
        if type(c) == int and type(d) == int:
            div = gcd(c, d)
            if div > 1:
                c, d = c / div, d / div

        return CodeNumber(c, d)

# Constants as per pp 72 in the Triples book

CODENUMBER_0 = CodeNumber(1, 0)
CODENUMBER_90 = CodeNumber(1, 1)
CODENUMBER_180 = CodeNumber(0, 1)
CODENUMBER_270 = CodeNumber(1, -1)
CODENUMBER_360 = CodeNumber(1, 0)


def code_number_of(t:Triple) -> CodeNumber:
    '''Return the codenumber corresponding to a triple, pp 68 in 
    Triples book.'''
    x, y, r = t.get_values()
    return CodeNumber(x + r, y).reduce()

def triple_of(cn:CodeNumber) -> Triple:
    '''Return the triple corresponding to a codenumber. Function defined 
    for completion.'''
    return cn.get_triple()
