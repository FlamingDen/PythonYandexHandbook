import math as _m

data = list(map(int, input().split()))
print(_m.pow(_m.prod(data), 1 / len(data)))