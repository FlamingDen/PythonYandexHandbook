fl = lambda x: isinstance(x[1], list) and any(val % 2 == 0 for val in x[1])

print(dict(filter(
    fl,
    {'first': 2, 'second': '2 + 2 = 4', 'third': [1, 2, 3]}.items()
)))