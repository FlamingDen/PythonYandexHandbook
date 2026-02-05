class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError

    if not all(char.lower() in 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя' for char in name):
        raise CyrillicError

    if name != name.lower().capitalize():
        raise CapitalError

    return name

print(name_validation("user"))
print(name_validation("иванов"))
