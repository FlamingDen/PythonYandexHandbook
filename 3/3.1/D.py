while (s := input()) != "":
    if s.endswith("@@@"):
        continue
    elif s.startswith("##"):
        print(s[2:])
    else:
        print(s)