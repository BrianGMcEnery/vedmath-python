import random
from vm import (int_to_digits, negate_digits, all_from_9_last_from_10, 
    find_truth_changes, to_vinculum, from_vinculum, 
    digits_from_vdigits, VDigit, VInt)

random.seed(0)

def test_int_to_digits():
    assert int_to_digits(345) == [3,4,5]
    assert int_to_digits(0) == [0]
    assert int_to_digits(-345) == [-3, -4, -5]

def test_negate_digits():
    assert negate_digits([3, 4, 5]) == [-3, -4, -5]
    assert negate_digits([-3, 4, -5]) == [3, -4, 5]

def test_af9l10():
    assert all_from_9_last_from_10([3, 4, 6]) == [6, 5, 4]

def test_truth_changes():
    assert find_truth_changes([True, False]) == [0, 1]
    assert find_truth_changes([True, False, True]) == [0, 1, 2]
    assert find_truth_changes([True, True, True]) == [0]
    assert find_truth_changes([True, True, False]) == [0, 2]

def test_to_vinculum():
    assert to_vinculum([3, 4, 5]) == [3, 4, 5]
    assert to_vinculum([3, 7, 8]) == [4, -2, -2]
    assert to_vinculum([6, 7, 8]) == [1, -3, -2, -2]
    assert to_vinculum([3, 7, 8, 1, 7, 6]) == [4, -2, -2, 2, -2, -4]

def test_from_vinculum():
    assert from_vinculum([3,4,5]) == [3,4,5]
    assert from_vinculum([4, -2, -2]) == [3, 7, 8]
    assert from_vinculum([1, -3, -2, -2]) == [6, 7, 8]
    assert from_vinculum([4, -2, -2, 2, -2, -4]) == [3, 7, 8, 1, 7, 6]


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

    def test_to_vinculum(self):
        assert VInt(4).to_vinculum().get_digits() == [4]
        assert VInt(8).to_vinculum().get_digits() == [1, -2]
        assert VInt(35).to_vinculum().get_digits() == [3, 5]
        assert VInt(38).to_vinculum().get_digits() == [4, -2]
        assert VInt(62).to_vinculum().get_digits() == [1, -4, 2]
        assert VInt(67).to_vinculum().get_digits() == [1, -3, -3]
        assert VInt(243).to_vinculum().get_digits() == [2, 4, 3]
        assert VInt(207).to_vinculum().get_digits() == [2, 1, -3]
        assert VInt(267).to_vinculum().get_digits() == [3, -3, -3]
        assert VInt(627).to_vinculum().get_digits() == [1, -4, 3, -3]
        assert VInt(672).to_vinculum().get_digits() == [1, -3, -3, 2]
        assert (VInt(19802476).to_vinculum().get_digits() == 
        [2, 0, -2, 0, 2, 5, -2, -4])
        assert (VInt(91287625).to_vinculum().get_digits() == 
        [1, -1, 1, 3, -1, -2, -4, 2, 5])


    def test_from_vinculum(self):
        a = VInt(1234)
        assert a.from_vinculum() == VInt(1234)
        a = VInt.from_digits([2, -3, -2, -2])
        assert a.from_vinculum().get_digits() == [1, 6, 7, 8]
        a = VInt.from_digits([-2, 3, 2, 2])
        assert a.from_vinculum().get_digits() == [-1, -6, -7, -8]
        a = VInt.from_digits([2, -3, -2, -2, 1, -1, -1])
        assert a.from_vinculum().get_digits() == [1, 6, 7, 8, 0, 8, 9]

    def test_from_vinculum_further(self):
        for _ in range(100):
            a = random.randint(-1000000000, 1000000000)
            ads = VInt(a).get_digits()
            vads = VInt(a).to_vinculum().from_vinculum().get_digits()
            assert ads == vads

    def test_first_last(self):
        a = VInt(123456)
        assert a.first_digit() == VDigit(1)
        assert a.all_but_first_digit() == VInt(23456).get_vdigits()
        assert a.last_digit() == VDigit(6)
        assert a.all_but_last_digit() == VInt(12345).get_vdigits()

    def test_digit_sum(self):
        a = VInt(1234)
        assert a.digit_sum() == 1
        a = VInt.from_digits([2, -3, -2, -2])
        assert a.digit_sum() == 4
        a = VInt.from_digits([1, 6, 7, 8, 0, 8, 9])
        assert a.digit_sum() == 3
        a = VInt.from_digits([2, -3, -2, -2, 1, -1, -1])
        assert a.digit_sum() == 3

    def test_all_from_9_last_10(self):
        a = VInt(346)
        assert a.all_from_9_last_from_10() == VInt(654)
        a = VInt(-346)
        assert a.all_from_9_last_from_10() == VInt(-654)