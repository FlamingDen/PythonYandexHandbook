def roman(a, b):
    roman_pairs = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def to_roman(num):
        result = ""
        for value, symbol in roman_pairs:
            while num >= value:
                result += symbol
                num -= value
        return result

    roman_a = to_roman(a)
    roman_b = to_roman(b)
    roman_sum = to_roman(a + b)

    return f"{roman_a} + {roman_b} = {roman_sum}"


print(roman(10, 9))
