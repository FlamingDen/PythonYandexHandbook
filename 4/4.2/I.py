def product(*args, **val):
    result = []
    for arg in args:
        chars = set(arg)
        curr_ans = 1
        has_ans = False
        for char in chars:
            if char in val:
                curr_ans *= val[char]
                has_ans = True

        if has_ans:
            result.append(curr_ans)

    return tuple(result)


print(product("Ann", "Bob", "Chuck", a=9, n=5, u=3, c=2, A=5))
