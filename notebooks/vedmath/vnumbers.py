import copy
import functools

def int_to_digits(n):
    '''
    Returns a list of digits of an integer.
    '''
    digits = []

    def digits_inner(i):
        if i == 0:
            return
        digits.append(i%10)
        digits_inner(i//10)
    
    if n > 0:
        digits_inner(n)
    elif n == 0:
        digits = [0]
    else:
        # Handle negative integers
        digits_inner(-n)
        digits = [-d for d in digits]
    digits.reverse()
    return digits


def digit_from_vdigit(vd):
    '''
    Return a digit from a vdigit.
    '''
    if (type(vd) == VDigit):
        return vd.d
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
    
    def __init__(self, d):
        if d in range(-9, 10):
            self.d = d
        else:
            raise ValueError(f'{d} is not a digit.')

    def __str__(self):
        return f"VDigit({self.d})"

    def __repr__(self):
        return f"{self.d}"

    def __add__(self, other):
        if type(other) == VDigit:
            ans = self.d + other.d
        elif type(other) == VInteger:
            ans = self.d + int(other)
        return VInteger(ans)

    def __sub__(self, other):
        if type(other) == VDigit:
            ans = self.d - other.d
            return VInteger(ans)

    def __mul__(self, other):
        if type(other) == VDigit:
            ans = self.d * other.d
            return VInteger(ans)

    def __neg__(self):
        return VDigit(-self.d)
        
    def __abs__(self):
        return VDigit(abs(self.d))

    def __eq__(self, other):
        if type(other) == VDigit:
            return self.d == other.d
    
    def as_vinteger(self):
        return VInteger(self.d)

    def __int__(self):
        return self.d


def all_from_9_last_from_10_list(ds):
    '''Apply the sutra to a list of digits'''
    def all_from_9(d):
        return 9 - d
    def last_from_10(d):
        return 10 - d
                           
    return [all_from_9(d) for d in ds[:-1]] + [last_from_10(ds[-1])]

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

def to_vinculum(ds):
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
                ans += negate_digits(all_from_9_last_from_10_list(ds[ci:cip1]))
            else:
                ans += one_more_than_list(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is > 5
                ans += negate_digits(all_from_9_last_from_10_list(ds[ci:]))
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
                ans += all_from_9_last_from_10_list(negate_digits(ds[ci:cip1]))
            else:
                ans += one_less_than_list(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is < 0
                ans += all_from_9_last_from_10_list(negate_digits(ds[ci:]))
        else:
            ans += ds[ci:]

        if ans[0] == 0: #chop leading 0
            ans = ans[1:]
        return ans
   

class VInteger():
    '''
    VInteger is a class for computing with integers.
    '''
    def __init__(self, n:int):
        '''
        Instantiate a VInteger from an integer n.
        '''
        self.ds = [VDigit(d) for d in int_to_digits(n)]

    @classmethod
    def fromints(cls, ds):
        '''
        Return a VInteger from a list of digits as ints.
        '''
        ans = cls(0)
        ans.ds = [VDigit(d) for d in ds]
        return ans

    @classmethod
    def fromvdigits(cls, ds):
        '''
        Return a VInteger from a list of digits as VDigits.
        '''
        ans = cls(0)
        ans.ds = ds
        return ans



    def __str__(self):
        return f"VInteger({self.ds})"
    
    def __repr__(self):
        return f"VInteger({self.ds})"

    def __len__(self):
        return len(self.ds)

    def __neg__(self):
        return VInteger.fromvdigits([-d for d in self.ds])

    def __add__(self, other):
        summ = int(self) + int(other)
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
        prod = int(self) * int(other)
        return VInteger(prod)

    def __eq__(self, other):
        if len(self) == len(other):
            return all(a == b for a, b in zip(self, other))
            
    def __ne__(self, other):
        if type(other) == VInteger:
            return int(self) != int(other)

    def __lt__(self, other):
        if type(other) == VInteger:
            return int(self) < int(other)

    def __le__(self, other):
        if type(other) == VInteger:
            return int(self) <= int(other)

    def __gt__(self, other):
        if type(other) == VInteger:
            return int(self) > int(other)

    def __ge__(self, other):
        if type(other) == VInteger:
            return int(self) >= int(other)

    def __int__(self):
        '''
        Transform a VInteger to an int.
        '''
        return functools.reduce(lambda x, y: 10 * x + y, self.get_digits() , 0)
        
    def all_zero(self):
        '''
        Returns True if all the digits are zero.
        '''
        return all([d == VDigit(0) for d in self.ds])

    def is_whole(self):
        '''
        Returns True if the digits are a one followed by zeros.
        '''
        leading_one = (self.ds[0] == VDigit(1))
        return leading_one and VInteger.fromvdigits(self.ds[1:]).all_zero()

    def padl_zero(self, l0):
        '''
        Pad the integer by l0 leading zero digits on the left.
        '''
        padded = [0 for _ in range(l0)] + self.get_digits()
        return VInteger.fromints(padded)

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
        return VInteger.fromints(ds[idx:])

    def padr_zero(self, l0):
        '''
        Pad the integer by l0 trailing zero digits on the right.
        '''
        padded = self.get_digits() + [0 for _ in range(l0)]
        return VInteger.fromints(padded)


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

        ds = to_vinculum(ds)

        if is_negative:
            ds = negate_digits(ds)

        return VInteger.fromints(ds)

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
        
        return VInteger.fromints(ds).unpadl_zero()

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
        return VInteger.fromints(ds[:-1])

    def last_as_vinteger(self):
        ds = self.get_digits()
        return VInteger.fromints(ds[-1:])

    def all_but_first_as_vinteger(self):
        ds = self.get_digits()
        return VInteger.fromints(ds[1:])

    def first_as_vinteger(self):
        ds = self.get_digits()
        return VInteger.fromints(ds[0])

    def prepend(self, vd):
        '''
        Prepend the VDigit vd to the VInteger.
        '''
        ds = self.ds
        ds.reverse()
        ds.append(vd)
        ds.reverse()
        self.ds = ds

    def resolve(self):
        '''
        Resolve any carries or VInteger mixins.
        '''
        obj = copy.deepcopy(self)
        obj.prepend(VDigit(0)) #in case a carry forward is necessary
        for i, d in enumerate(obj):
            if type(d) == VInteger:
                if len(d) == 1:
                    obj[i] = VDigit(int(d))
                elif len(d) == 2:
                    obj[i] = d[-1]
                    obj[i-1] = obj[i-1] + d[0]
        return obj

    def needs_resolution(self):
        '''
        Test whether the object needs to be resolved.
        '''
        return False in [type(d) == VDigit for d in self.ds]

    def digit_sum(self):
        '''
        Compute the digit sum of a VInteger by summing the digits.
        Elementary Vedic Mathematics pp 24
        '''
        dsum = 0
        for d in self.get_digits():
            dsum = dsum + d

        while dsum > 9:
            ds = int_to_digits(dsum)
            dsum = 0
            for d in ds:
                dsum = dsum + d

        return dsum

    def all_from_9_last_from_10(self):
        return VInteger(all_from_9_last_from_10_list(self.get_digits()))

    def duplex(self):
        '''
        Returns the duplex of a VInteger as a VInteger.
        '''
        ds = self.ds
        ld = len(ds)
        ans = VInteger(0)
        for i in range(0, ld // 2):
            ans = ans + ds[i] * ds[-1-i]
        ans = ans * VInteger(2)
        if ld % 2:
            middle = (ld // 2)
            ans = ans + (ds[middle] * ds[middle])
        return ans

    def square(self):
        '''
        Returns the square of a VInteger as a VInteger using the duplex.
        '''
        ds = self.ds
        ld = len(ds)

        lans = []
        lans = [VInteger.fromvdigits(ds[:i]).duplex() 
            for i in range(1, ld + 1)]
        lans = lans + [VInteger.fromvdigits(ds[i:]).duplex() 
            for i in range(1, ld)]

        ans = VInteger(0)
        for e in lans:
            ans = ans * VInteger(10) + e

        return ans

    def _vc_inner_prod(self, other):
        '''
        Vertical and Crosswise inner product. Assume both VIntegers of same 
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

        lans = []
        lans = [VInteger.fromvdigits(vs[:i])._vc_inner_prod(VInteger.fromvdigits(vo[:i])) 
                    for i in range(1, lvs + 1)]
        lans = lans + [VInteger.fromvdigits(vs[i:])._vc_inner_prod(VInteger.fromvdigits(vo[i:])) 
                    for i in range(1, lvs)]

        ans = VInteger(0)
        for e in lans:
            ans = ans * VInteger(10) + e

        return ans
