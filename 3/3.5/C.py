from sys import stdin

for line in stdin:
    if not line.startswith("#"):
        print(line[:line.find("#")])    