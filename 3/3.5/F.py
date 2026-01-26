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
    "Ъ": "",
}

input_txt = "cyrillic.txt"
output_txt = "transliteration.txt"

ans = []
with open(input_txt, "r", encoding="UTF-8") as in_file:
    for line in in_file:

        curr_line = ""
        for letter in line.rstrip("\n"):
            code = ord(letter.upper())
            if letter == " " or (65 <= code <= 90) or (not letter.isalpha()):
                curr_line += letter
            else:
                low = letter.islower()
                tmp_let = translater[letter.upper()]
                curr_line += tmp_let if not low else tmp_let.lower()
        ans.append(curr_line)

with open(output_txt, "w", encoding="UTF-8") as out_file:
    print(*(line for line in ans), sep="\n", file=out_file)
