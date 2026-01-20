food = {}

n = int(input())
for i in range(n):
    name = input()
    food[name] = food.get(name, 0) + 1
    
m = int(input())
for i in range(m):
    j = int(input())
    for k in range(j):
        name = input()
        food[name] -= 1

has_cooked = False
for key in sorted(food.keys()):
    val = food[key]
    if val > 0:
        print(key)
        has_cooked = True

if not has_cooked:
    print("Готовить нечего")
