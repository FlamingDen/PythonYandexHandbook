import numpy as np


def multiplication_matrix(n):
    matrix = np.arange(1, n + 1)
    return matrix * matrix.reshape(-1, 1)

print(multiplication_matrix(3))
