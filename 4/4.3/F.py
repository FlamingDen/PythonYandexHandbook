def merge(t1: list, t2: list) -> list:
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

    return res


def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return data

    m = len(data) // 2
    left_half = merge_sort(data[:m])
    right_half = merge_sort(data[m:])

    return merge(left_half, right_half)


result = merge_sort([3, 2, 1])
print(result)
