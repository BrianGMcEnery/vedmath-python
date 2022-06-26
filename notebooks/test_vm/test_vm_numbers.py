import random
from vm import int_to_digits, digits_from_vdigits, VDigit, VInt

random.seed(0)

def test_int_to_digits():
    assert int_to_digits(345) == [3,4,5]
    assert int_to_digits(0) == [0]
    assert int_to_digits(-345) == [-3, -4, -5]


class Test_VDigit:
    def test_creation(self):
        assert VDigit(7).get_digit() == 7
        assert VDigit(0).get_digit() == 0
        assert VDigit(-3).get_digit() == -3

    def test_list_vdigits(self):
        assert digits_from_vdigits([VDigit(1), VDigit(2)]) == [1,2]

class Test_VInt:
    def test_creation(self):
        a = VInt(3)
        assert a.get_digits() == [3]
        a = VInt(123)
        assert a.get_digits() == [1,2,3]
        a = VInt.from_digits([1,2,3])
        assert a.get_digits() == [1,2,3]
        a = VInt.from_digits([1,-2,3])
        assert a.get_digits() == [1,-2,3]
        a = VInt.from_vdigits([VDigit(1), VDigit(2), VDigit(3)])
        assert a.get_digits() == [1,2,3]
        a = VInt.from_vdigits([VDigit(1), VDigit(-2), VDigit(3)])
        assert a.get_digits() == [1,-2,3]
        

    def test_comparison(self):
        a = VInt(1234)
        assert (a == VInt(1234)) == True
        assert (a != VInt(1334)) == True
        assert (a < VInt(2234)) == True
        assert (a <= VInt(2234)) == True
        assert (a > VInt(234)) == True
        assert (a >= VInt(234)) == True

    def test_slicing(self):
        a = VInt(1234)
        assert len(a) == 4
        assert a[2] == VDigit(3)
        assert a[:] == VInt(1234).get_vdigits()
        assert a[:-1] == VInt(123).get_vdigits()
        assert a[2:] == VInt(34).get_vdigits()

    def test_transformation(self):
        a = VInt(1234)
        assert int(a) == 1234
        a = VInt.from_digits([1, -2, 3])
        assert int(a) == 83

    def test_zero(self):
        a = VInt(1234)
        assert a.all_zero() == False
        a = VInt(0)
        assert a.all_zero() == True
        a = VInt.from_digits([0, 0, 0])
        assert a.all_zero() == True
        a = VInt.from_digits([0, 1, 0])
        assert a.all_zero() == False

    def test_whole(self):
        a = VInt(1000)
        assert a.is_whole() == True
        a = VInt(2000)
        assert a.is_whole() == False
        assert a.is_whole(VDigit(2)) == True
        a = VInt(2345)
        assert a.is_whole() == False

    def test_padding(self):
        a = VInt(1234)
        
        b = a.padl_zero(4)
        assert b.get_digits() == [0, 0, 0, 0, 1, 2, 3, 4]
        assert b.unpadl_zero().get_digits() == [1, 2, 3, 4]

        c = a.padr_zero(4)
        assert c.get_digits() == [1, 2, 3, 4, 0, 0, 0, 0]
        assert c.unpadr_zero().get_digits() == [1, 2, 3, 4]