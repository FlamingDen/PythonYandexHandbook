def cycle(data: list):
    while True:
        for curr in data:
            yield curr


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
