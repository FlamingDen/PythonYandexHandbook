import numpy as np


def rotate(matrix, deg):
    count = (deg % 360) // 90 
    return np.rot90(matrix, -count) 


