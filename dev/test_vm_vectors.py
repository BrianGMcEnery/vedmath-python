from math import atan, pi, sin, sqrt

from vm import (Vec3D, VEC3D_0, VEC3D_I, VEC3D_J, VEC3D_K,
                Cylindrical, cylindrical_of, vec3D_of)

class Test_Vec3D:
    def test_creation(self):
        assert Vec3D(1, 2, 3).get_components() == (1, 2, 3)
        assert Vec3D(1.5, 2, 2.5).get_components() == (1.5, 2, 2.5)
        
    def test_repr(self):
        assert repr(Vec3D(1, 2, 3)) == 'Vec3D(1, 2, 3)'

    def test_str(self):
        assert str(Vec3D(1, 2, 3)) == '1i + 2j + 3k'

    def test_neg(self):
        assert -Vec3D(1, 2, 3) == Vec3D(-1, -2, -3)

    def test_add_sub(self):
        assert Vec3D(1, 2, 3) + Vec3D(4, 5, 6) == Vec3D(5, 7, 9)
        assert Vec3D(1, 2, 3) - Vec3D(4, 5, 6) == Vec3D(-3, -3, -3)

    def test_basis(self):
        assert VEC3D_0 == Vec3D(0, 0, 0)
        assert VEC3D_I == Vec3D(1, 0, 0)
        assert VEC3D_J == Vec3D(0, 1, 0)
        assert VEC3D_K == Vec3D(0, 0, 1)

        assert VEC3D_I.dot(VEC3D_I) == 1
        assert VEC3D_I.dot(VEC3D_J) == 0

        assert VEC3D_I.cross(VEC3D_J) == VEC3D_K
        assert VEC3D_K.cross(VEC3D_J) == -VEC3D_I
        assert VEC3D_K.cross(VEC3D_K) == VEC3D_0

    def test_dot_cross_mul(self):
        assert Vec3D(1, 2, 3).dot(Vec3D(4, 5, 6)) == 32
        assert Vec3D(1, 2, 3).cross(Vec3D(1, 2, 3)) == VEC3D_0

        a = Vec3D(1, 2, 3)
        b = Vec3D(4, -5, 6)
        c = Vec3D(7, 8, 9)
        r = 2.0

        assert a.cross(b + c) == a.cross(b) + a.cross(c)

        assert r * a == Vec3D(2.0, 4.0, 6.0)
        assert (r * a).cross(b) == a.cross(r * b) == r * (a.cross(b))

        # Scalar triple product

        assert a.dot(b.cross(c)) == b.dot(c.cross(a))
        assert a.dot(b.cross(c)) == c.dot(a.cross(b))

class Test_Cylindrical:
    def test_creation(self):
        assert Cylindrical(2, pi/3, 1).get_components() == (2, pi/3, 1)
        
    def test_repr(self):
        assert repr(Cylindrical(1, 2, 3)) == 'Cylindrical(1, 2, 3)'

    def test_str(self):
        assert str(Cylindrical(1, 2, 3)) == 'Cylindrical(1, 2, 3)'

def test_changing_coordinates():
    cyl = Cylindrical(2, -pi/3, 1)
    assert vec3D_of(cyl) == Vec3D(1.0, 2 * sin(-pi / 3), 1.0)

    vec = Vec3D(1, 2, 3)
    assert cylindrical_of(vec) == Cylindrical(sqrt(5), atan(2), 3)