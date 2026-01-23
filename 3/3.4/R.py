from itertools import product

condition = input()

status = [0, 1]
result = list(product(status, repeat=3))

print("a b c f")
print(*[f"{a} {b} {c} {1 if eval(condition) else 0}" for a, b, c in result], sep="\n")
