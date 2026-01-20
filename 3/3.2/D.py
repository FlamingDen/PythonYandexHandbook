n = int(input())
m = int(input())

s1 = set()
for _ in range(n):
    s1.add(input())
s2 = set()
for _ in range(m):
    s2.add(input())
    
sz = len(s1 & s2)
print(sz if sz != 0 else "Таких нет")

