file_in = "sample01.num"

bytes = 2
nums_sum = 0
with open(file_in, "rb") as file:
    while chunk := file.read(bytes):
        nums_sum += int.from_bytes(chunk, byteorder="big")

nums_sum %= 256**bytes
print(nums_sum)
