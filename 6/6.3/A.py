from requests import get, ConnectionError


try:
    response = get("http://127.0.0.1:5000/")
except ConnectionError:
    print("Проверьте подключение к Сети.")
else:
    print(response.content.decode("utf-8"))
