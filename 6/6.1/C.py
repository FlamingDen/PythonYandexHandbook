import math as _m

n, m = map(int, input().split())

all_perm = _m.comb(n, m)
print(all_perm - _m.comb(n - 1, m), all_perm)
