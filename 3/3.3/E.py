numbers = [number for number in range(16, 100, 4)]
print({el for el in numbers if round(el ** (1 / 2)) ** 2 == el})
