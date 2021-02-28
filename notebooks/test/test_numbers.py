import random

from vedmath import *

def test_to_digits():
    assert to_digits(345) == [3,4,5]
    assert to_digits(0) == []
    assert to_digits(-345) == [-3, -4, -5]

random.seed(0)

class Test_VDigit:
    def test_creation(self):
        assert digit_from_vdigit(VDigit(7)) == 7
        assert digit_from_vdigit(VDigit(0)) == 0
        assert digit_from_vdigit(VDigit(-3)) == -3

    def test_add(self):
        d1 = VDigit(1)
        d3 = VDigit(3)
        d9 = VDigit(9)
        dm9 = VDigit(-9)
        assert (d1 + d3).get_digits() == [4]
        assert (d3 + d9).get_digits() == [1,2]
        assert (d3 + dm9).get_digits() == [-6]

    def test_sub(self):
        d1 = VDigit(1)
        d3 = VDigit(3)
        d9 = VDigit(9)
        dm9 = VDigit(-9)
        assert (d1 - d3).get_digits() == [-2]
        assert (d3 - d9).get_digits() == [-6]
        assert (d3 - dm9).get_digits() == [1,2]

    def test_mul(self):
        d1 = VDigit(1)
        d3 = VDigit(3)
        d9 = VDigit(9)
        dm9 = VDigit(-9)
        assert (d1 * d3).get_digits() == [3]
        assert (d3 * d9).get_digits() == [2, 7]
        assert (d3 * dm9).get_digits() == [-2, -7]

    def test_neg(self):
        d1 = VDigit(1)
        d3 = VDigit(3)
        d9 = VDigit(9)
        dm9 = VDigit(-9)
        assert -d1 == VDigit(-1)
        assert -d3 == VDigit(-3)
        assert -d9 == VDigit(-9)
        assert -dm9 == VDigit(9)

    def test_abs(self):
        d1 = VDigit(1)
        d3 = VDigit(3)
        d9 = VDigit(9)
        dm9 = VDigit(-9)
        assert abs(d1) == VDigit(1)
        assert abs(d3) == VDigit(3)
        assert abs(d9) == VDigit(9)
        assert abs(dm9) == VDigit(9)


class Test_VNumber:
    # This test is here for completion of the import
    def test_creation(self):
        assert type (VNumber()) == VNumber


class Test_VInteger:
    def test_to_vinculum(self):
        assert VInteger(4).to_vinculum().get_digits() == [4]
        assert VInteger(8).to_vinculum().get_digits() == [1, -2]
        assert VInteger(35).to_vinculum().get_digits() == [3, 5]
        assert VInteger(38).to_vinculum().get_digits() == [4, -2]
        assert VInteger(62).to_vinculum().get_digits() == [1, -4, 2]
        assert VInteger(67).to_vinculum().get_digits() == [1, -3, -3]
        assert VInteger(243).to_vinculum().get_digits() == [2, 4, 3]
        assert VInteger(207).to_vinculum().get_digits() == [2, 1, -3]
        assert VInteger(267).to_vinculum().get_digits() == [3, -3, -3]
        assert VInteger(627).to_vinculum().get_digits() == [1, -4, 3, -3]
        assert VInteger(672).to_vinculum().get_digits() == [1, -3, -3, 2]
        assert VInteger(19802476).to_vinculum().get_digits() == [2, 0, -2, 0, 2, 5, -2, -4]
        assert VInteger(91287625).to_vinculum().get_digits() == [1, -1, 1, 3, -1, -2, -4, 2, 5]

    def test_from_vinculum(self):
        for _ in range(100):
            a = random.randint(-1000000000, 1000000000)
            ads = VInteger(a).get_digits()
            vads = VInteger(a).to_vinculum().from_vinculum().get_digits()
            assert ads == vads