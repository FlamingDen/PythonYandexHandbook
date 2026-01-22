from itertools import chain

n = int(input())
data = list(chain(*[input().split(", ") for _ in range(n)]))
for i, val in enumerate(sorted(data), 1):
    print(f"{i}. {val}")