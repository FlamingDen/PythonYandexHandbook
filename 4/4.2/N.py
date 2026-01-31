even_sum = lambda x: sum(int(char) for char in str(x) if char.isdigit()) % 2 == 0
print(*filter(even_sum, (1, 2, 3, 4, 5)))