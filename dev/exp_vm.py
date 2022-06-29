from math import sqrt, gcd
from vm import (Triple, TRIPLE_45, TRIPLE_30, TRIPLE_60, Quadruple,
                CodeNumber, CODENUMBER_30, CODENUMBER_45, CODENUMBER_60, 
                code_number_of, triple_of)

t = Quadruple(2, -1, 2, 3)

trips = t.get_composite_triples()
print(trips)

print([t.is_valid() for t in trips])

print(sqrt(5))








