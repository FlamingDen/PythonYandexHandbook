translater = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "Ь": "",
    "Ъ": ""
}

s = input()
res = ""
for letter in s:    
    code = ord(letter.upper())
    if letter == " " or (65 <= code <= 90) or (not letter.isalpha()):
        res += letter
    else:
        low = letter.islower()
        tmp_let = translater[letter.upper()]
        res += tmp_let if not low else tmp_let.lower()
    
print(res)
