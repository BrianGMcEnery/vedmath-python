import random

from vedmath import VInt, VDigit

class Test_VInt:
    def test_creation(self):
        a = VInt(123)
        assert a.get_digits() == [1,2,3]
        a = VInt.fromvdigits([VDigit(1), VDigit(2), VDigit(3)])
        assert a.get_digits() == [1,2,3]
        a = VInt.fromints([1,2,3])
        assert a.get_digits() == [1,2,3]

    def test_comparison(self):
        a = VInt(1234)
        comp = (a == VInt(1234))
        assert comp == True

    def test_slicing(self):
        a = VInt(1234)
        assert len(a) == 4
        assert a[:] == VInt(1234)
        assert a[:-1] == VInt(123)
        assert a[2:] == VInt(34)

    def test_transformation(self):
        a = VInt(1234)
        assert int(a) == 1234

