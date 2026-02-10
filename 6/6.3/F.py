from requests import get, ConnectionError


host_port = input()
try:
    response = get(f"http://{host_port}/users").json()
    users = [f"{user['last_name']} {user['first_name']}" for user in response]
    users.sort()
except ConnectionError:
    print("Проверьте подключение к Сети.")
else:
    print(*users, sep="\n")
