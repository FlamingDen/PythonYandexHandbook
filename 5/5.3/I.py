class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError

    if not all(
        (97 <= ord(char.lower()) <= 122 or char.isdigit() or char == "_")
        for char in username
    ):
        raise BadCharacterError

    if username[0].lower().isdigit():
        raise StartsWithDigitError

    return username


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    if not all(char.lower() in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for char in name):
        raise CyrillicError

    if name != name.lower().capitalize():
        raise CapitalError

    return name


def user_validation(**kwargs):
    if [i for i in kwargs] != ['last_name', 'first_name', 'username'] or len(kwargs) != 3:
        raise KeyError
    if any(not isinstance(k, str) for k in kwargs.values()):
        raise TypeError
    kwargs['last_name'] = name_validation(kwargs['last_name'])
    kwargs['first_name'] = name_validation(kwargs['first_name'])
    kwargs['username'] = username_validation(kwargs['username'])
    return kwargs



