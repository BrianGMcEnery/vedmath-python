from .vnumbers import VInteger, VDigit

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

    @classmethod
    def nikhilam_by_9_two_digit(cls, a:VInteger):
        '''
        Special division by 9 as per Tirthaji's book, pp 45.
        '''
        q = a[0].as_vinteger()
        r = a[1].as_vinteger()

        r = r + q

        if r >= VInteger(9):
            r = r - VInteger(9)
            q = q + VInteger(1)

        return {'quotient':q, 'remainder':r}

    @classmethod
    def nikhilam_by_9_three_digit(cls, a:VInteger):
        '''
        Special division by 9 as per Tirthaji's book, pp 46.
        '''
        q = a.all_but_last_as_vinteger()
        r = a.last_as_vinteger()

        q[1] = q[1] + q[0]

        if len(q[1]) == 2:
            q[0] = q[0] + VInteger(1)
            q[1] = q[1] - VInteger(9)
        
        r = r + q[1]

        if len(r) == 2:
            q[1] = q[1] + VInteger(1)
            r = r - VInteger(9)

        if len(q[1]) == 2:
            q[0] = q[0] + VInteger(1)
            q[1] = q[1] - VInteger(10)

        while q.needs_resolution():
            q = q.resolve()

        q = q.unpadl_zero()

        return {'quotient':q, 'remainder':r}

    @classmethod
    def nikhilam_by_9_many_digit(cls, a:VInteger):
        '''
        Special division by 9 for many digit as per Tirthaji's book, pp 46, 47.
        '''
        q = a.all_but_last_as_vinteger()
        r = a.last_as_vinteger()

        for i in range(1, len(q)):
            q[i] = q[i] + q[i-1]
            if len(q[i]) == 2:
                q[i-1] = q[i-1] + VInteger(1)
                q[i] = q[i] - VInteger(9)
        
        r = r + q[-1]

        while r >= VInteger(9):
            q[-1] = q[-1] + VInteger(1)
            r = r - VInteger(9)
        

        for i in range(1, len(q)):
            if len(q[i]) == 2:
                q[i-1] = q[i-1] + VInteger(1)
                q[i] = q[i] - VInteger(10)

        while q.needs_resolution():
            q = q.resolve()

        q = q.unpadl_zero() #eliminate any leading zero's 
        return {'quotient':q, 'remainder':r}

    @classmethod
    def nikhilam_by_8_many_digit(cls, a:VInteger):
        '''
        Special division by 8 for many digit as per Tirthaji's book, pp 47.
        '''
        q = a.all_but_last_as_vinteger()
        r = a.last_as_vinteger()

        for i in range(1, len(q)):
            q[i] = q[i] + VInteger(2) * q[i-1]
            if len(q[i]) == 2:
                q[i-1] = q[i-1] + VInteger(1)
                q[i] = q[i] - VInteger(8)
        
        r = r + VInteger(2) * q[-1]

        while r >= VInteger(8):
            q[-1] = q[-1] + VInteger(1)
            r = r - VInteger(8)

        for i in range(1, len(q)):
            if len(q[i]) == 2:
                q[i-1] = q[i-1] + VInteger(1)
                q[i] = q[i] - VInteger(10)

        while q.needs_resolution():
            q = q.resolve()

        q = q.unpadl_zero() #eliminate any leading zero's 
        return {'quotient':q, 'remainder':r}

    @classmethod
    def nikhilam_by_7_many_digit(cls, a:VInteger):
        '''
        Special division by 7 for many digit as per Tirthaji's book, pp 47.
        '''
        q = a.all_but_last_as_vinteger()
        r = a.last_as_vinteger()

        for i in range(1, len(q)):
            q[i] = q[i] + VInteger(3) * q[i-1]
            if len(q[i]) == 2:
                q[i-1] = q[i-1] + VInteger(1)
                q[i] = q[i] - VInteger(7)
        
        r = r + VInteger(3) * q[-1]

        while r >= VInteger(7):
            q[-1] = q[-1] + VInteger(1)
            r = r - VInteger(7)

        for i in range(1, len(q)):
            if len(q[i]) == 2:
                q[i-1] = q[i-1] + VInteger(1)
                q[i] = q[i] - VInteger(10)

        while q.needs_resolution():
            q = q.resolve()

        q = q.unpadl_zero() #eliminate any leading zero's 
        return {'quotient':q, 'remainder':r}



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

