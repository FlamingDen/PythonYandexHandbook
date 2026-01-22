from itertools import product, repeat

n = int(input())
res = (a * b for a, b in product([i for i in range(1, n + 1)], repeat=2))
for i, val in enumerate(res):
    if i % n == 0 and i != 0:
        print()
    print(val, end=" ")
