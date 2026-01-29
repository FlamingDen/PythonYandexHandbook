def merge(t1: tuple, t2: tuple) -> tuple:
    res = []
    p1 = p2 = 0
    while p1 < len(t1) or p2 < len(t2):
        if p1 < len(t1) and p2 < len(t2):
            if t1[p1] > t2[p2]:
                res.append(t2[p2])
                p2 += 1
            elif t1[p1] <= t2[p2]:
                res.append(t1[p1])
                p1 += 1
        elif p1 < len(t1):
            res.append(t1[p1])
            p1 += 1
        else:
            res.append(t2[p2])
            p2 += 1

    return tuple(res)


print(merge((7, 12), (1, 9, 50)))
