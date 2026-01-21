numbers = [1, 2, 3]
print(max(i * j for j in numbers for i in numbers if i != j))
