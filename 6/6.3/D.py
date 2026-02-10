from requests import get, ConnectionError


host_port = input()
key = input()
try:
    res = 0
    response = get(f"http://{host_port}/").json()
    res = response.get(key, "No data")
except ConnectionError:
    print("Проверьте подключение к Сети.")
else:
    print(res)
