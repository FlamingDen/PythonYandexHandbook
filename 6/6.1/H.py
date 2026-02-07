import numpy as np


def snake(m, n, direction="H"):
    matrix = np.arange(1, m * n + 1, dtype="int16")
    if direction == "H":
        matrix = matrix.reshape(n, m)
        matrix[1::2] = matrix[1::2, ::-1]
    elif direction == "V":
        matrix = matrix.reshape(n, m, order="F")
        matrix[:, 1::2] = matrix[::-1, 1::2]
    return matrix

print(snake(3, 5))
