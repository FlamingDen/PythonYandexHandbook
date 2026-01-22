from itertools import product

n = int(input())

print("А Б В")
data = product((i for i in range(1, n - 1)), repeat=2)
print(*(f"{a} {b} {n - a - b}" for a, b in data if n - a - b >= 1), sep="\n")
