import pandas as pd
import numpy as np


def values(func, start, end, step):
    ind = np.arange(start, end + step, step)
    return pd.Series(map(func, ind), index=ind, dtype="float64")


def min_extremum(data: pd.Series):
    return data.idxmin()


def max_extremum(data: pd.Series):
    return data.idxmax()


data = values(lambda x: x**2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
