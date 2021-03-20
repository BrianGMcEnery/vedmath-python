import random

from vedmath import VInteger, VMonomial

random.seed(0)

class Test_VMonomial:
    def test_duplex_square(self):
        m = VMonomial([VInteger(3)])
        assert m.duplex() == VInteger(9)
        m = VMonomial([VInteger(4), VInteger(3)])
        assert m.duplex() == VInteger(24)
        m = VMonomial([VInteger(5), VInteger(2), VInteger(3)])
        assert m.duplex() == VInteger(34)

        m = VMonomial([VInteger(3)])
        assert m.square() == VMonomial([VInteger(9)])
        m = VMonomial([VInteger(4), VInteger(3)])
        assert m.square() == VMonomial([VInteger(16), VInteger(24), VInteger(9)])
        m = VMonomial([VInteger(5), VInteger(2), VInteger(3)])
        assert m.square() == VMonomial([VInteger(25), VInteger(20), 
            VInteger(34), VInteger(12), VInteger(9)])