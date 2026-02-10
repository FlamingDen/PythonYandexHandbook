from requests import get, ConnectionError


host_port = input()
try:
    res = 0
    while response := int(get(f"http://{host_port}/").text):
        res += response
except ConnectionError:
    print("Проверьте подключение к Сети.")
else:
    print(res)
