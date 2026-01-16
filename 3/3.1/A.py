n = int(input())

res = True
for i in range(n):
    s = input()
    if not s.startswith(("а", "б", "в")):
        res = False

if res:
    print("YES")
else:
    print("NO")
