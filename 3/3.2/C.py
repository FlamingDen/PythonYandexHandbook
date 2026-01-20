n = int(input())

places = set()
for _ in range(n):
    lt = input().split()
    places |= set(lt)

for place in places:
    print(place)