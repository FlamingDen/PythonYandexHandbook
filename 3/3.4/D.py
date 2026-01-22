from itertools import accumulate

data = input().split()
for i in range(len(data)):
    if i != len(data) - 1:
        data[i] += " "

print(*accumulate(data), sep="\n")

