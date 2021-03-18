class VMonomial:
    '''
    VMonomial to represent a monomial in vedmath.
    '''
    def __init__(self, coeff):
        self.coeff = coeff
    
    def __str__(self):
        return f"VMonomial({self.coeff})"
    
    def __repr__(self):
        return f"VMonomial({self.coeff})"

    def __len__(self):
        return len(self.coeff)
    
    def __getitem__(self, key):
        return self.coeff[key]

    def __setitem__(self, key, value):
        self.coeff[key] = value

