from itertools import cycle, islice

n = int(input())
porr = [input() for _ in range(n)]
m = int(input())
print(*islice((cycle(porr)), 0, m, 1), sep="\n")