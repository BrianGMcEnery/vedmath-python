from math import sqrt, gcd
from vm import (Triple, Quadruple, CodeNumber, QuadCodeNumber, Quintuple,
                code_number_of, triple_of, quad_code_number_of, quadruple_of,
                sub_quadruples)

qcn = quad_code_number_of(Quadruple(-1, 0, 0, 1))

q = quadruple_of(QuadCodeNumber(1, 0, 1))

diff = sub_quadruples(Quadruple(2, 3, 6, 7), Quadruple(2, 2, 1, 3))

