def get_dict(text):
    res = dict()

    items = text.split(";")
    for pair in items:
        key, val = pair.split("=")
        if val.isdigit():
            res[key] = int(val)
            continue

        val_list = val.split(".")
        if len(val_list) == 2 and val_list[0].isdigit() and val_list[1].isdigit():
            res[key] = float(val)
        else:
            res[key] = val
    return res


print(get_dict("id=3-76;ip=127.0.0.1;phone=+7-(123)-456-78-90"))
