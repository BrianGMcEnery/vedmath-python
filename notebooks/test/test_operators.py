import random

from vedmath import VInteger, VMul, VDiv, VProp

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

    def test_under_base(self):
        for _ in range (5):
            i1 = random.randint(87, 99)
            i2 = random.randint(87, 99)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.under_base(v1, v2)
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

        for _ in range (5):
            i1 = random.randint(870, 999)
            i2 = random.randint(870, 999)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.under_base(v1, v2)
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

    def test_over_base(self):
        for _ in range (5):
            i1 = random.randint(101, 120)
            i2 = random.randint(101, 120)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.over_base(v1, v2)
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

        for _ in range (5):
            i1 = random.randint(1001, 1200)
            i2 = random.randint(1001, 1200)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.over_base(v1, v2)
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

    def test_near_base(self):
        for _ in range (10):
            i1 = random.randint(81, 120)
            i2 = random.randint(81, 120)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.near_base(v1, v2, base=VInteger(100))
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

        for _ in range (10):
            i1 = random.randint(801, 1200)
            i2 = random.randint(801, 1200)
            v1 = VInteger(i1)
            v2 = VInteger(i2)
            mv1v2 = VMul.near_base(v1, v2, base=VInteger(1000))
            assert mv1v2.get_digits() == VInteger(i1 * i2).get_digits()

class Test_VDiv:
    def test_nikhilam_by_9_two_digit(self):
        ans = VDiv.nikhilam_by_9_two_digit(VInteger(12))
        assert ans == {'quotient': VInteger(1), 'remainder': VInteger(3)}
        ans = VDiv.nikhilam_by_9_two_digit(VInteger(62))
        assert ans == {'quotient': VInteger(6), 'remainder': VInteger(8)}
        ans = VDiv.nikhilam_by_9_two_digit(VInteger(65))
        assert ans == {'quotient': VInteger(7), 'remainder': VInteger(2)}
        ans = VDiv.nikhilam_by_9_two_digit(VInteger(72))
        assert ans == {'quotient': VInteger(8), 'remainder': VInteger(0)}

    def test_nikhilam_by_9_three_digit(self):
        ans = VDiv.nikhilam_by_9_three_digit(VInteger(103))
        assert ans == {'quotient': VInteger(11), 'remainder': VInteger(4)}
        ans = VDiv.nikhilam_by_9_three_digit(VInteger(211))
        assert ans == {'quotient': VInteger(23), 'remainder': VInteger(4)}
        ans = VDiv.nikhilam_by_9_three_digit(VInteger(871))
        assert ans == {'quotient': VInteger(96), 'remainder': VInteger(7)}
        ans = VDiv.nikhilam_by_9_three_digit(VInteger(877))
        assert ans == {'quotient': VInteger(97), 'remainder': VInteger(4)}


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

    def test_deficit(self):
        assert VProp.deficit(VInteger(825)).get_digits() == [-1, -7, -5]
        assert VProp.deficit(VInteger(-825)).get_digits() == [1, 7, 5]
        assert VProp.deficit(VInteger([3, 4, 5])).get_digits() == [-6, -5, -5]
        assert VProp.deficit(VInteger([3, -4, 5])).get_digits() == [-7, -3, -5]
        assert VProp.deficit(VInteger(100)).get_digits() == [0]

    def test_surplus(self):
        assert VProp.surplus(VInteger(113)).get_digits() == [1, 3]
        assert VProp.surplus(VInteger(-113)).get_digits() == [-1, -3]
        assert VProp.surplus(VInteger([1, 2, 3, 7])).get_digits() == [2, 3, 7]
        assert VProp.surplus(VInteger([1, 2, -3, -7])).get_digits() == [1, 6, 3]
        assert VProp.surplus(VInteger(100)).get_digits() == [0]

