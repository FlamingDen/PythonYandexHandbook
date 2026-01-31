mp = lambda x: (
    "".join(char for char in x[0].lower() if char.isalpha()),
    (
        sum(x[1])
        if hasattr(x[1], "__iter__") and not isinstance(x[1], (str, bytes))
        else x[1]
    )
)

print(dict(map(mp, {"First 1": 2, "second:": (2, 1, 1), "THIRD": [1, 2, 3]}.items())))
