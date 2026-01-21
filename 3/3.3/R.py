numbers = {1, 2, 3, 4, 5}
print({num: [curr for curr in range(1, num + 1) if num % curr == 0] for num in numbers})
