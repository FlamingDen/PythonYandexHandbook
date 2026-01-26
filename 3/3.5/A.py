from sys import stdin

res = 0
for line in stdin:
    res += sum(map(int, line.split()))
print(res)