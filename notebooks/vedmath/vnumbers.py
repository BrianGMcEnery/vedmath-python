from sympy import Basic, S, Expr, latex
from .vdigits import *

def _to_vinculum(ds):
    '''
    Returns the digits ds in vinculum form.
    '''
    def all_from_9(d):
        return 9 - d

    def last_from_10(d):
        return 10 - d

    def all_from_9_last_from_10(ds):
        '''Apply the sutra to a list of digits'''
        ans = list(map(all_from_9, ds[:-1]))
        ans = ans + [last_from_10(ds[-1])]
        return ans

    def negate(ds):
        '''Negate a list of digits'''
        return [-d for d in ds]
    
    def one_more_than(d):
        return d + 1

    def one_more_than_list(ds):
        if ds == []:
            return [1]
        else:
            ds[-1] += 1
            return ds

    def find_splits(dt):
        '''Find out where the truth values change'''
        splits = [0]
        current = dt[0]
        try:
            while True:
                idx = dt.index(not current, splits[-1])
                splits.append(idx)
                current = not current
        except:
            return splits


    truth_values = list(map(lambda e: e > 5, ds))
    split_indxs = find_splits(truth_values)

    if truth_values[0]: #the first element is > 5
        ans = [1]
    else:
        ans = []


    idx = 0

    try:
        while True:
            sp1 = split_indxs[idx]
            sp2 = split_indxs[idx+1]
            if truth_values[sp1]: #the element is > 5
                ans += negate(all_from_9_last_from_10(ds[sp1:sp2]))
            else:
                ans += one_more_than_list(ds[sp1:sp2])

            idx += 1
    except:
        sp = split_indxs[idx]
        if truth_values[sp]: #the element is > 5
                ans += negate(all_from_9_last_from_10(ds[sp:]))
        else:
            ans += ds[sp:]
        return ans
    
    

class VNumber(Basic):
    '''
    Root class for all numbers in vedmath.
    '''
    pass


class VInteger(VNumber):
    __slots__ = ('d',)

    def __new__(cls, i):
        obj = Expr.__new__(cls)
        if isinstance(i, list):
            digits = i
        else:
            digits = get_digits(i)
        obj.d = list(map(digit_to_vdigit, digits))
        return obj

    def _latex(self, printer):
        return latex(self.d)

    def to_vinculum(self):
        '''
        Transforms the digits so the number is written in vinculum form.
        '''
        ds = list(map (digit_from_vdigit, self.d))
        return VInteger(_to_vinculum(ds))

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return list(map (digit_from_vdigit, self.d))
