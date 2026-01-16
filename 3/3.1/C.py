ln = int(input())
n = int(input())

for _ in range(n):
    s = input()
    if len(s) > ln:
        s = s[:ln - 3] 
        s += "..."
    print(s)
