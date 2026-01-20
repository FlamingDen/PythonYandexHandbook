names = dict()

n = int(input())
for i in range(n):
    name = input()
    names[name] = names.get(name, 0) + 1

count = 0
for key in names:
    val = names[key]
    if val >= 2:
        count += val
print(count)