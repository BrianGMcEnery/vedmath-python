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
        base.
        '''
        ca = VProp.deficit(a)
        cb = VProp.deficit(b)
        lhs = a + cb
        lhs = lhs.padr_zero(len(a))
        rhs = ca * cb
        return lhs + rhs

    @classmethod
    def over_base(cls, a:VInteger, b:VInteger):
        '''
        Calculate product of a and b assuming that both are over the same 
        base.
        '''
        ca = VProp.surplus(a)
        cb = VProp.surplus(b)
        lhs = a + cb
        lhs = lhs.padr_zero(len(a)-1)
        rhs = ca * cb
        return lhs + rhs

    @classmethod
    def near_base(cls, a:VInteger, b:VInteger, base=VInteger(100)):
        '''
        Calculate product of a and b assuming that both are near the same 
        base.
        '''
        if a.is_whole():
            return b.padr_zero(len(a)-1)
        elif b.is_whole():
            return a.padr_zero(len(b)-1)

        if a < base:
            ca = VProp.deficit(a)
        else:
            ca = VProp.surplus(a)
        if b < base:
            cb = VProp.deficit(b)
        else:
            cb = VProp.surplus(b)
        
        lhs = a + cb
        if a < base:
            lhs = lhs.padr_zero(len(a))
        else:
            lhs = lhs.padr_zero(len(a)-1)
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
    def deficit(cls, a:VInteger):
        '''
        Compute the deficit of an integer from the next highest whole.
        '''
        if a.is_whole() or a == VInteger(0):
            return VInteger(0)

        ac = a
        is_negative = False

        if a < VInteger(0):
            ac = -a
            is_negative = True

        com = (ac - VProp.next_highest_whole(ac))

        if is_negative:
            return -com
        else:
            return com

    @classmethod
    def next_highest_whole(cls, a:VInteger):
        '''
        Compute the next highest whole of an integer.
        '''
        if a.is_whole() or a == VInteger(0):
            return a

        ac = a
        is_negative = False

        if a < VInteger(0):
            ac = -a
            is_negative = True

        whole = [1]
        for _ in range(len(ac)):
            whole.append(0)

        if is_negative:
            return -VInteger(whole)
        else:
            return VInteger(whole)

    @classmethod
    def surplus(cls, a:VInteger):
        '''
        Compute the surplus of an integer over the next lowest whole.
        '''
        if a.is_whole() or a == VInteger(0):
            return VInteger(0)

        ac = a
        is_negative = False

        if a < VInteger(0):
            ac = -a
            is_negative = True

        com = (ac - VProp.next_lowest_whole(ac))

        if is_negative:
            return -com
        else:
            return com


    @classmethod
    def next_lowest_whole(cls, a:VInteger):
        '''
        Compute the next lowest whole of an integer.
        '''
        if a.is_whole() or a == VInteger(0):
            return a

        ac = a
        is_negative = False

        if a < VInteger(0):
            ac = -a
            is_negative = True

        whole = [1]
        for _ in range(len(ac[1:])):
            whole.append(0)

        if is_negative:
            return -VInteger(whole)
        else:
            return VInteger(whole)

