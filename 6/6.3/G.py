from requests import get, ConnectionError
import sys


host_port = input()
user_id = input()
text = "".join(line for line in sys.stdin)
try:
    data = get(f"http://{host_port}/users/{user_id}").json()
except ConnectionError:
    print("Проверьте подключение к Сети.")
except ValueError:
    print('Пользователь не найден')

if data:
    email_ = data["email"]
    last_name_ = data["last_name"]
    first_name_ = data["first_name"]
    text = text.format(**data)
    print(text)
