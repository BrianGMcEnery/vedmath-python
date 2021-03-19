from .vnumbers import VInteger

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

    def duplex(self):
        '''
        Returns the duplex of a VMonomial as a VInteger.
        '''
        coeff = self.coeff
        ld = len(coeff)
        ans = VInteger(0)
        for i in range(0, ld // 2):
            ans = ans + coeff[i] * coeff[-1-i]
        ans = ans * VInteger(2)
        if ld % 2:
            middle = (ld // 2)
            ans = ans + (coeff[middle] * coeff[middle])
        return ans

    def square(self):
        '''
        Returns the square of a VMonomial as a VMonomial using the duplex.
        '''
        coeff = self.coeff
        ld = len(coeff)
        ans = []

        for i in range(1, ld + 1):
            duplex = VMonomial(coeff[:i]).duplex()
            ans.append(duplex)
        
        for i in range(1, ld):
            duplex = VMonomial(coeff[i:]).duplex()
            ans.append(duplex)
            
        return ans

