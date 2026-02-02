def make_equation(*args):
    if len(args) == 1:
        return args[0]
    curr_str = f"({args[0]}) * x + {args[1]}"
    return make_equation(curr_str, *args[2:]) 

result = make_equation(3, 1, 5, 3)
print(result)