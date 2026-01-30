def make_matrix(size, value: int = 0) -> list:
    if isinstance(size, int):
        return [[value for _ in range(size)] for _ in range(size)]
    return [[value for _ in range(size[0])] for _ in range(size[1])]


print(make_matrix((4, 2), 1), sep="\n")
