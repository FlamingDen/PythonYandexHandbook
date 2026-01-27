import json

DEFAULT_ENCODING = {"encoding": "UTF-8"}
file_in = input()
file_out = input()

data = []
with open(file_in, "r", **DEFAULT_ENCODING) as f:
    for line in f:
        data += map(int, line.split())

ln = len(data)
data_sum = sum(data)
min_num = min(data)
max_num = max(data)
positiv_ln = len([1 for num in data if num > 0])
avg = data_sum / (1 if ln == 0 else ln)

res = {
    "count": ln,
    "positive_count": positiv_ln,
    "min": min_num,
    "max": max_num,
    "sum": data_sum,
    "average": round(avg, 2)
}
with open(file_out, "w", **DEFAULT_ENCODING) as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
