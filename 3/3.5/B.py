from sys import stdin

sum = 0
n = 0
for line in stdin:
    name, st, end = line.split()
    sum += int(end) - int(st)
    n += 1 
print(round(sum / n))
