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
            
        return VMonomial(ans)

    def _vc_inner_prod(self, other):
        '''
        Vertical and Crosswise inner product. Assume both VMonomials of same 
        length.
        '''
        ld = len(self)
        ans = VInteger(0)
        for i in range(0, ld):
            ans = ans + self[i] * other[ld - i - 1]

        return ans

    def vert_cross_product(self, other):
        '''
        Vertical Crosswise product. Based on duplex and squaring.
        '''

        vs = self
        vo = other
        l0 = len(vs) - len(vo)
        if l0 > 0:
            vo = vo.padl_zero(l0)
        elif l0 < 0:
            vs = vs.padl_zero(-l0)

        lvs = len(vs)

        ans = []

        for i in range(1, lvs + 1):
            inner_product = VMonomial(vs[:i])._vc_inner_prod(VMonomial(vo[:i]))
            ans.append(inner_product)

        for i in range(1, lvs):
            inner_product = VMonomial(vs[i:])._vc_inner_prod(VMonomial(vo[i:]))
            ans.append(inner_product)

        return VMonomial(ans)

    def padl_zero(self, l0):
        '''
        Pad the monomial by l0 leading zero Vintegers on the left.
        '''
        padded = [VInteger(0) for _ in range(l0)] + self.coeff
        return VMonomial(padded)

    def unpadl_zero(self):
        '''
        Take away leading zero's in the monomial.
        '''
        coeff = self.coeff
        idx = 0
        while coeff[idx] == VInteger(0):
            idx += 1

        print(idx)
        return VMonomial(coeff[idx:])
