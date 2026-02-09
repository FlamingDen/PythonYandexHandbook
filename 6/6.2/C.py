import pandas as pd


def cheque(*args, **kwargs):
    series = args[0]
    data = dict()
    data["product"] = [*series.index]
    data["price"] = series.values
    data["number"] = [0 for _ in range(len(series))]
    data["cost"] = [0 for _ in range(len(series))]
    for key, val in kwargs.items():
        ind = data["product"].index(key)
        data["number"][ind] = val
        data["cost"][ind] = val * data["price"][ind]
    res = pd.DataFrame(data=data)
    res = res[res["number"] >= 1]
    return res.sort_values(by="product").reset_index(drop=True)


products = ["bread", "milk", "soda", "cream"]
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, index=products)
print(price_list)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
