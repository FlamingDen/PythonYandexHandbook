while (s := input()) != "":
    it = s.find("#")
    if it != -1:
        s = s[:it]
    if it != 0:   
        print(s)