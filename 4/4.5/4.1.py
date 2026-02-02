import sys


# Handler'ы для разных маршрутов
def home_handler(params):
    return 200, "Home Page"


def admin_handler(params):
    return 200, "Admin Panel"


def user_handler(params):
    # Должен использовать параметр name из URL
    return 200, f"Hello, {params['name']}!"


def attempt_handler(params):
    # Должен использовать параметр name из URL
    return (
        200,
        f"Good try, {params['name']}! Your attempt on task '{params['task']}' is accepted!",
    )


def not_found_handler(params):
    return 404, "Not Found"


# Функция маршрутизации
def router(path):
    if path == "/":
        return home_handler
    elif path.startswith("/user"):
        return user_handler
    elif path.startswith("/attempt"):
        return attempt_handler
    elif path.startswith("/admin"):
        return admin_handler

    return not_found_handler


def wsgi_server():
    """Обрабатывает запросы и возвращает каждый из ответов через yield"""
    request = yield None
    while True:
        clean_req = request.strip().split(" ")[1]
        curr_handler = router(clean_req)
        params = dict()
        args = clean_req.split("?")
        if len(args) > 1:
            for pair in args[1].split("&"):
                key, val = pair.split("=")
                params[key] = val

        response = curr_handler(params)
        request = yield response


# Имитация работы сервера
app = wsgi_server()
app.send(None)

for request in sys.stdin:
    print(app.send(request))
