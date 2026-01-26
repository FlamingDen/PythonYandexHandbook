first = input()
second = input()
out_file = input()
DEFAULT_ENCODING = {"encoding": "UTF-8"}

first_set = set()
second_set = set()

with open(first, "r", **DEFAULT_ENCODING) as f:
    first_set |= set(f.read().split())

with open(second, "r", **DEFAULT_ENCODING) as f:
    second_set |= set(f.read().split()) 

with open(out_file, "w", **DEFAULT_ENCODING) as f:
    print(*(sorted(list(first_set ^ second_set))), sep="\n", file=f)       
