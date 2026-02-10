from requests import put, ConnectionError
import json
from sys import stdin

host_port = input()
user_id = input()
new_user = dict()
for line in stdin:
    key, val = line.strip().split("=")
    new_user[key] = val

try:
    put(
        f"http://{host_port}/users/{user_id}",
        data=json.dumps(new_user),
    )
except ConnectionError:
    print("Проверьте подключение к Сети.")
except ValueError:
    print("Пользователь не найден")
