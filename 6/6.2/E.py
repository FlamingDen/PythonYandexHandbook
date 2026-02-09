import pandas as pd
import re


def length_stats(text: str):
    indices = sorted(set(re.findall(r"\w+", text.lower())))
    return pd.Series([len(key) for key in indices], index=indices)


def get_long(data: pd.Series, min_length=5) -> pd.Series:
    return data[data >= min_length]


data = pd.Series([3, 5, 6, 6], ["мир", "питон", "привет", "яндекс"])
filtered = get_long(data, min_length=6)
print(data)
print(filtered)
