numbers = set(range(11, 50, 2))
print({num for num in numbers if len([curr for curr in range(1, num // 2 + 1) if num % curr == 0]) == 1})