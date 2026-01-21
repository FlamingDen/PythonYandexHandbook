a = 5
b = -4
# 2 способа
print([x**2 for x in range(a, b + 1)] if a < b else [x**2 for x in range(a, b - 1, -1)])
print([x**2 for x in range(a, b + (1 if a < b else -1), 1 if a < b else -1)])
