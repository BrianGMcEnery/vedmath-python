from math import sqrt, gcd

APPROX_ZERO = 1e-10

class CodeNumber:
    ''' Class to compute with the code numbers of triples. For details
    see chapter 6 of the Triples book.
    '''

    def __init__(self, c, d=1):
        '''Initialise attributes.'''
        self.c = c
        self.d = d

    def __repr__(self) -> str:
        '''Return canonical string representation.'''
        return f'CodeNumber{self.get_values()}'

    def __eq__(self, other) -> bool:
        '''Comparison of codenumbers.'''
        return self.get_values() == other.get_values()

    def __add__(self, other):
        '''Addition of codenumbers, pp69 in Triples book.'''
        sc, sd = self.get_values()
        oc, od = other.get_values()
        sum = CodeNumber(sc * oc - sd * od, sd * oc + sc * od)
        return sum.reduce()

    def __sub__(self, other):
        '''Subtraction of codenumbers, pp70 in Triples book.'''
        sc, sd = self.get_values()
        oc, od = other.get_values()
        dif = CodeNumber(sc * oc + sd * od, sd * oc - sc * od)
        return dif.reduce()

    def get_values(self):
        '''Return a tuple of the attributes c, d.'''
        return (self.c, self.d)

    def reduce(self):
        '''
        Reduce to the form where the elements have no common factors.
        '''
        c, d = self.get_values()
        if type(c) == int and type(d) == int:
            div = gcd(c, d)
            if div > 1:
                c, d = c / div, d / div
        elif abs(d) > 1:
            c, d = c / d, 1

        return CodeNumber(c, d)

    def complimentary(self):
        '''Codenumbers corresponding to the complimentary triple, pp 71 in 
        Triples book.'''
        c,d = self.get_values()
        return CodeNumber(c+d, c-d).reduce()

    def supplimentary(self):
        '''Codenumbers corresponding to the supplimentary triple, pp 72 in 
        Triples book.'''
        c,d = self.get_values()
        return CodeNumber(d, c).reduce()

# Constants as per pp 72 in the Triples book

CODENUMBER_0 = CodeNumber(1, 0)
CODENUMBER_90 = CodeNumber(1, 1)
CODENUMBER_180 = CodeNumber(0, 1)
CODENUMBER_270 = CodeNumber(1, -1)
CODENUMBER_360 = CodeNumber(1, 0)

#Constants based on numerical experiments.

CODENUMBER_30 = CodeNumber(2 + sqrt(3))
CODENUMBER_45 = CodeNumber(1 + sqrt(2))
CODENUMBER_60 = CodeNumber(sqrt(3))

class QuadCodeNumber:
    ''' Class to compute with the code numbers of quadruples. For details
    see chapter 14 of the Triples book.
    '''

    def __init__(self, c, d, e):
        '''Initialise attributes.'''
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self) -> str:
        '''Return canonical string representation.'''
        return f'QuadCodeNumber{self.get_values()}'

    def __eq__(self, other) -> bool:
        '''Comparison of codenumbers.'''
        return self.get_values() == other.get_values()

    def get_values(self):
        '''Return a tuple of the attributes c, d, e.'''
        return (self.c, self.d, self.e)

    def reduce(self):
        '''
        Reduce to the form where the elements have no common factors.
        '''
        c, d, e = self.get_values()
        if type(c) == int and type(d) == int and type(e) == int:
            div = gcd(gcd(c, d), e)
            if div > 1:
                c, d, e = c / div, d / div, e / div
                
        return QuadCodeNumber(c, d, e)

# As per pp164 of the Triples book.

QCN_POSX = QuadCodeNumber(1, 0, 1)
QCN_NEGX = QuadCodeNumber(0, 1, 0)
QCN_POSY = QuadCodeNumber(1, 1, 0)
QCN_NEGY = QuadCodeNumber(1, -1, 0)
QCN_POSZ = QuadCodeNumber(0, 1, 1)
QCN_NEGZ = QuadCodeNumber(0, -1, 1)