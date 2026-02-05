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


print(username_validation("45_user"))
