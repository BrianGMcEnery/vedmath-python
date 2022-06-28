from math import sqrt
from vm import Triple

root_13 = sqrt(13)

d = Triple(2, 3, root_13)

print(d.is_valid())
