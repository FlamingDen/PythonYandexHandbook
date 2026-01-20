res = set()
while (s := input()) != "":
    row = list(s.split())
    for i, word in enumerate(row):
        if word == "зайка":
            if i > 0:
                res.add(row[i - 1])
            if i < len(row) - 1:
                res.add(row[i + 1])

for t in res:
    print(t)                
            
