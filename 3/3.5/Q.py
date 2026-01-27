DEFAULT_ENCODING = {"encoding": "UTF-8"}

ans = []
text = []
file_name = "secret.txt"
with open(file_name, "r", **DEFAULT_ENCODING) as file:
    text += [line.rstrip() for line in file]

for line in text:
    decode_line = []
    for char in line:
        if ord(char) >= 128:
            # num = str(bin(ord(char)))
            # decode_line.append(chr(int(num[-8:], 2)))
            low_bits = ord(char) % 256
            decode_line.append(chr(low_bits))
        else:
            decode_line.append(char)

    ans.append("".join(decode_line))

print(*ans, sep="\n")
