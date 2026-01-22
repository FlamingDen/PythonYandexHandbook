from itertools import permutations

data = [input() for _ in range(int(input()))]
data.sort()
print(*(", ".join(row) for row in permutations(data)), sep="\n")
