n = int(input())

titles = []
for _ in range(n):
    titles.append(input())    
request = input().lower()

for i, title in enumerate(titles):
    curr = title.lower()
    if request in curr:
        print(title)
    
