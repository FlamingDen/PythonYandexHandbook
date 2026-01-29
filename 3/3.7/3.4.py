import csv
import datetime
import time
import json

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
    open("test_task_link.csv", "r", **DEFAULT_ENCODING) as file_test_task,
    open("task.csv", "r", **DEFAULT_ENCODING) as file_task,
    open("task_attempt.csv", "r", **DEFAULT_ENCODING) as file_task_attempt,
    open("user.csv", "r", **DEFAULT_ENCODING) as file_user,
):
    result_json = dict()
    tests = []

    # user.json
    reader = csv.reader(file_user)
    next(reader)
    user_data = list(reader)
    curr_user = []
    for user in user_data:
        if user[0] == user_id:
            curr_user = user
            break
    user_json = {
        "user_id": int(user_id),
        "full_name": f"{curr_user[4]} {curr_user[2]}",
        "class_id": int(class_id),
    }
    result_json["user"] = user_json

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
            tests.append([row[0], row[1], dt])  # id связи, id теста и дату выдачи
    tests.sort(key=lambda x: x[2], reverse=True)

    # получили список вопросов(task) и его номер для каждого теста [task_id, order_number]
    reader = csv.reader(file_test_task)
    next(reader)
    test_task_data = list(reader)
    test_tasks = dict()
    for test in tests:
        tasks_for_test = [
            [row[2], row[3]] for row in test_task_data if row[1] == test[1]
        ]
        test_tasks[test[1]] = [test[0], tasks_for_test, test[2]]

    # получаем название теста title
    reader = csv.reader(file_test)
    next(reader)
    test_data = list(reader)
    test_data_dict = {row[0]: row[1] for row in test_data}
    for c_test, c_tasks in test_tasks.items():
        c_tasks.append(test_data_dict[c_test])

    # добавлние результата самого теста(flag_is_finished)
    reader = csv.reader(file_test_attempt)
    next(reader)
    test_attempt_data = list(reader)
    for c_test, c_tasks in test_tasks.items():
        for ans in test_attempt_data:
            if ans[1] == c_tasks[0]:
                c_tasks.append(ans[2])

    # добавили корректные ответы для вопросов
    reader = csv.reader(file_task)
    next(reader)
    task_data = list(reader)
    answers = {row[0]: row[2] for row in task_data}
    for c_test, c_tasks in test_tasks.items():
        for task in c_tasks[1]:
            task.append(answers[task[0]])

    # берем результаты решения теста
    reader = csv.reader(file_task_attempt)
    next(reader)
    task_attempt_data = list(reader)
    for c_test, c_tasks in test_tasks.items():
        for task in c_tasks[1]:
            for row in task_attempt_data:
                # совпадения полностью id попытки и теста
                if row[1] == task[0] and row[2] == c_tasks[0]:
                    task.append(row[3])
                    task.append(row[5])
                    break
            else:
                task.append("")
                task.append("")

    # заполняем json для ответа
    progress_json = {
        "tests_completed": sum(
            1 for key, row in test_tasks.items() if row[4] == "TRUE"
        ),
        "tests_total": int(len(test_tasks)),
    }
    sum_correct_percent = 0
    test_count = 0
    tests_json = list()
    for c_id_test, c_test_data in test_tasks.items():
        currect_data_test = dict()
        tasks_data_for_json = []

        count_of_tasks = len(c_test_data[1])
        passed = 0
        accepted = 0
        result_time = 0

        currect_data_test["test_id"] = int(c_id_test)
        currect_data_test["title"] = c_test_data[3]

        # sorted_tasks = sorted(c_test_data[1], key=lambda x: x[1])
        for task in c_test_data[1]:
            curr = "?" if task[3] == "" else ("TRUE" if task[2] == task[3] else "FALSE")
            if curr != "?":
                if curr == "TRUE":
                    accepted += 1
                passed += 1
            result_time += int(task[4]) if task[4] != "" else 0
            curr_task_data = {
                "order_number": int(task[1]),
                "task_id": int(task[0]),
                "is_correct": curr,
            }
            tasks_data_for_json.append(curr_task_data)

        currect_data_test["tasks"] = tasks_data_for_json
        currect_data_test["progress_percent"] = round(passed / count_of_tasks * 100 if passed > 0 else 0.0, 1)

        correct_percent = accepted / passed * 100 if passed != 0 else 0.0
        if passed > 0:
            sum_correct_percent += correct_percent
            test_count += 1
            
        currect_data_test["correct_percent"] = round(correct_percent, 1)
        currect_data_test["time"] = time.strftime("%H:%M:%S", time.gmtime(result_time))
        currect_data_test["date_assigned"] = c_test_data[2].strftime("%d.%m.%y")
        
        tests_json.append(currect_data_test)

    progress_json["accuracy_average_percent"] = round(
        (
            sum_correct_percent / test_count
            if test_count > 0
            else 0
        ),
        1,
    )

    result = {"user": user_json, "progress": progress_json, "tests": tests_json}
    print(json.dumps(result, ensure_ascii=False, indent=2))
