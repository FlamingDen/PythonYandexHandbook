n = int(input())

count = 0
for _ in range(n):
    s = input()
    count += s.count("зайка")
print(count)
    