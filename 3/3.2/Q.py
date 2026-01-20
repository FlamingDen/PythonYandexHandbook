connections = {}

while (s := input()) != "":
    n1, n2 = s.split()
    connections[n1] = connections.get(n1, []) + [n2]
    connections[n2] = connections.get(n2, []) + [n1]


for key, val in sorted(connections.items()):
    first_level = set(val)
    second_level = set()
    for name in first_level:
        second_level |= set(connections[name])
        
    res = second_level - first_level
    res.discard(key)
    str_val = ", ".join(sorted(res))
    print(f"{key}: {str_val}")