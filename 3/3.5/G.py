input_file = input()

data = []
with open(input_file, "r", encoding="UTF-8") as f:
    for line in f:
        data += map(int, line.split())

ln = len(data)
data_sum = sum(data)

print(ln)
print(len([1 for num in data if num > 0]))
print(min(data))
print(max(data))
print(data_sum)
print(round(data_sum / (1 if ln == 0 else ln), 2))
