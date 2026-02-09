import pandas as pd


def cut(data: pd.DataFrame, upl, btr) -> pd.DataFrame:
    x1, y1 = upl[0], upl[1]
    x2, y2 = btr[0], btr[1]
    mask = (data["x"] >= x1) & (data["x"] <= x2) & (data["y"] <= y1) & (data["y"] >= y2)
    return data[mask]


data = pd.read_csv("data.csv")
up_l = list(map(int, input().split()))
bottom_r = list(map(int, input().split()))
print(cut(data, up_l, bottom_r))
