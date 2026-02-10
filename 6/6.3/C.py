from requests import get, ConnectionError


host_port = input()
try:
    res = 0
    response = get(f"http://{host_port}/").json()
    res = sum(i for i in response if type(i) == int)
except ConnectionError:
    print("Проверьте подключение к Сети.")
else:
    print(res)
