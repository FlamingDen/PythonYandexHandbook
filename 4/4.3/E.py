def result_accumulator(func):
    results = []

    def wrapper(*args, method="accumulate", **kwargs):
        result = func(*args, **kwargs)
        results.append(result)

        if method == "drop":
            copy_results = results.copy()
            results.clear()
            return copy_results
        else:
            return None

    return wrapper


@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
