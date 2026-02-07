import math as m

x, y = map(float, input().split())
d, q = map(float, input().split())
print(m.dist((x, y), (d * m.cos(q), d * m.sin(q))))