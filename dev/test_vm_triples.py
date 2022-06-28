from vm import Triple

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

    def test_cmparison(self):
        assert Triple(3, 4, 5) == Triple(3, 4, 5)

    def test_complimentary(self):
        assert Triple(3, 4, 5).complimentary() == Triple(4, 3, 5)

    def test_similarity(self):
        assert Triple(3, 4, 5).similar(Triple(6, 8, 10)) == True
        assert Triple(3, 4, 5).similar(Triple(1.5, 2, 2.5)) == True
        assert Triple(3, 4, 5).similar(Triple(8, 6, 10)) == False

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

        