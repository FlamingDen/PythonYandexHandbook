n = int(input())

for _ in range(n):
    s = input()
    st = s.find("зайка")
    print(st + 1 if st != -1 else "Заек нет =(")