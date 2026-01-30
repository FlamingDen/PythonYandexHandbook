def get_formatter(sep: str = " ", end: str = ""):
    return lambda *args: sep.join(str(arg) for arg in args) + end


formatter = get_formatter(end="!", sep=", ")
print(formatter("Hello", "world"))
