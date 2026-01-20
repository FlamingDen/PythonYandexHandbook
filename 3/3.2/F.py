n = int(input())
m = int(input())

names = set()
for _ in range(n + m):
    name = input()
    if name in names:
        names.remove(name)
    else:
        names.add(name)
    
if len(names) == 0:
    print("Таких нет")
else:
    sorted_list = sorted(names)
    for name in sorted_list:
        print(name)


