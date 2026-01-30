def get_operator(type: str):
    match type:
        case "+":
            return lambda x, y: x + y
        case "-":
            return lambda x, y: x - y
        case "*":
            return lambda x, y: x * y
        case "//":
            return lambda x, y: x // y
        case "**":
            return lambda x, y: x**y
        case __:
            return lambda x, y: None

print(get_operator("+")(3, 4))