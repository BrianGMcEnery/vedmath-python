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

    # Must handle negative integers
    if n >= 0:
        digits_inner(n)
    else:
        digits_inner(-n)
        digits = list(map(lambda e: -1 * e, digits))

    digits.reverse()
    return digits[1:]


def digit_from_vdigit(vd):
    '''
    Return a digit from a vdigit
    '''
    if (type(vd) == VDigit):
        return vd.get_val()
    else:
        raise ValueError(f"{vd} is of wrong type.")

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
            sum = self._val + other._val
            return VInteger(sum)

    def __sub__(self, other):
        if type(other) == VDigit:
            d = self._val - other._val
            return VInteger(d)
    
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

    def to_vinculum(self):
        '''
        Transforms the digits so the number is written in vinculum form.
        '''
        is_negative = False
        ds = list(map (digit_from_vdigit, self.d))

        # Must handle negative digits
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

        # Must handle negative digits
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
