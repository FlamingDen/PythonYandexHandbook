n = int(input())
m = int(input())

width = len(str(n * m))
data = [i for i in range(1, n * m + 1)]
iters = [iter(data)] * m
result = list(zip(*iters))
for row in result:
    for v in row:
        print(f"{v:>{width}}", end=" ")
    print()
