from sys import stdin
import json

file = input()

data_new = {}
for line in stdin:
    data = line.split()
    data_new[data[0]] = data[2]

DEFAULT_ENCODING = {"encoding": "UTF-8"}
with open(file, "r+", **DEFAULT_ENCODING) as f:
    records = json.load(f)
    for key in data_new:
        records[key] = data_new[key]
    f.seek(0)
    json.dump(records, f, ensure_ascii=False, indent=4)
    f.truncate()
