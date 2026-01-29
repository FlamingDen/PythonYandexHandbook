def add_num(list, str_num):
    list.append(int("".join(str_num)))


def split_numbers(text):
    result = []
    curr_num = []

    for char in text:
        if char == " ":
            add_num(result, curr_num)
            curr_num = []
        else:
            curr_num.append(char)

    if curr_num:
        add_num(result, curr_num)

    return tuple(result)


print(split_numbers("1 -2 3 -4 5"))
