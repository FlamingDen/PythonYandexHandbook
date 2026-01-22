from itertools import count

start, end, step = map(float, input().split())

print()
for val in count(start, step):
    if val > end:
        break
    print(val)