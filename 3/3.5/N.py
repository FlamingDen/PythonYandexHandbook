import json

file_users = input()
file_upd = input()

DEFAULT_ENCODING = {"encoding": "UTF-8"}
with (
    open(file_users, "r+", **DEFAULT_ENCODING) as f_users,
    open(file_upd, "r", **DEFAULT_ENCODING) as f_upd,
):
    users = json.load(f_users)
    upd = json.load(f_upd)

    data = {}
    for user in users:
        data[user["name"]] = {key: user[key] for key in user if key != "name"}

    for user in upd:
        for key in user:
            if key == "name":
                continue
            if key not in data[user["name"]] or user[key] > data[user["name"]][key]:
                data[user["name"]][key] = user[key]

    f_users.seek(0)
    json.dump(data, f_users, ensure_ascii=False, indent=4)
    f_users.truncate()
