public_file = "public.txt"
private_file = "private.txt"

ALPHA_END = ord("z")
LENGTH = 26

n = int(input())
n %= LENGTH

DEFAULT_ENCODING = {"encoding": "UTF-8"}
with (
    open(public_file, "r", **DEFAULT_ENCODING) as file_in,
    open(private_file, "w", **DEFAULT_ENCODING) as file_out,
):
    for line in file_in:
        encode = []
        for char in line:
            if char.isalpha():
                code_point = ord(char.lower()) + n

                if code_point > ALPHA_END:
                    code_point -= LENGTH

                new_char = chr(code_point)

                encode.append(new_char if char.islower() else new_char.upper())
            else:
                encode.append(char)

        file_out.write("".join(encode))
