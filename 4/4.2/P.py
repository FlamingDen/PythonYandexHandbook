def login(login: str, password: str, callbackS, callbackF):
    val = sum(ord(char) for char in login) * len(login)
    str_num16 = f"{val:x}"
    if str_num16.lower() == password[::-1].lower():
        callbackS(login)
    else:
        callbackF(login)


def on_login(username):
    print(f"Hello, {username}!")


def on_fail(username):
    print(f"Nice try... You are not {username}!")


login("NoobMaster", "4C72", on_login, on_fail)
