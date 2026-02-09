import pandas as pd


def update(data: pd.DataFrame) -> pd.DataFrame:
    j = data.copy()
    columns = ["maths", "physics", "computer science"]
    j["average"] = j[columns].sum(axis=1) / len(columns)
    return j.sort_values(by=["average", "name"], ascending=(False, True))


