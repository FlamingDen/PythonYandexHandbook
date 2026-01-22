from itertools import chain

n = 3

# # простой способ
# data = [word for _ in range(n) for word in input().split(", ")]
# for i, val in enumerate(sorted(data), 1):
#     print(f"{i}. {val}")
    
# chain
data = list(chain(*[input().split(", ") for _ in range(n)]))
data.sort()
for i, val in enumerate(sorted(data), 1):
    print(f"{i}. {val}")