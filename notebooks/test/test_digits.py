from vedmath import *

def test_get_digits():
    assert get_digits(345) == [3,4,5]
    assert get_digits(0) == []

class TestVInteger:
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





