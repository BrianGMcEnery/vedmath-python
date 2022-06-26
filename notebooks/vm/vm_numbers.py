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


def digits_from_vdigits(vds):
    '''
    Return a list of digits from a list of vdigits.
    '''
    return [vd.get_digit() for vd in vds]

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
        return f"VDigit({self.d})"

    def __eq__(self, other):
        '''Return a equality test based on int comparison.'''
        return self.d == other.d

    def get_digit(self):
        '''Return the digit.'''
        return self.d


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
    def from_digits(cls, ds):
        '''
        Return a VInt from a list of digits as ints.
        '''
        ans = cls(0)
        ans.ds = [VDigit(d) for d in ds]
        return ans

    @classmethod
    def from_vdigits(cls, ds):
        '''
        Return a VInt from a list of VDigits.
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
            return self.ds[index]
        elif isinstance(index, numbers.Integral):
            return self.ds[index]
        else:
            raise TypeError(f'{cls.__name__} indices must be integers or slices')

    def __int__(self):
        '''Return a VInt transformed to int.'''
        return functools.reduce(lambda x, y: 10 * x + y, self.get_digits(), 0)

    def __eq__(self, other):
        '''Return a == test based on int comparison.'''
        return int(self) == int(other)

    def __ne__(self, other):
        '''Return a != test based on int comparison.'''
        return int(self) != int(other)

    def __lt__(self, other):
        '''Return a < test based on int comparison.'''
        return int(self) < int(other)
    
    def __le__(self, other):
        '''Return a <= test based on int comparison.'''
        return int(self) <= int(other)

    def __gt__(self, other):
        '''Return a < test based on int comparison.'''
        return int(self) > int(other)
    
    def __ge__(self, other):
        '''Return a <= test based on int comparison.'''
        return int(self) >= int(other)

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return digits_from_vdigits(self.ds)

    def get_vdigits(self):
        '''
        Returns a list of the vdigits
        '''
        return self.ds

    def all_zero(self):
        '''
        Returns True if all the digits are zero.
        '''
        return all([d == VDigit(0) for d in self.ds])

    def is_whole(self, vd=VDigit(1)):
        '''
        Returns True if there is a single digit vd followed by zeros.
        '''
        leading = vd == self[0]
        remainder_zero = VInt.from_vdigits(self[1:]).all_zero()
        return leading and remainder_zero

    def padl_zero(self, l0):
        '''
        Pad the integer by l0 leading zero digits on the left.
        '''
        padded = [0 for _ in range(l0)] + self.get_digits()
        return VInt.from_digits(padded)

    def unpadl_zero(self):
        '''
        Take away leading zero's in the integer, unless the integer is zero.
        '''
        if self.all_zero():
            return VInt(0)
        ds = self.get_digits()
        idx = 0
        while ds[idx] == 0:
            idx += 1
        return VInt.from_digits(ds[idx:])

    def padr_zero(self, l0):
        '''
        Pad the integer by l0 trailing zero digits on the right.
        '''
        padded = self.get_digits() + [0 for _ in range(l0)]
        return VInt.from_digits(padded)

    def unpadr_zero(self):
        '''
        Take away trailing zero's in the integer, unless the integer is zero.
        '''
        if self.all_zero():
            return VInt(0)
        ds = self.get_digits()
        idx = len(ds) - 1
        while ds[idx] == 0:
            idx -= 1
        return VInt.from_digits(ds[:idx + 1])