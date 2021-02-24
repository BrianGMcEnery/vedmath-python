from vedmath import *

def test_get_digits():
    assert get_digits(345) == [3,4,5]
    assert get_digits(0) == []
