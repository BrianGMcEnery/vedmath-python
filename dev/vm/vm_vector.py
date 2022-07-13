from math import atan, atan2, cos, sin, sqrt
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

class Cylindrical:
    '''Work with cylindrical coords.'''
    def __init__(self, rho, phi, z):
        self.rho = rho
        self.phi = phi
        self.z = z

    def __str__(self) -> str:
        rho, phi, z = self.get_components()
        return f'Cylindrical({rho}, {phi}, {z})'

    def __repr__(self) -> str:
        rho, phi, z = self.get_components()
        return f'Cylindrical({rho}, {phi}, {z})'

    def get_components(self):
        return self.rho, self.phi, self.z

    def __eq__(self, other):
        rho1, phi1, z1 = self.get_components()
        rho2, phi2, z2 = other.get_components()
        return (approx_equal(rho1, rho2) and approx_equal(phi1, phi2) and
                approx_equal(z1, z2))

class Spherical:
    '''Work with spherical coords. 
    https://en.wikipedia.org/wiki/Spherical_coordinate_system'''

    def __init__(self, r, theta, phi):
        self.r = r
        self.theta = theta
        self.phi = phi

    def __str__(self) -> str:
        r, theta, phi = self.get_components()
        return f'Spherical({r}, {theta}, {phi})'

    def __repr__(self) -> str:
        r, theta, phi = self.get_components()
        return f'Spherical({r}, {theta}, {phi})'

    def get_components(self):
        return self.r, self.theta, self.phi

    def __eq__(self, other):
        r1, theta1, phi1 = self.get_components()
        r2, theta2, phi2 = other.get_components()
        return (approx_equal(r1, r2) and approx_equal(theta1, theta2) and
                approx_equal(phi1, phi2))


def cylindrical_of_vec3D(vec:Vec3D) -> Cylindrical:
    x, y, z = vec.get_components()
    return Cylindrical(sqrt(x * x + y * y), atan2(y, x), z)

def cylindrical_of_spherical(sph:Spherical) -> Cylindrical:
    r, theta, phi = sph.get_components()
    return Cylindrical(r * sin(theta), phi, r * cos(theta))

def spherical_of_vec3D(vec:Vec3D) -> Spherical:
    x, y, z = vec.get_components()
    return Spherical(
        sqrt(x * x + y * y + z * z),
        atan2(sqrt(x * x + y * y),  z),
        atan2(y, x)
    )

def spherical_of_cylindrical(cyl:Cylindrical) -> Spherical:
    rho, phi, z = cyl.get_components()
    return Spherical(sqrt(rho * rho + z * z), atan2(rho, z), phi)

def vec3D_of_cylindrical(cyl:Cylindrical) -> Vec3D:
    rho, phi, z = cyl.get_components()
    return Vec3D(rho * cos(phi), rho * sin(phi), z)

def vec3D_of_spherical(sph:Spherical) -> Vec3D:
    r, theta, phi = sph.get_components()
    return Vec3D(
        r * cos(phi) * sin(theta), 
        r * sin(phi) * sin(theta), 
        r * cos(theta)
    )

