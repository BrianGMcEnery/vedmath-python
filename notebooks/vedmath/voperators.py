from .vnumbers import VInteger

class VOp:
    '''
    Root class to handle operations in vedicmath.
    '''
    pass

class VAdd(VOp):
    '''
    Class to handle addition in vedicmath.
    '''
    pass

class VSub(VOp):
    '''
    Class to handle subtraction in vedicmath.
    '''
    pass

class VMul(VOp):
    '''
    Class to handle multiplication in vedicmath.
    '''
    @classmethod
    def vert_cross(cls, a:VInteger, b:VInteger):
        '''
        Calculate multiplication using vertical and crosswise pattern,
        the default method for VInteger types.
        '''
        return a * b

    @classmethod
    def under_base(cls, a:VInteger, b:VInteger):
        '''
        Calculate product of a and b assuming that both are under the same 
        base, and not to far.
        '''
        ca = VProp.complement(a)
        cb = VProp.complement(b)
        lhs = a - cb
        lhs = lhs.padr_zero(len(a))
        rhs = ca * cb
        return lhs + rhs

class VDiv(VOp):
    '''
    Class to handle division in vedicmath.
    '''
    pass

class VProp:
    '''
    Class to handle a variety of properties.
    '''
    @classmethod
    def to_vinculum(cls, a:VInteger):
        '''
        Compute the vinculum form of an integer.
        '''
        return a.to_vinculum()

    @classmethod
    def from_vinculum(cls, a:VInteger):
        '''
        Compute the normal form of an integer.
        '''
        return a.from_vinculum()

    @classmethod
    def complement(cls, a:VInteger):
        '''
        Compute the complement of an integer from the next highest whole.
        '''

        if a.is_whole() or a == VInteger(0):
            return VInteger(0)

        ac = a
        is_negative = False

        if a < VInteger(0):
            ac = -a
            is_negative = True

        whole = [1]
        for _ in range(len(ac)):
            whole.append(0)
            
        com = (VInteger(whole) - ac)

        if is_negative:
            return -com
        else:
            return com