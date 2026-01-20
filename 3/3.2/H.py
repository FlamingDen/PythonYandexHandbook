n = int(input())

s = dict()
for i in range(n):
    name, *food = input().split()
    for type in food:
        s[type] = s.get(type, []) + [name]

ans = s.get(input(), [])
if len(ans) != 0:
    ans.sort()
    for name in ans:
        print(name)
else:
    print("Таких нет")
