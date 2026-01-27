import json
from sys import stdin

ans = [line.rstrip("\n") for line in stdin]

file_answers = "scoring.json"
DEFAULT_ENCODING = {"encoding": "UTF-8"}
scors = 0
with open(file_answers, "r", **DEFAULT_ENCODING) as f:
    data = json.load(f)
    i = 0
    for group in data:
        point_per_test = group["points"] // len(group["tests"])
        for test in group["tests"]:
            if test["pattern"] == ans[i]:
                scors += point_per_test
            i += 1

print(scors)
