from vedmath import *

def test_to_digits():
    assert to_digits(345) == [3,4,5]
    assert to_digits(0) == []
