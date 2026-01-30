def grow(*args, **data):
    result = [*args]
    for key, val in data.items():
        n = len(key)
        for i, num in enumerate(args, 0):
            if num % n == 0:
                result[i] += val
    return tuple(result)

print(grow(12, 5, 30, 60, 15, first=13, second=2, Bob=7))
# print(grow(1, 2, 3, 4, 5, ab=7, dad=10))
