def answer(func):

    def decorated(*args, **kwargs):
        return f"Результат функции: {func(*args, **kwargs)}"

    return decorated


@answer
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5))
print(a_plus_b(7, 9))
