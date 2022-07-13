from math import sqrt

from vm import (Quaternion, QUATERNION_1, QUATERNION_I, QUATERNION_J,
                QUATERNION_K, approx_equal)

class Test_Quaternion:
    def test_creation(self):
        assert Quaternion(1, 2, 3, 4).get_components() == (1, 2, 3, 4)
        assert Quaternion(1.5, 2, 2.5, 1.0).get_components() == (1.5, 2, 2.5, 1.0)
        
    def test_repr(self):
        assert repr(Quaternion(1, 2, 3, 4)) == 'Quaternion(1, 2, 3, 4)'

    def test_str(self):
        assert str(Quaternion(1, 2, 3, 4)) == '1 + 2i + 3j + 4k'

    def test_neg(self):
        assert -Quaternion(1, 2, 3, 4) == Quaternion(-1, -2, -3, -4)

    def test_mult_basis(self):
        assert QUATERNION_I * QUATERNION_1 == QUATERNION_I
        assert QUATERNION_1 * QUATERNION_J == QUATERNION_J
        assert QUATERNION_K * QUATERNION_1 == QUATERNION_K

        assert QUATERNION_I * QUATERNION_I == - QUATERNION_1
        assert QUATERNION_J * QUATERNION_J == - QUATERNION_1

        assert QUATERNION_I * QUATERNION_J == QUATERNION_K
        assert QUATERNION_J * QUATERNION_I == - QUATERNION_K

        assert QUATERNION_J * QUATERNION_K == QUATERNION_I
        assert QUATERNION_K * QUATERNION_J == - QUATERNION_I
        assert QUATERNION_K * QUATERNION_I == QUATERNION_J
        assert QUATERNION_I * QUATERNION_K == - QUATERNION_J

        assert QUATERNION_I * QUATERNION_J * QUATERNION_K == - QUATERNION_1
        assert QUATERNION_K * QUATERNION_K == - QUATERNION_1

    def test_scalar_vector(self):
        assert Quaternion(1, 2, 3, 4).scalar_part() == Quaternion(1, 0, 0, 0)
        assert Quaternion(1, 2, 3, 4).vector_part() == Quaternion(0, 2, 3, 4)

    def test_conjugate(self):
        assert Quaternion(1, 2, 3, 4).conjugate() == Quaternion(1, -2, -3, -4)
        
        p = Quaternion(1, 2, 3, 4)
        p_star = p.conjugate()
        q = Quaternion(5, 6, 7, 8)
        q_star = q.conjugate()
        pq = p * q
        pq_star = pq.conjugate()
        assert pq_star == q_star * p_star
        assert pq_star != p_star * q_star

        s = Quaternion(1, 2, 3, 4).scalar_part()
        v = Quaternion(1, 2, 3, 4).vector_part()
        assert s == (p + p_star)/2
        assert v == 1 / 2 * (p - p_star)

    def test_norm(self):
        p = Quaternion(1, 2, 3, 4)
        assert p.norm() == sqrt(1 * 1 + 2 * 2 + 3 * 3 + 4 * 4)

        q = Quaternion(5, 6, 7, 8)
        assert approx_equal((p * q).norm(), p.norm() * q.norm())

    def test_unit(self):
        p = Quaternion(1, 2, 3, 4)
        up = p.unit()
        assert approx_equal(up.norm(), 1)

        rp = p.reciprocal()
        assert p * rp == QUATERNION_1

        (norm, unit) = p.polar_decomposition()
        assert p == norm * unit
