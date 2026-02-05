from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    password,
    min_length=8,
    possible_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    at_least_one=str.isdigit,
):
    if not isinstance(password, str):
        raise TypeError

    if len(password) < min_length:
        raise MinLengthError

    if any(char not in possible_chars for char in password):
        raise PossibleCharError

    if not any(map(at_least_one, password)):
        raise NeedCharError

    return sha256(password.encode()).hexdigest()


print(password_validation("Hello12345"))