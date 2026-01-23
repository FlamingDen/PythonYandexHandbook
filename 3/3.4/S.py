from itertools import product

condition = input()
vars = [char for char in set(condition) if char.isupper()]
vars.sort()

status = [0, 1]
result = list(product(status, repeat=len(vars)))

print(*vars, "F")
print(
    *[
        f"{' '.join(map(str,vals))} {int(eval(condition, dict(zip(vars, vals))))}"
        for vals in result
    ],
    sep="\n",
)
