def recursive_sum(arg, *args):
    if not args:
        return arg
    return arg + recursive_sum(*args)


print(recursive_sum(7, 1, 3, 2, 10))
