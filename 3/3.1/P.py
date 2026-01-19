ln = int(input())
n = int(input())

title = []
check = True
for i in range(n):
    s = input()
    if check:
        if len(s) <= ln:
            title.append(s)
            ln -= len(s)
        else:
            if ln > 3:
                title.append(s[: ln - 3] + "...")
            elif ln == 3:
                title[i - 1] += "..."
            else:
                title[i - 1] = title[i - 1][: -(3 - ln)] + "..."
            check = False

for s in title:
    print(s)
