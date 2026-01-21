words = "My homework is too difficult!"
print(
    [
        word
        for word in words.split()
        if sum(
            [
                1
                for letter in word.lower()
                if letter in "аяуюоёэеиы" or letter in "aeiouy"
            ]
        )
        >= 3
    ]
)

# Подсчет кол-во гласных в слове
# s = "Ехали"
# print(sum([1 for letter in s if letter.lower() in "аяуюоёэеиы" or letter in "aeiouy"]))
