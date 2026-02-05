def only_positive_even_sum(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError
    if not all(x > 0 and x % 2 == 0 for x in (a, b)):
        raise ValueError
    return a + b

