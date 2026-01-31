def get_repeater(func, count: int):
    def rep(x):
        res = x
        for _ in range(count):
            res = func(res)
        return res

    return rep


repeater = get_repeater(lambda x: x + 1, 5)
print(repeater(2))
