from .vnumbers import VInteger

class VMonomial:
    '''
    VMonomial to represent a monomial in vedmath.
    '''
    def __init__(self, cs):
        self.cs = cs
    
    def __str__(self):
        return f"VMonomial({self.cs})"
    
    def __repr__(self):
        return f"VMonomial({self.cs})"

    def __len__(self):
        return len(self.cs)
    
    def __getitem__(self, key):
        return self.cs[key]

    def __setitem__(self, key, value):
        self.cs[key] = value

    def __eq__(self, other):
        if type(other) == VMonomial:
            return self.cs == other.cs

    def __ne__(self, other):
        if type(other) == VMonomial:
            return self.cs != other.cs

    def duplex(self):
        '''
        Returns the duplex of a VMonomial as a VInteger.
        '''
        cs = self.cs
        ld = len(cs)
        ans = VInteger(0)
        for i in range(0, ld // 2):
            ans = ans + cs[i] * cs[-1-i]
        ans = ans * VInteger(2)
        if ld % 2:
            middle = (ld // 2)
            ans = ans + (cs[middle] * cs[middle])
        return ans

    def square(self):
        '''
        Returns the square of a VMonomial as a VMonomial using the duplex.
        '''
        cs = self.cs
        ld = len(cs)
        
        ans = [VMonomial(cs[:i]).duplex() for i in range(1, ld + 1)]
        ans = ans + [VMonomial(cs[i:]).duplex() for i in range(1, ld)]
            
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

        ans = [VMonomial(vs[:i])._vc_inner_prod(VMonomial(vo[:i]))
                for i in range(1, lvs + 1)]

        ans = ans + [VMonomial(vs[i:])._vc_inner_prod(VMonomial(vo[i:]))
                for i in range(1, lvs)]

        return VMonomial(ans).unpadl_zero()

    def padl_zero(self, l0):
        '''
        Pad the monomial by l0 leading zero Vintegers on the left.
        '''
        padded = [VInteger(0) for _ in range(l0)] + self.cs
        return VMonomial(padded)

    def unpadl_zero(self):
        '''
        Take away leading zero's in the monomial.
        '''
        cs = self.cs
        idx = 0
        while cs[idx] == VInteger(0):
            idx += 1

        return VMonomial(cs[idx:])

    def padr_zero(self, l0):
        '''
        Pad the momomial by l0 trailing zero digits on the right.
        '''
        padded = self.cs + [VInteger(0) for _ in range(l0)]
        return VMonomial(padded)
