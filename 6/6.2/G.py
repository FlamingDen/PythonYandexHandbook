import pandas as pd


def best(data: pd.DataFrame) -> pd.DataFrame:
    columns = ["maths", "physics", "computer science"]
    return data.loc[(data[columns] > 3).all(axis=1)]


def need_to_work_better(data: pd.DataFrame) -> pd.DataFrame:
    columns = ["maths", "physics", "computer science"]
    return data.loc[(data[columns] == 2).any(axis=1)]


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)
