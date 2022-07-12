from vm import (Quaternion, QUATERNION_1, QUATERNION_I, QUATERNION_J,
                QUATERNION_K)

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








