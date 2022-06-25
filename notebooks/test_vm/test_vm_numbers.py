import random
from vm import int_to_digits, VDigit, digit_from_vdigit

random.seed(0)

def test_int_to_digits():
    assert int_to_digits(345) == [3,4,5]
    assert int_to_digits(0) == [0]
    assert int_to_digits(-345) == [-3, -4, -5]


class Test_VDigit:
    def test_creation(self):
        assert digit_from_vdigit(VDigit(7)) == 7
        assert digit_from_vdigit(VDigit(0)) == 0
        assert digit_from_vdigit(VDigit(-3)) == -3
