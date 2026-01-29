def is_palindrome(x):
    match x:
        case int():
            x_str = str(abs(x))
            return x_str == x_str[::-1]
        case str():
            return x == x[::-1]
        case list() | tuple():
            return list(x) == list(reversed(x))
        case _:
            return False


print(is_palindrome([1, 1, 1]))
