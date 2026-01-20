food = {}

n = int(input())
for i in range(n):
    name = input()
    food[name] = food.get(name, 0) + 1
    
ans = list()
m = int(input())
for i in range(m):
    dish_name = input()
    j = int(input())
    count = 0
    for k in range(j):
        name = input()
        if name in food:
            count += 1
    if count == j:
        ans.append(dish_name)
        
if len(ans) == 0:
    print("Готовить нечего")
else:
    ans.sort()
    for val in ans:
        print(val)


    
