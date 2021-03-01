def to_digits(n):
    '''
    Returns a list of digits of an integer.
    '''
    def digits_inner(i):
        digits.append(i%10)
        if i == 0:
            return digits
        digits_inner(i//10)
    
    digits = []
    if n > 0:
        digits_inner(n)
    elif n == 0:
        digits = [0,0] # two zeros needed here
    else:
        # Handle negative integers
        digits_inner(-n)
        digits = list(map(lambda d: -d, digits))
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
    return list(map(digit_from_vdigit, vds))

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


def all_from_9_last_from_10(ds):
    '''Apply the sutra to a list of digits'''
    def all_from_9(d):
        return 9 - d
    def last_from_10(d):
        return 10 - d

    ans = list(map(all_from_9, ds[:-1]))
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

    truth_values = list(map(lambda e: e > 5, ds))
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

    truth_values = list(map(lambda e: e < 0, ds))
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
    def __init__(self, i):
        if isinstance(i, list):
            digits = i
        else:
            digits = to_digits(i)
        self.d = list(map(lambda d: VDigit(d), digits))

    def __str__(self):
        return f"VInteger({self.d})"
    
    def __repr__(self):
        return f"{self.d}"

    def __len__(self):
        return len(self.d)

    def __neg__(self):
        return VInteger(negate_digits(self.get_digits()))

    def __add__(self, other):
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

        if c.all_zero(): #No carries left
            return s.upadl_zero().from_vinculum()
        else:
            return s + (c.padr_zero(1)) #pad to carry on

    def __sub__(self, other):
        return self + (-other)

    def all_zero(self):
        '''
        Returns True if all the digits are zero.
        '''
        all_True = list(map(lambda e: e == VDigit(0), self.d))
        return False not in all_True

    def padl_zero(self, l):
        '''
        Pad the integer by l leading zero digits on the left.
        '''
        lzeros = []
        for _ in range(l):
            lzeros.append(0)
        padded = lzeros + self.get_digits()
        return VInteger(padded)

    def upadl_zero(self):
        '''
        Take away leading zero's in the integer.
        '''
        ds = self.get_digits()
        idx = 0
        while ds[idx] == 0:
            idx += 1
        return VInteger(ds[idx:])

    def padr_zero(self, l):
        '''
        Pad the integer by l trailing zero digits on the right.
        '''
        rzeros = []
        for _ in range(l):
            rzeros.append(0)
        padded = self.get_digits() + rzeros
        return VInteger(padded)


    def to_vinculum(self):
        '''
        Transforms the digits so the number is written in vinculum form.
        '''
        is_negative = False
        ds = list(map (digit_from_vdigit, self.d))

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
        ds = list(map (digit_from_vdigit, self.d))

        # Handle negative digits
        if ds[0] < 0:
            is_negative = True
            ds = negate_digits(ds)

        ds = _from_vinculum(ds)

        #test to see if all bar digits gone
        truth_values = list(map(lambda e: e < 0, ds))
        while True in truth_values: # needs to go again
            ds = _from_vinculum(ds)
            truth_values = list(map(lambda e: e < 0, ds))

        if is_negative:
            ds = negate_digits(ds)
        
        return VInteger(ds)

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return list(map (digit_from_vdigit, self.d))

    def __getitem__(self, key):
        return self.d[key]

    def __setitem__(self, key, value):
        self.d[key] = value
