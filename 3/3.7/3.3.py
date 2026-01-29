import csv
import datetime
import time

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
):
    tasks = []
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

    # находим тесты(id и дату выдачи) -> сортируем -> берем последний
    reader = csv.reader(file_test_class_user)
    next(reader)
    test_class_user_data = list(reader)
    for row in test_class_user_data:
        if row[2] == class_user_link_id:
            dt = datetime.datetime.strptime(row[3], "%d.%m.%Y %H:%M:%S")
            # dt.strftime("%d.%m.%y")
            result.append([row[0], row[1], dt])  # id связи, id теста и дату выдачи
    result.sort(key=lambda x: x[2], reverse=True)

    last_test = result[0]

    # получили список вопросов(task) для этого теста [task_id, order_number]
    reader = csv.reader(file_test_task)
    next(reader)
    test_task_data = list(reader)
    tasks = [[row[2], row[3]] for row in test_task_data if row[1] == last_test[1]]

    # добавили корректные ответы для вопросов
    reader = csv.reader(file_task)
    next(reader)
    task_data = list(reader)
    answers = {row[0]: row[2] for row in task_data}
    for task in tasks:
        task.append(answers[task[0]])

    # берем результаты решения теста
    reader = csv.reader(file_task_attempt)
    next(reader)
    task_attempt_data = list(reader)
    for task in tasks:
        for row in task_attempt_data:
            # совпадения полностью id попытки и теста
            if row[1] == task[0] and row[2] == last_test[0]:
                task.append(row[3])
                task.append(row[5])
                break
        else:
            task.append("")
            task.append("")

    # Вывод результата
    ln = len(tasks)
    passed = 0
    accepted = 0
    result_time = 0
    result_answer = []
    for task in tasks:
        curr = "?" if task[3] == "" else ("TRUE" if task[2] == task[3] else "FALSE")
        if curr != "?":
            if curr == "TRUE":
                accepted += 1
            passed += 1
        result_time += int(task[4]) if task[4] != "" else 0
        result_answer.append(f"{task[1]} {curr} {task[0]}")

    print(f"{round(passed / ln * 100, 1)}% {round(accepted / passed * 100, 1)}%")
    print(*result_answer, sep="\n")
    print(time.strftime("%H:%M:%S", time.gmtime(result_time)))
