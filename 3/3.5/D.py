from sys import stdin

lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))

requst = lines[-1].lower()
for i, line in enumerate(lines[:-1]):
    if requst in line.lower():
        print(lines[i])