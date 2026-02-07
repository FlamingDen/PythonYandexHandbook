import numpy as np


def make_board(n):
    mt = np.indices((n, n)).sum(axis=0) % 2
    return np.array(np.rot90(mt), dtype="int8")

print(make_board(4))
