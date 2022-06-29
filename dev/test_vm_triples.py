from math import sqrt
from vm import (Triple, TRIPLE_0, TRIPLE_90, TRIPLE_180, TRIPLE_270,
                TRIPLE_360, TRIPLE_30, TRIPLE_45, TRIPLE_60, CodeNumber,
                CODENUMBER_0, CODENUMBER_90, CODENUMBER_180, CODENUMBER_270, 
                CODENUMBER_360, CODENUMBER_30, CODENUMBER_45, CODENUMBER_60,
                code_number_of, triple_of)

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
        assert a - a == Triple(1, 0, 1)

        assert Triple(7, 24, 25).half() == Triple(4, 3, 5)
        assert Triple(4, 3, 5).half() == Triple(3, 1, sqrt(10))
        assert Triple(-3, 4, 5).half() == Triple(1, 2, sqrt(5))

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

class Test_CodeNumber:
    def test_creation(self):
        assert CodeNumber(7, 3).get_values() == (7, 3)
    
    def test_repr(self):
        assert repr(CodeNumber(7, 3)) == 'CodeNumber(7, 3)'

    def test_constant_codenumbers(self):
        assert CODENUMBER_0 == CodeNumber(1, 0)
        assert CODENUMBER_90 == CodeNumber(1, 1)
        assert CODENUMBER_180 == CodeNumber(0, 1)
        assert CODENUMBER_270 == CodeNumber(1, -1)
        assert CODENUMBER_360 == CodeNumber(1, 0)

        assert CODENUMBER_30 == CodeNumber(2 + sqrt(3))
        assert CODENUMBER_45 == CodeNumber(1 + sqrt(2))
        assert CODENUMBER_60 == CodeNumber(sqrt(3))

        assert CODENUMBER_45 + CODENUMBER_45 == CODENUMBER_90
        assert CODENUMBER_90 - CODENUMBER_30 == CODENUMBER_60 

    def test_arithmetic(self):
        assert CodeNumber(5, 2) + CodeNumber(3, 1) == CodeNumber(13, 11)
        assert CodeNumber(5, 3) - CodeNumber(9, 2) == CodeNumber(3, 1)

        # sum of complimentary triples, see following test.
        assert CodeNumber(20, 9) + CodeNumber(29, 11) == CODENUMBER_90

        # sum of supplimentary triples, see following test.
        assert CodeNumber(20, 9) + CodeNumber(9, 20) == CODENUMBER_180

    def test_complimentary_supplimentary(self):
        assert CodeNumber(20, 9).complimentary() == CodeNumber(29, 11)
        assert CodeNumber(5, -2).complimentary() == CodeNumber(3, 7)
        assert CodeNumber(20, 9).supplimentary() == CodeNumber(9, 20)
        assert CodeNumber(7).supplimentary() == CodeNumber(1, 7)


def test_code_number_and_triple():
    assert code_number_of(Triple(21, 20, 29)) == CodeNumber(5, 2)
    assert triple_of(CodeNumber(5, 2)) == Triple(21, 20, 29)
    assert triple_of(CodeNumber(6)) == Triple(35, 12, 37)
    assert triple_of(CodeNumber(10, 3)) == Triple(91, 60, 109)
    assert triple_of(CodeNumber(-6, -4)) == Triple(5, 12, 13)