from vm import approx_equal

class Vec3D:
    '''Simple class for 3-D vectors.'''

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        x, y, z = self.get_components()
        return f'{x}i + {y}j + {z}k'

    def __repr__(self) -> str:
        x, y, z = self.get_components()        
        return f'Vec3D({x}, {y}, {z})'

    def get_components(self):
        return self.x, self.y, self.z

    def __eq__(self, other):
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = other.get_components()
        return (approx_equal(x1, x2) and approx_equal(y1, y2) and
                approx_equal(z1, z2))

    def __neg__(self):
        x, y, z = self.get_components()
        return Vec3D(-x, -y, -z)

    def __add__(self, other):
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = other.get_components()
        return Vec3D(x1 + x2, y1 + y2, z1 + z2)

    def __sub__(self, other):
        return self + (- other)

    def __rmul__(self, a:float):
        x, y, z = self.get_components()
        return Vec3D(x * a, y * a, z * a)

    def dot(self, other):
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = other.get_components()
        return x1 * x2 + y1 * y2 + z1 * z2

    def cross(self, other):
        x1, y1, z1 = self.get_components()
        x2, y2, z2 = other.get_components()
        return Vec3D(
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2
        )


VEC3D_0 = Vec3D(0, 0, 0)
VEC3D_I = Vec3D(1, 0, 0)
VEC3D_J = Vec3D(0, 1, 0)
VEC3D_K = Vec3D(0, 0, 1)
