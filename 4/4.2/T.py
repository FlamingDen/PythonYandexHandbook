from datetime import datetime

DB = []


def insert(*user) -> None:
    DB.extend(user)


def select(*conditions):
    if not conditions:
        return sorted(DB, key=lambda x: x["id"])

    result = DB[:]
    for condition in conditions:
        col_name, operator, val = condition.split()
        filtered_result = []
        for user in result:
            curr_val = user[col_name]
            match curr_val:
                case int():
                    first = curr_val
                    second = int(val)
                case str():
                    if len(curr_val.split(".")) == 3:
                        first = datetime.strptime(curr_val, "%d.%m.%Y")
                        second = datetime.strptime(val, "%d.%m.%Y")
                    else:
                        first = curr_val
                        second = val

            match operator:
                case ">":
                    if first > second:
                        filtered_result.append(user)
                case "<":
                    if first < second:
                        filtered_result.append(user)
                case "==":
                    if first == second:
                        filtered_result.append(user)
                case ">=":
                    if first >= second:
                        filtered_result.append(user)
                case "<=":
                    if first <= second:
                        filtered_result.append(user)
                case "!=":
                    if first != second:
                        filtered_result.append(user)
        result = filtered_result

    result.sort(key=lambda x: x["id"])
    return result


insert({"id": 1, "name": "Ann", "birth": "01.03.2001"})
insert(
    {"id": 3, "name": "Bob", "birth": "05.03.2002"},
    {"id": 4, "name": "Chuck", "birth": "07.06.2001"},
)
print(select())
print([user["name"] for user in select()])
print([user["name"] for user in select("name > B")])
insert({"id": 2, "name": "Den", "birth": "29.02.2000"})
print([user["name"] for user in select("name > B")])
print([user["name"] for user in select("id <= 2")])
print(*select("birth >= 12.04.2001"), sep="\n")
