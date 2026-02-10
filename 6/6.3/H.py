from requests import post, ConnectionError
import json


host_port = input()
new_user = {
    "username": input(),
    "last_name": input(),
    "first_name": input(),
    "email": input(),
}

try:
    post(
        f"http://{host_port}/users",
        data=json.dumps(new_user),
    )
except ConnectionError:
    print("Проверьте подключение к Сети.")
except ValueError:
    print("Пользователь не найден")
