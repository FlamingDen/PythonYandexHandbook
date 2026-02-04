class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            self._numerator, self._denominator = map(int, args[0].split("/"))
        if len(args) == 2:
            self._numerator = args[0]
            self._denominator = args[1]
        self._normalize()

    def _gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a %= b
            a, b = b, a
        return a

    def _normalize(self):
        curr_gcd = self._gcd(self._denominator, self._numerator)
        self._numerator = int(self._numerator / curr_gcd)
        self._denominator = int(self._denominator / curr_gcd)

    def _set_numerator(self, value):
        self._numerator = value
        self._normalize()

    def numerator(self, value=None):
        if value is None:
            return self._numerator
        self._set_numerator(value)

    def _set_denominator(self, value):
        self._denominator = value
        self._normalize()

    def denominator(self, value=None):
        if value is None:
            return self._denominator
        self._set_denominator(value)

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"


fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())
