from sympy import Basic, S, Expr, latex
from .vdigits import *

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

def _to_vinculum(ds):
    '''
    Returns the digits ds in vinculum form.
    '''
    def negate(ds):
        '''Negate a list of digits'''
        return [-d for d in ds]
    
    def one_more_than(d):
        return d + 1

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
                ans += negate(all_from_9_last_from_10(ds[ci:cip1]))
            else:
                ans += one_more_than_list(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is > 5
                ans += negate(all_from_9_last_from_10(ds[ci:]))
        else:
            ans += ds[ci:]
        return ans
    
def _from_vinculum(ds):
    '''
    Returns the digits ds in normal form.
    '''
    def negate(ds):
        '''Negate a list of digits'''
        return [-d for d in ds]
    
    def one_more_than(d):
        return d + 1

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
                ans += all_from_9_last_from_10(negate(ds[ci:cip1]))
            else:
                ans += one_less_than_list(ds[ci:cip1])
            idx += 1
    except:
        #handle the final change
        ci = change_indxs[idx]
        if truth_values[ci]: #the element is < 0
                ans += all_from_9_last_from_10(negate(ds[ci:]))
        else:
            ans += ds[ci:]

        if ans[0] == 0: #chop leading 0
            ans = ans[1:]
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
            digits = to_digits(i)
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

    def from_vinculum(self):
        '''
        Transforms the digits so the number is written in normal form.
        '''
        ds = list(map (digit_from_vdigit, self.d))
        ds = _from_vinculum(ds)

        #test to see if all bar digits gone
        truth_values = list(map(lambda e: e < 0, ds))
        while True in truth_values: # needs to go again
            ds = _from_vinculum(ds)
            truth_values = list(map(lambda e: e < 0, ds))
        
        return VInteger(ds)

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return list(map (digit_from_vdigit, self.d))
