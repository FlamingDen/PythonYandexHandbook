import csv
import datetime

csv_files = [
    "user.csv",
    "class.csv",
    "class_user_link.csv",
    "task.csv",
    "test.csv",
    "test_task_link.csv",
    "test_class_user_link.csv",
    "test_attempt.csv",
    "task_attempt.csv",
]

user_id, class_id = input().split()

DEFAULT_ENCODING = {"encoding": "UTF-8"}
with (
    open("class_user_link.csv", "r", **DEFAULT_ENCODING) as file_class_user,
    open("test_class_user_link.csv", "r", **DEFAULT_ENCODING) as file_test_class_user,
    open("test.csv", "r", **DEFAULT_ENCODING) as file_test,
    open("test_attempt.csv", "r", **DEFAULT_ENCODING) as file_test_attempt,
):
    result = []

    # находим что это за учених (id точный)
    reader = csv.reader(file_class_user)
    next(reader)
    class_user_link_data = list(reader)
    class_user_link_id = -1
    for row in class_user_link_data:
        if row[1] == class_id and row[2] == user_id:
            class_user_link_id = row[0]
            break

    # находим тесты(id и дату выдачи)
    reader = csv.reader(file_test_class_user)
    next(reader)
    test_class_user_data = list(reader)
    for row in test_class_user_data:
        if row[2] == class_user_link_id:
            dt = datetime.datetime.strptime(row[3], "%d.%m.%Y %H:%M:%S")
            # dt.strftime("%d.%m.%y")
            result.append([row[0], row[1], dt])  # id связи, id теста и дату выдачи
    result.sort(key=lambda x: x[2], reverse=True)

    # заменили id -> на titile в result
    reader = csv.reader(file_test)
    next(reader)
    test_data = list(reader)
    test_data_dict = {row[0]: row[1] for row in test_data}
    for row in result:
        row[1] = test_data_dict[row[1]]

    # добавлние результата
    reader = csv.reader(file_test_attempt)
    next(reader)
    test_attempt_data = list(reader)
    for row in result:
        for ans in test_attempt_data:
            if ans[1] == row[0]:
                row.append(ans[2])

    print(f"{sum(1 for row in result if row[3] == 'TRUE')}/{len(result)}")
    print(
        *[f"{row[1]} {row[2].strftime('%d.%m.%y')} {row[3]}" for row in result],
        sep="\n",
    )
