from math import sqrt
from vm import (Triple, TRIPLE_0, TRIPLE_90, TRIPLE_180, TRIPLE_270,
                TRIPLE_360, TRIPLE_30, TRIPLE_45, TRIPLE_60)

class Test_Triple:
    def test_creation(self):
        assert Triple(3, 4, 5).get_values() == (3, 4, 5)
        assert Triple(6, 8, 10).get_values() == (6, 8, 10)
        assert Triple(1.5, 2, 2.5).get_values() == (1.5, 2, 2.5)

    def test_validation(self):
        assert Triple(3, 4, 5).is_valid() == True
        assert Triple(6, 8, 10).is_valid() == True
        assert Triple(1.5, 2, 2.5).is_valid() == True
        assert Triple(5, 4, 9).is_valid() == False
        assert Triple(2, 3, sqrt(13)).is_valid() == True

    def test_repr(self):
        assert repr(Triple(3, 4, 5)) == 'Triple(3, 4, 5)'

    def test_triangle(self):
        assert Triple(3, 4, 5).base() == 3
        assert Triple(3, 4, 5).height() == 4
        assert Triple(3, 4, 5).hypotenuse() == 5

    def test_trig_functions(self):
        assert Triple(3, 4, 5).cos() == 3 / 5
        assert Triple(3, 4, 5).sin() == 4 / 5
        assert Triple(3, 4, 5).tan() == 4 / 3
        assert Triple(3, 4, 5).cosec() == 5 / 3
        assert Triple(3, 4, 5).sec() == 5 / 4
        assert Triple(3, 4, 5).cot() == 3 / 4

    def test_cmparison(self):
        assert Triple(3, 4, 5) == Triple(3, 4, 5)

    def test_complimentary(self):
        assert Triple(3, 4, 5).complimentary() == Triple(4, 3, 5)

    def test_similarity(self):
        assert Triple(3, 4, 5).is_similar(Triple(6, 8, 10)) == True
        assert Triple(3, 4, 5).is_similar(Triple(1.5, 2, 2.5)) == True
        assert Triple(3, 4, 5).is_similar(Triple(8, 6, 10)) == False

        assert Triple(3, 4, 5).multiply(2) == Triple(6, 8, 10)
        assert Triple(3, 4, 5).multiply(2.0) == Triple(6, 8, 10)
        assert Triple(6, 8, 10).divide(2) == Triple(3, 4, 5)
        assert Triple(6, 8, 10).divide(2.0) == Triple(3, 4, 5)
        
        assert Triple(6, 8, 10).reduce() == Triple(3, 4, 5)

    def test_arithmetic(self):
        assert Triple(12, 5, 13) + Triple(3, 4, 5) == Triple(16, 63, 65)
        assert Triple(12, 5, 13).double() == Triple(119, 120, 169)
        assert Triple(3, 4, 5).double() == Triple(-7, 24, 25)
        assert Triple(4, 3, 5) - Triple(15, 8, 17) == Triple(84, 13, 85)
        assert Triple(3, 4, 5) - Triple(4, 3, 5) == Triple(24, 7, 25)
        assert Triple(4, 3, 5) - Triple(3, 4, 5) == Triple(24, -7, 25)

        a = Triple(12, 5, 13)
        b = Triple(5, 12, 13)
        c = Triple(3, -4, 5)
        assert a - b == Triple(120, -119, 169)
        assert b - c == Triple(-33, 56, 65)
        assert c.double() - b == Triple(-323, -36, 325)
        assert a - b - c == Triple(836, 123, 845)
        assert a - a == Triple(169, 0, 169)

        assert Triple(7, 24, 25).half() == Triple(32, 24, 40)
        assert Triple(4, 3, 5).half() == Triple(9, 3, sqrt(90))
        assert Triple(-3, 4, 5).half() == Triple(2, 4, sqrt(20))

    def test_quadrant_triples(self):
        assert TRIPLE_0 == Triple(1, 0, 1)
        assert TRIPLE_90 == Triple(0, 1, 1)
        assert TRIPLE_180 == Triple(-1, 0, 1)
        assert TRIPLE_270 == Triple(0, -1, 1)
        assert TRIPLE_360 == Triple(1, 0, 1)

    def test_arithmetic_with_quadrants(self):
        a = Triple(4, 3, 5)
        assert a + TRIPLE_90 == Triple(-3, 4, 5)
        assert TRIPLE_180 - a == Triple(-4, 3, 5)
        assert a + TRIPLE_180 == Triple(-4, -3, 5)

    def test_angles_30_45_60(self):
        assert TRIPLE_30 == Triple(sqrt(3), 1, 2)
        assert TRIPLE_45 == Triple(1, 1, sqrt(2))
        assert TRIPLE_60 == Triple(1, sqrt(3), 2)
        triple_75 = TRIPLE_30 + TRIPLE_45
        assert triple_75 == Triple(sqrt(3) - 1, 1 + sqrt(3), 2 * sqrt(2))

    