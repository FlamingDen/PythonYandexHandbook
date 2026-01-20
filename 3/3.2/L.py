names = {}

n = int(input())
for i in range(n):
    name = input()
    names[name] = names.get(name, 0) + 1

count = 0
for name in sorted(names.keys()):
    count_name = names[name]  
    if count_name >= 2:
        count += count_name
        print(f"{name} - {count_name}")

if count == 0:
    print("Однофамильцев нет")