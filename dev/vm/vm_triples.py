class Triple:
    '''
    Class for computing with Pythagorean Triples. For reference see the 
    book Triples by Kenneth Williams.
    '''
    def __init__(self, a, b, c):
        '''
        Initialise the attributes of a triple, where a is the base, 
        b is the height and c is the hypotenuse.
        '''
        self.a = a
        self.b = b
        self.c = c

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

    def get_values(self):
        '''
        Return a tuple of the values a, b, c
        '''
        return (self.a, self.b, self.c)

    def is_valid(self):
        '''
        Tests for the validity of the triple.
        '''
        (a, b, c) = (self.a, self.b, self.c)
        return a ** 2 + b ** 2 == c ** 2

    def base(self):
        return self.a

    def height(self):
        return self.b

    def hypotenuse(self):
        return self.c

    def cos(self):
        '''
        Cosine of the angle of the triple.
        '''
        return self.a / self.c

    def sin(self):
        '''
        Sine of the angle of the triple.
        '''
        return self.b / self.c

    def tan(self):
        '''
        Tan of the angle of the triple.
        '''
        return self.b / self.a

    def complimentary(self):
        '''
        Returns the complimentary triple.
        '''
        return Triple(self.b, self.a, self.c)

    def similar(self, other):
        ''' Test for similarity between triples.'''
        s = self.get_values()
        o = other.get_values()
        ratios = [e[0] / e[1] for e in zip(s, o)]
        return all([r == ratios[0] for r in ratios])

TRIPLE_0 = Triple(1, 0, 1)
TRIPLE_90 = Triple(0, 1, 1)
TRIPLE_180 = Triple(-1, 0, 1)
TRIPLE_270 = Triple(0, -1, 1)
TRIPLE_360 = Triple(1, 0, 1)