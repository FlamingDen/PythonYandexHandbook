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

lengths = []

DEFAULT_ENCODING = {"encoding": "UTF-8"}
for file_name in csv_files:
    with open(file_name, "r", **DEFAULT_ENCODING) as file_in:
        lengths.append(sum(1 for _ in file_in) - 1)

print(*lengths)
