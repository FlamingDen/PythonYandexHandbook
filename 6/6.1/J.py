import numpy as np


def stairs(vec):
    n = len(vec)
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        matrix[i] = np.roll(vec, i)
    return matrix