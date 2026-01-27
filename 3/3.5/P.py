from sys import stdin

req = input().lower()
files = [file.rstrip("\n") for file in stdin]

DEFAULT_ENCODING = {"encoding": "UTF-8"}

ans = []
for file_name in files:
    with open(file_name, "r", **DEFAULT_ENCODING) as file:
        clean_list = []

        while s := file.readline():
            line = " ".join(s.replace("&nbsp;", " ").split())
            if line:
                clean_list.append(line)

        text = " ".join(clean_list).lower()

        if req in text:
            ans.append(file_name)

if ans:
    print(*ans, sep="\n")
else:
    print("404. Not Found")
