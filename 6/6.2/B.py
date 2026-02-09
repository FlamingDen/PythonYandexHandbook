import pandas as pd
import re


def length_stats(text: str):
    indices = sorted(set(re.findall(r"\w+", text.lower())))
    data_res = pd.Series([len(key) for key in indices], index=indices)
    return data_res[data_res % 2 != 0], data_res[data_res % 2 == 0]



odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)