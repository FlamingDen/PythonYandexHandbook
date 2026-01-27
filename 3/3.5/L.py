DEFAULT_ENCODING = {"encoding": "UTF-8"}
file_in = input()
file_even = input()  # четное
file_odd = input()  # нечетное
file_eq = input()

with (
    open(file_in, "r", **DEFAULT_ENCODING) as f,
    open(file_even, "w+", **DEFAULT_ENCODING) as even_out,
    open(file_odd, "w+", **DEFAULT_ENCODING) as odd_out,
    open(file_eq, "w+", **DEFAULT_ENCODING) as equal_out,
):
    for line in f:
        curr = line.split()
        data = {}

        for num in curr:
            odd = even = 0
            for char in num:
                if int(char) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            if even > odd:
                data["even"] = data.get("even", []) + [num]
            elif even < odd:
                data["odd"] = data.get("odd", []) + [num]
            else:
                data["eq"] = data.get("eq", []) + [num]

        even_out.write(f"{' '.join(data.get('even', []))}\n")
        odd_out.write(f"{' '.join(data.get('odd', []))}\n")
        equal_out.write(f"{' '.join(data.get('eq', []))}\n")
