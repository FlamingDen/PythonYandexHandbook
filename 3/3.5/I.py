import re

first = input()
second = input()
DEFAULT_ENCODING = {"encoding": "UTF-8"}

res = []
with open(first, "r", **DEFAULT_ENCODING) as f:
    for line in f:
        s = re.findall(r"\S+", line.replace("\t", ""))
        if len(s) != 0:
            res.append(" ".join(s))

with open(second, "w", **DEFAULT_ENCODING) as f:
    print(*res, sep="\n", file=f)
