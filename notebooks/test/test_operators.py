import random

from vedmath import VInteger, VMul, VProp

random.seed(0)

class Test_VMul:
    def test_vert_cross(self):
        for _ in range (100):
            i1 = random.randint(-999999999, 999999999)
            i2 = random.randint(-999999999, 999999999)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.vert_cross(v1, v2)
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

class Test_VProp:
    def test_to_vinculum(self):
        assert VProp.to_vinculum(VInteger(19802476)).get_digits() == [2, 0, -2, 0, 2, 5, -2, -4]
        assert VProp.to_vinculum(VInteger(91287625)).get_digits() == [1, -1, 1, 3, -1, -2, -4, 2, 5]

    def test_from_vinculum(self):
        for _ in range(100):
            a = random.randint(-1000000000, 1000000000)
            ads = VInteger(a).get_digits()
            vads = VProp.to_vinculum(VInteger(a))
            vads = VProp.from_vinculum(vads).get_digits()
            assert ads == vads
