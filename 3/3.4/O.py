from itertools import permutations

data = [food for _ in range(int(input())) for food in input().split(", ")]
data.sort()
print(*(" ".join(row) for row in permutations(data, 3)), sep="\n")
