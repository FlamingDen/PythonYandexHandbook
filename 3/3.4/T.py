from itertools import product

REPLACEMENTS = {
    "not": " not ",
    "~": " ~ ",
    "and": " and ",
    "or": " or ",
    "^": " ^ ",
    "->": " -> ",
    "(": " ( ",
    ")": " ) ",
}

PRECEDENCE = {
    "not": 6,  # самый высокий (отрицание)
    "^": 5,  # строгая дизъюнкция (XOR)
    "and": 4,  # конъюнкция
    "or": 3,  # дизъюнкция
    "->": 2,  # импликация
    "~": 1,  # эквивалентность (самый низкий)
}

condition = input()
for old_value, new_value in REPLACEMENTS.items():
    condition = condition.replace(old_value, new_value)
vars = [char for char in set(condition) if char.isupper()]
vars.sort()

status = [0, 1]
tupls = list(product(status, repeat=len(vars)))

tokens = condition.split()

print(*vars, "F")
for args in tupls:
    curr_args = dict(zip(vars, args))
    value_stack = []
    operations_stack = []

    for i in range(len(tokens)):
        curr = tokens[i]
        if curr.isupper():
            value_stack.append(curr_args[curr])
        elif curr == "(":
            operations_stack.append(curr)
        elif curr == ")":
            while operations_stack[-1] != "(":
                curr_oper = operations_stack.pop()
                if curr_oper == "not":
                    if not value_stack:
                        quit()
                    value_stack.append(not value_stack.pop())
                else:
                    if len(value_stack) < 2:
                        quit()
                    a = value_stack.pop()
                    b = value_stack.pop()
                    match curr_oper:
                        case "and":
                            value_stack.append(a and b)
                        case "or":
                            value_stack.append(a or b)
                        case "->":
                            value_stack.append(not b or a)
                        case "~":
                            value_stack.append(b == a)
                        case "^":
                            value_stack.append(a ^ b)
            operations_stack.pop()
        elif curr in PRECEDENCE:
            # нажо рассмтореть 3 варинта
            # 1. текущий приоритет выше чем который лежит в стеке сверху(просто кладем)
            # 2. екущий приоритет ниже (выполняем что сейчас на стеке последнюю операцию)
            # 3. равен (тоже выполняем пока не будет скобка или занк с приоритеттом выше)
            # 4. если находим ')' -> выполняем все поочереди пока не найдем открывающую скорбку '('
            top = operations_stack[-1] if operations_stack else None
            if not operations_stack or top == "(" or PRECEDENCE[top] < PRECEDENCE[curr]:
                operations_stack.append(curr)
            else:
                while (
                    operations_stack
                    and PRECEDENCE[operations_stack[-1]] >= PRECEDENCE[curr]
                ):
                    curr_oper = operations_stack.pop()
                    if curr_oper == "not":
                        if not value_stack:
                            quit()
                        value_stack.append(not value_stack.pop())
                    else:
                        if len(value_stack) < 2:
                            quit()
                        a = value_stack.pop()
                        b = value_stack.pop()
                        match curr_oper:
                            case "and":
                                value_stack.append(a and b)
                            case "or":
                                value_stack.append(a or b)
                            case "->":
                                value_stack.append(not b or a)
                            case "~":
                                value_stack.append(b == a)
                            case "^":
                                value_stack.append(a ^ b)
                operations_stack.append(curr)

    while operations_stack:
        curr_oper = operations_stack.pop()
        if curr_oper == "not":
            if not value_stack:
                break
            value_stack.append(not value_stack.pop())
        else:
            if len(value_stack) < 2:
                break
            a = value_stack.pop()
            b = value_stack.pop()
            match curr_oper:
                case "and":
                    value_stack.append(a and b)
                case "or":
                    value_stack.append(a or b)
                case "->":
                    value_stack.append(not b or a)
                case "~":
                    value_stack.append(a == b)
                case "^":
                    value_stack.append(a ^ b)

    print(*args, int(value_stack.pop()))
