from math import sqrt, gcd
from vm import Triple

d = Triple(2, 3, sqrt(13))
two_d = Triple(4, 6, 2*sqrt(13))

print(d.is_valid())
print(two_d.is_valid())

print(d.is_similar(two_d))

two_ds = two_d.get_values()

ratio = gcd(two_ds[0], two_ds[1])