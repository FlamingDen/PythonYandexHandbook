first = input().split(", ")
second = input().split(", ")

res = list(zip(first, second))
for n1, n2 in res:
    print(f"{n1} - {n2}")