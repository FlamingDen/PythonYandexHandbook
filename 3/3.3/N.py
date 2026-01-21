data = {'a': [1, 2, 3], 'b': [5, 2, 5], 'c': [7, 15, 3]}
print({key for key, nums in data.items() if len(nums) != len(set(nums))})