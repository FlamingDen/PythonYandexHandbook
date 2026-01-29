def is_mountain(data, point):
    row, col = point
    current_value = data[row][col]

    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),  # Верхние соседи
        (0, -1),
        (0, 1),  # Боковые соседи
        (1, -1),
        (1, 0),
        (1, 1),  # Нижние соседи
    ]

    for dr, dc in directions:
        neighbor_row = row + dr
        neighbor_col = col + dc
        neighbor_value = data[neighbor_row][neighbor_col]

        if neighbor_value >= current_value:
            return False

    return True


def find_mountains(data):
    res = []
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            if is_mountain(data, (i, j)):
                res.append((i + 1, j + 1))
    return tuple(res)


result = find_mountains(
    [
        [1, 1, 1, 1, 1, 1],
        [1, 2, 1, 5, 4, 1],
        [1, 1, 1, 3, 4, 3],
        [2, 3, 3, 1, 2, 3],
        [1, 2, 1, 3, 2, 1],
    ]
)
print(result)
