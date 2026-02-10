from requests import get, ConnectionError
import sys

host_port, *path = map(str.strip, sys.stdin)
try:
    response = [sum(get(f"http://{host_port}{path_}").json()) for path_ in path]
    res = sum(response)
except ConnectionError:
    print("Проверьте подключение к Сети.")
else:
    print(res)
