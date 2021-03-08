def to_digits(n):
    '''
    Returns a list of digits of an integer.
    '''
    digits = []

    def digits_inner(i):
        digits.append(i%10)
        if i == 0:
            return digits
        digits_inner(i//10)
    
    
    if n > 0:
        digits_inner(n)
    elif n == 0:
        digits = [0,0] # two zeros needed here
    else:
        # Handle negative integers
        digits_inner(-n)
        digits = [-d for d in digits]
    digits.reverse()
    return digits[1:]


def digit_from_vdigit(vd):
    '''
    Return a digit from a vdigit.
    '''
    if (type(vd) == VDigit):
        return vd.get_val()
    else:
        raise ValueError(f"{vd} is not a VDigit.")

def digits_from_vdigits(vds):
    '''
    Return a list of digits from a list of vdigits.
    '''
    return [digit_from_vdigit(vd) for vd in vds]

class VDigit:
    """
    Root class for all digits in vedmath.
    """
    _val = None

    def __init__(self, d):
        if d in range(-9, 10):
            self._val = d
        else:
            raise ValueError(f'{d} is not a digit.')

    def __str__(self):
        return f"VDigit({self.get_val()})"

    def __repr__(self):
        return f"{self.get_val()}"

    def __add__(self, other):
        if type(other) == VDigit:
            ans = self._val + other._val
            return VInteger(ans)

    def __sub__(self, other):
        if type(other) == VDigit:
            ans = self._val - other._val
            return VInteger(ans)

    def __mul__(self, other):
        if type(other) == VDigit:
            ans = self._val * other._val
            return VInteger(ans)

    def __neg__(self):
        return VDigit(-self._val)
        
    def __abs__(self):
        return VDigit(abs(self._val))

    def __eq__(self, other):
        if type(other) == VDigit:
            return self._val == other._val
    
    def get_val(self):
        return self._val

    def as_vinteger(self):
        return VInteger(self._val)


def all_from_9_last_from_10(ds):
    '''Apply the sutra to a list of digits'''
    def all_from_9(d):
        return 9 - d
    def last_from_10(d):
        return 10 - d

    ans = [all_from_9(d) for d in ds[:-1]]
    ans = ans + [last_from_10(ds[-1])]
    return ans

def find_truth_changes(truth_values):
    '''Find out where the truth values change'''
    changes = [0]
    current = truth_values[0]
    try:
        while True:
            idx = truth_values.index(not current, changes[-1])
            changes.append(idx)
            current = not current
    except:
        return changes

def negate_digits(ds):
    '''Negate a list of digits'''
    return [-d for d in ds]

def _to_vinculum(ds):
    '''
    Returns the digits ds in vinculum form.
    '''

    def one_more_than_list(ds):
        '''Apply one_more_than to the last element of a list'''
        if ds == []:
            return [1]
        else:
            ds[-1] += 1
            return ds

    truth_values = [e > 5 for e in ds]
    change_indxs = find_truth_changes(truth_values)
    
    #special case to handle the first element
    if truth_values[0]: #the first element is > 5
        ans = [1]
    else:
        ans = []

    idx = 0
    try:
        while True:
            ci = change_indxs[idx]
            cip1 = change_indxs[idx+1]
            if truth_values[ci]: #the element is > 5
                ans += negate_digits(all_from_9_last_from_10(ds[ci:cip1]))
            else:
                ans += one_more_than_list(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is > 5
                ans += negate_digits(all_from_9_last_from_10(ds[ci:]))
        else:
            ans += ds[ci:]
        return ans
    
def _from_vinculum(ds):
    '''
    Returns the digits ds in normal form.
    '''
    
    def one_less_than_list(ds):
        '''Apply one_less_than to the last element of a list'''
        if ds == [1]:
            return [0]
        else:
            ds[-1] -= 1
            return ds

    truth_values = [e < 0 for e in ds]
    change_indxs = find_truth_changes(truth_values)
    
    ans = []
    idx = 0
    try:
        while True:
            ci = change_indxs[idx]
            cip1 = change_indxs[idx+1]
            if truth_values[ci]: #the element is < 0
                ans += all_from_9_last_from_10(negate_digits(ds[ci:cip1]))
            else:
                ans += one_less_than_list(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is < 0
                ans += all_from_9_last_from_10(negate_digits(ds[ci:]))
        else:
            ans += ds[ci:]

        if ans[0] == 0: #chop leading 0
            ans = ans[1:]
        return ans
   

class VNumber():
    '''
    Root class for all numbers in vedmath.
    '''
    pass


class VInteger(VNumber):
    '''
    VInteger is a class for computing with integers.
    '''
    def __init__(self, n):
        '''
        Instantiate a VInteger with
            n: int
            n: list of digits as ints
            n: list of digits as VDigits
        '''
        if isinstance(n, int):
            digits = to_digits(n)
        elif isinstance(n, list):
            if isinstance(n[0], int):
                digits = n
            elif isinstance(n[0], VDigit):
                digits = digits_from_vdigits(n)
            
        self.ds = [VDigit(d) for d in digits]

    def __str__(self):
        return f"VInteger({self.ds})"
    
    def __repr__(self):
        return f"{self.ds}"

    def __len__(self):
        return len(self.ds)

    def __neg__(self):
        return VInteger(negate_digits(self.get_digits()))

    def __add__(self, other):
        summ = self.to_int() + other.to_int()
        return VInteger(summ)

    def _add_later(self, other):
        #will use this later

        #handle zero addition
        if self.all_zero():
            ds = other.get_digits()
            return VInteger(ds)
        elif other.all_zero():
            ds = self.get_digits()
            return VInteger(ds)
        
        vs = self.to_vinculum()
        vo = other.to_vinculum()
        l = len(vs) - len(vo)
        if l > 0:
            vo = vo.padl_zero(l)
        elif l < 0:
            vs = vs.padl_zero(-l)

        s = [] #to hold the sum
        c = [] #to hold the carries
        
        for vz in zip(vs, vo):
            su = vz[0] + vz[1]
            s.append(su[-1])
            if len(su) == 1:
                c.append(VDigit(0))
            else:
                c.append(su[0])
        
        s = VInteger(digits_from_vdigits(s))
        c = VInteger(digits_from_vdigits(c))
        
        s = s.from_vinculum()
        
        if c.all_zero(): #No carries left
            return s
        else:
            return s + (c.padr_zero(1)) #pad to carry on

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        prod = self.to_int() * other.to_int()
        return VInteger(prod)

    def __eq__(self, other):
        if type(other) == VInteger:
            return self.to_int() == other.to_int()

    def __ne__(self, other):
        if type(other) == VInteger:
            return self.to_int() != other.to_int()

    def __lt__(self, other):
        if type(other) == VInteger:
            return self.to_int() < other.to_int()

    def __le__(self, other):
        if type(other) == VInteger:
            return self.to_int() <= other.to_int()

    def __gt__(self, other):
        if type(other) == VInteger:
            return self.to_int() > other.to_int()

    def __ge__(self, other):
        if type(other) == VInteger:
            return self.to_int() >= other.to_int()

    def to_int(self):
        '''
        Transform a VInteger to an int.
        '''
        ds = self.get_digits()
        ans = 0
        for d in ds:
            ans = 10 * ans + d
        return ans

    def _mul_vert_cross_len_2(self, other):
        vs = self
        vo = other
        l = len(vs) - len(vo)
        if l > 0:
            vo = vo.padl_zero(l)
        elif l < 0:
            vs = vs.padl_zero(-l)

        vc = [] #to hold the vertical and cross products
        p = [] #to hold the product
        fc = [] #to hold the first carries
        sc = [] #to hold the second carries
        
        vc.append(vs[0] * vo[0]) #right most vertical product
        if len(vs) > 1 and len (vo) > 1:
            vc.append(vs[1] * vo[0] + vs[0] * vo[1]) # cross product
            vc.append(vs[1] * vo[1]) #left most vertical product
        
        for v in vc:
            if len(v)== 1:
                fc.append(VDigit(0))
                sc.append(VDigit(0))

            elif len(v) == 2:
                fc.append(v[0])
                sc.append(VDigit(0))
            else:
                fc.append(v[1])
                sc.append(v[0])

        p = [digit_from_vdigit(e[-1]) for e in vc]
        fc = [digit_from_vdigit(e) for e in fc]
        sc = [digit_from_vdigit(e) for e in sc]
        
        p =  VInteger(p) + VInteger(fc).padr_zero(1) + VInteger(sc).padr_zero(2)

        return p.unpadl_zero()

    def _mul_vert_cross_len_3(self, other):
        vs = self
        vo = other
        l = len(vs) - len(vo)
        if l > 0:
            vo = vo.padl_zero(l)
        elif l < 0:
            vs = vs.padl_zero(-l)

        vc = [] #to hold the vertical and cross products
        p = [] #to hold the product
        fc = [] #to hold the first carries
        sc = [] #to hold the second carries
        
        vc.append(vs[0] * vo[0]) #right most vertical product
        vc.append(vs[1] * vo[0] + vs[0] * vo[1]) # cross product
        vc.append(vs[1] * vo[1] + vs[2] * vo[0] + vs[0] * vo[2]) #central product
        vc.append(vs[2] * vo[1] + vs[1] * vo[2]) # cross product
        vc.append(vs[2] * vo[2]) #left most vertical product
        
        for v in vc:
            if len(v)== 1:
                fc.append(VDigit(0))
                sc.append(VDigit(0))
            elif len(v) == 2:
                fc.append(v[0])
                sc.append(VDigit(0))
            else:
                fc.append(v[1])
                sc.append(v[0])
        
        p = [digit_from_vdigit(e[-1]) for e in vc]
        fc = [digit_from_vdigit(e) for e in fc]
        sc = [digit_from_vdigit(e) for e in sc]
        
        p =  VInteger(p) + VInteger(fc).padr_zero(1) + VInteger(sc).padr_zero(2)

        return p.unpadl_zero()

    def _mul_vert_cross_len_4(self, other):
        vs = self
        vo = other
        l = len(vs) - len(vo)
        if l > 0:
            vo = vo.padl_zero(l)
        elif l < 0:
            vs = vs.padl_zero(-l)

        vc = [] #to hold the vertical and cross products
        p = [] #to hold the product
        fc = [] #to hold the first carries
        sc = [] #to hold the second carries
        
        vc.append(vs[0] * vo[0]) #right most vertical product
        vc.append(vs[1] * vo[0] + vs[0] * vo[1]) # cross product
        vc.append(vs[1] * vo[1] + vs[2] * vo[0] + vs[0] * vo[2]) #central product
        vc.append(vs[0] * vo[3] + vs[3] * vo[0] + vs[1] * vo[2] + vs[2] * vo[1])
        vc.append(vs[2] * vo[2] + vs[3] * vo[1] + vs[1] * vo[3]) #central product
        vc.append(vs[3] * vo[2] + vs[2] * vo[3]) # cross product
        vc.append(vs[3] * vo[3]) #left most vertical product
        
        for v in vc:
            if len(v)== 1:
                fc.append(VDigit(0))
                sc.append(VDigit(0))
            elif len(v) == 2:
                fc.append(v[0])
                sc.append(VDigit(0))
            else:
                fc.append(v[1])
                sc.append(v[0])
        
        p = [digit_from_vdigit(e[-1]) for e in vc]
        fc = [digit_from_vdigit(e) for e in fc]
        sc = [digit_from_vdigit(e) for e in sc]
        
        p =  VInteger(p) + VInteger(fc).padr_zero(1) + VInteger(sc).padr_zero(2)

        return p.unpadl_zero()

    def _mul_vert_cross(self, other):
        vs = self
        vo = other
        l0 = len(vs) - len(vo)
        if l0 > 0:
            vo = vo.padl_zero(l0)
        elif l0 < 0:
            vs = vs.padl_zero(-l0)

        
        lvs = len(vs) - 1
        #the following generates indices for vert and crosswise mults
        #see the jupyter-lab notebook VertCross pattern.
        pat_top = [[(j-i,i) for i in range(j+1)] for j in range(lvs + 1)]
        k = list(range(lvs, 0, -1))
        pat_bot = [[(j-i + k[j],i + k[j]) for i in range(j + 1)] 
            for j in range(lvs - 1, -1, -1)]
            
        pat = pat_top + pat_bot
        
        #the following forms the individual summations
        def sum_func(indx):
            def in_sum_func(t):
                (e1, e2) = t
                return vs[e1] * vo[e2]
            sum = VInteger(0)
            li = len(indx)
            for i in indx:
                sum = sum + in_sum_func(i)
                if li <= 1:
                    break
                li -= 1
            return sum
        
        vc = [] #to hold the vertical and cross products
        for indx in pat:
            vc.append(sum_func(indx))

        p = [] #to hold the product
        fc = [] #to hold the first carries
        sc = [] #to hold the second carries
        tc = [] #to hold the third carries

        #handle the carries
        for v in vc:
            if len(v)== 1:
                fc.append(VDigit(0))
                sc.append(VDigit(0))
                tc.append(VDigit(0))
            elif len(v) == 2:
                fc.append(v[0])
                sc.append(VDigit(0))
                tc.append(VDigit(0))
            elif len(v) == 3:
                fc.append(v[1])
                sc.append(v[0])
                tc.append(VDigit(0))
            else:
                fc.append(v[2])
                sc.append(v[1])
                tc.append(v[0])
        
        p = [digit_from_vdigit(e[-1]) for e in vc]
        fc = [digit_from_vdigit(e) for e in fc]
        sc = [digit_from_vdigit(e) for e in sc]
        tc = [digit_from_vdigit(e) for e in tc]
        
        p =  (VInteger(p) + VInteger(fc).padr_zero(1) + 
                VInteger(sc).padr_zero(2) + VInteger(tc).padr_zero(3))

        return p.unpadl_zero()


    def all_zero(self):
        '''
        Returns True if all the digits are zero.
        '''
        all_zero = [d == VDigit(0) for d in self.ds]
        return False not in all_zero

    def is_whole(self):
        '''
        Returns True if the digits are a one followed by zeros.
        '''
        leading_one = (self.ds[0] == VDigit(1))
        rest_zero = [d == VDigit(0) for d in self.ds[1:]]
        return leading_one and (False not in rest_zero)

    def padl_zero(self, l0):
        '''
        Pad the integer by l0 leading zero digits on the left.
        '''
        padded = [0 for _ in range(l0)] + self.get_digits()
        return VInteger(padded)

    def unpadl_zero(self):
        '''
        Take away leading zero's in the integer, unless the integer is zero.
        '''
        if self.all_zero():
            return VInteger(0)
        ds = self.get_digits()
        idx = 0
        while ds[idx] == 0:
            idx += 1
        return VInteger(ds[idx:])

    def padr_zero(self, l0):
        '''
        Pad the integer by l0 trailing zero digits on the right.
        '''
        padded = self.get_digits() + [0 for _ in range(l0)]
        return VInteger(padded)


    def to_vinculum(self):
        '''
        Transforms the digits so the number is written in vinculum form.
        '''
        is_negative = False
        ds = self.unpadl_zero().get_digits()

        # Handle negative digits
        if ds[0] < 0:
            is_negative = True
            ds = negate_digits(ds)

        ds = _to_vinculum(ds)

        if is_negative:
            ds = negate_digits(ds)

        return VInteger(ds)

    def from_vinculum(self):
        '''
        Transforms the digits so the number is written in normal form.
        '''
        is_negative = False
        ds = self.unpadl_zero().get_digits()

        # Handle negative digits
        if ds[0] < 0:
            is_negative = True
            ds = negate_digits(ds)

        ds = _from_vinculum(ds)

        #test to see if all bar digits gone
        truth_values = [d < 0 for d in ds]
        while True in truth_values: # needs to go again
            ds = _from_vinculum(ds)
            truth_values = [d < 0 for d in ds]

        if is_negative:
            ds = negate_digits(ds)
        
        return VInteger(ds).unpadl_zero()

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return [digit_from_vdigit(d) for d in self.ds]

    def __getitem__(self, key):
        return self.ds[key]

    def __setitem__(self, key, value):
        self.ds[key] = value

    def all_but_last_as_vinteger(self):
        ds = self.get_digits()
        return VInteger(ds[:-1])

    def last_as_vinteger(self):
        ds = self.get_digits()
        return VInteger(ds[-1])

    def all_but_first_as_vinteger(self):
        ds = self.get_digits()
        return VInteger(ds[1:])

    def first_as_vinteger(self):
        ds = self.get_digits()
        return VInteger(ds[0])
