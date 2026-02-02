def make_linear(data: list):
    result = []
    for el in data:
        if isinstance(el, list):
            result.extend(make_linear(el))
        else:
            result.append(el)

    return result

result = make_linear([1, [2, [3, 4]], 5, 6])
print(result)