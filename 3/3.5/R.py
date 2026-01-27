file_name = input()

DEFAULT_ENCODING = {"encoding": "UTF-8"}
with open(file_name, "r", **DEFAULT_ENCODING) as file:
    file.seek(0, 2)
    size = file.tell() # in bites

UNITS = ("Б", "КБ", "МБ", "ГБ")
unit_index = 0

while size >= 1024 and unit_index < 3:
    size /= 1024
    unit_index += 1

if size > int(size):
    size = (size + 1) // 1

print(f"{size:.0f}{UNITS[unit_index]}")
    