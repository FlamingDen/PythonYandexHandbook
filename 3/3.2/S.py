n = int(input())

stat = {}
for _ in range(n):
    s = input().split()
    name = s[0][:-1]
    toys = list()
    for i in range(1, len(s)):
        if i != len(s) - 1:
            toys.append(s[i][:-1])
        else:
            toys.append(s[i])
    stat[name] = stat.get(name, set()) | set(toys)

res = []
for name, toys in sorted(stat.items()):
    curr_toys = toys.copy()
    for key in stat.keys():
        if key == name:
            continue
        curr_toys -= stat[key]
    
    res += list(curr_toys)

res.sort()
print('\n'.join(res))
    
