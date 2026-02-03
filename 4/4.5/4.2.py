import sys
from functools import wraps
from json import dumps


# ЭТИ ДЕКОРАТОРЫ НУЖНО НАПИСАТЬ
def require_auth(func):

    @wraps(func)
    def wrapper(args):
        if "name" not in args:
            return 403, "Forbidden"
        return func(args)

    return wrapper


def log_call(func):

    @wraps(func)
    def wrapper(args):
        func_name = func.__name__
        response = func(args)
        log = {"handler": func_name, "params": args, "response": [*response]}
        print(dumps(log))

    return wrapper


# Handler'ы для разных маршрутов
@log_call
def home_handler(params):
    return 200, "Home Page"


@log_call
def admin_handler(params):
    return 200, "Admin Panel"


@log_call
@require_auth
def user_handler(params):
    # Должен использовать параметр name из URL
    return 200, f"Hello, {params['name']}!"


@log_call
@require_auth
def attempt_handler(params):
    # Должен использовать параметр name из URL
    return (
        200,
        f"Good try, {params['name']}! Your attempt on task '{params['task']}' is accepted!",
    )


@log_call
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
    else:
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
    app.send(request)
