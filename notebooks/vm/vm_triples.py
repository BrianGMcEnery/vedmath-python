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
        return f'Triple{self.get_values()}'

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
