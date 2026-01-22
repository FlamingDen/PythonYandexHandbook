from itertools import combinations

n = int(input())
data = [input() for _ in range(n)]
print(*[f"{n1} - {n2}" for n1, n2 in list(combinations(data, 2))], sep="\n")