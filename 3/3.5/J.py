DEFAULT_ENCODING = {"encoding": "UTF-8"}
file_name = input()
tail = int(input())

data = []
with open(file_name, "r", **DEFAULT_ENCODING) as f:
    for line in f:
        data.append(line.rstrip())

ln = len(data)
print(*data[ln - tail:], sep="\n")