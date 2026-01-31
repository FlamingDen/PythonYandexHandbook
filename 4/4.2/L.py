__results = [0, 0, 0]


def get_sum():
    return tuple(__results[:-1])


def get_average():
    if __results[2] != 0:
        return (__results[0] / __results[2], __results[1] / __results[2])
    return (0.0, 0.0)


def enter_results(*args):
    global __results
    for i in range(0, len(args) - 1, 2):
        __results[0] += args[i]
        __results[1] += args[i + 1]
        __results[2] += 1


# enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())
