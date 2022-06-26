import numbers, functools

def int_to_digits(n:int):
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

def negate_digits(ds):
    '''Negate a list of digits'''
    return [-d for d in ds]

def all_from_9_last_from_10(ds:list):
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


def to_vinculum(ds):
    '''
    Returns the digits ds in vinculum form.
    '''

    def one_more_than(ds:list):
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
                ans += one_more_than(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is > 5
                ans += negate_digits(all_from_9_last_from_10(ds[ci:]))
        else:
            ans += ds[ci:]
        return ans

def from_vinculum(ds):
    '''
    Returns the digits ds in normal form.
    '''
    
    def one_less_than(ds:list):
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
                ans += one_less_than(ds[ci:cip1])
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

        return VInt.from_digits(ds)

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

        ds = from_vinculum(ds)

        #test to see if all bar digits gone
        truth_values = [d < 0 for d in ds]
        while True in truth_values: # needs to go again
            ds = from_vinculum(ds)
            truth_values = [d < 0 for d in ds]

        if is_negative:
            ds = negate_digits(ds)
        
        return VInt.from_digits(ds).unpadl_zero()

    def first_digit(self):
        return self[0]

    def all_but_first_digit(self):
        return self[1:]

    def last_digit(self):
        return self[-1]

    def all_but_last_digit(self):
        return self[:-1]

    def digit_sum(self):
        '''
        Compute the digit sum of a VInt by summing the digits.
        Elementary Vedic Mathematics pp 24
        '''
        dsum = 0
        for d in self.get_digits():
            dsum = dsum + d

        while abs(dsum) > 9:
            ds = int_to_digits(dsum)
            dsum = 0
            for d in ds:
                dsum = dsum + d

        if dsum < 0:
           return dsum + 9
        return dsum

    def all_from_9_last_from_10(self):
        ds = self.get_digits()
        negative = False
        if ds[0] < 0:
            negative = True
            ds = negate_digits(ds)

        af9l10 = all_from_9_last_from_10(ds)
        if negative:
            af9l10 = negate_digits(af9l10)

        return VInt.from_digits(af9l10)
        