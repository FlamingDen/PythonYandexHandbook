import pandas as pd
import re


def length_stats(text: str):
    indices = sorted(set(re.findall(r"\w+", text.lower())))
    return pd.Series([len(key) for key in indices], index=indices)



