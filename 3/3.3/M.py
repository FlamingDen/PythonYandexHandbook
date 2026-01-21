data = {'a': [1, 2, 3], 'b': [1, 2, 3]}
print(min((sum(val), key) for key, val in data.items())[1])