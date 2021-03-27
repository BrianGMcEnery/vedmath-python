import numbers
import functools

from vedmath import VDigit, int_to_digits, digits_from_vdigits

class VInt:
    '''
    An experimental class for vedic integers.
    '''

    def __init__(self, n:int):
        '''
        Initialise a VInt from an integer n.
        '''
        self.ds = [VDigit(d) for d in int_to_digits(n)]

    @classmethod
    def fromvdigits(cls, ds):
        '''
        Return a VInt from a list of digits as VDigits.
        '''
        ans = cls(0)
        ans.ds = ds
        return ans

    def __repr__(self):
        '''
        Provide a string representation of a VInt.
        '''
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
        return functools.reduce(lambda x, y: 10 * x + y, self.get_digits() , 0)

    def get_digits(self):
        '''
        Returns a list of the digits as ints
        '''
        return digits_from_vdigits(self.ds)