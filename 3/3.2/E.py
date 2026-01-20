n = int(input())
m = int(input())

names = set()
for _ in range(n + m):
    name = input()
    if name in names:
        names.remove(name)
    else:
        names.add(name)
    
    
sz = len(names)
print(sz if sz != 0 else "Таких нет")

