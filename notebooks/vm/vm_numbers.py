import numbers, functools

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
    Root class for all digits in vm.
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

class VInt():
    '''
    VInt is a class for computing with integers.
    '''
    def __init__(self, n:int):
        '''
        Instantiate a VInt from an integer n.
        '''
        self.ds = [VDigit(d) for d in int_to_digits(n)]

    @classmethod
    def fromints(cls, ds):
        '''
        Return a VInt from a list of digits as ints.
        '''
        ans = cls(0)
        ans.ds = [VDigit(d) for d in ds]
        return ans

    @classmethod
    def fromvdigits(cls, ds):
        '''
        Return a VInt from a list of digits as VDigits.
        '''
        ans = cls(0)
        ans.ds = ds
        return ans

    def __str__(self):
        return f"VInt({self.ds})"
    
    def __repr__(self):
        return f"VInt({self.ds})"

    def __len__(self):
        '''Return the length of the VInt.'''
        return len(self.ds)

    def __getitem__(self, index):
        '''Return the item specified by index.'''
        cls = type(self)
        if isinstance(index, slice):
            return cls.fromvdigits(self.ds[index])
        elif isinstance(index, numbers.Integral):
            return self.ds[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __int__(self):
        '''Return a VInt transformed to int.'''
        return functools.reduce(lambda x, y: 10 * x + y, self.get_digits(), 0)

    def __eq__(self, other):
        return int(self) == int(other)

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return digits_from_vdigits(self.ds)