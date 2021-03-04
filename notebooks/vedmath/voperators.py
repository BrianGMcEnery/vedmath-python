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
        return a * b

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
        whole = [1]
        for _ in range(len(a)):
            whole.append(0)

        return (VInteger(whole) - a)