from requests import delete, ConnectionError

host_port = input()
user_id = input()

try:
    delete(f"http://{host_port}/users/{user_id}")
except ConnectionError:
    print("Проверьте подключение к Сети.")
except ValueError:
    print("Пользователь не найден")
