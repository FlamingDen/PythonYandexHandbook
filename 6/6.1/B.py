from sys import stdin
import math as _m

for line in stdin:
    print(_m.gcd(*list(map(int, line.split()))))
