def secret_replace(text: str, **args):
    counts = {key: 0 for key in args.keys()}
    res = []
    for char in text:
        if char in counts:
            res.append(args[char][counts[char]])
            counts[char] = (counts[char] + 1) % len(args[char])
        else:
            res.append(char)
    return "".join(res)


result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)
