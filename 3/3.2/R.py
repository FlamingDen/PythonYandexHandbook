n = int(input())

treasures = {}
ans = 0
for i in range(n):
    (x, y) = input().split()
    key = (x[:-1], y[:-1])
    treasures[key] = treasures.get(key, 0) + 1
    ans = max(ans, treasures[key])
print(ans)