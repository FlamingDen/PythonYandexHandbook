class Fraction:
    def __init__(self, *args):
        if isinstance(args[0], str):
            tmp_a, tmp_b = map(int, args[0].split("/"))
            self.sign = -1 if tmp_a * tmp_b < 0 else 1
            self.n = abs(tmp_a)
            self.d = abs(tmp_b)
        else:
            self.sign = -1 if args[0] * args[1] < 0 else 1
            self.n = abs(args[0])
            self.d = abs(args[1])
        self.__normalize()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __normalize(self):
        curr_gcd = self.__gcd(self.d, self.n)
        self.n = self.n // curr_gcd
        self.d = self.d // curr_gcd

    def _set_numerator(self, value):
        if value < 0:
            self.sign *= -1
        self.n = abs(value)
        self.__normalize()

    def numerator(self, value=None):
        if value is not None:
            self._set_numerator(value)
        return abs(self.n)

    def _set_denominator(self, value):
        if value < 0:
            self.sign *= -1
        self.d = abs(value)
        self.__normalize()

    def denominator(self, value=None):
        if value is not None:
            self._set_denominator(value)
        return abs(self.d)

    def __str__(self):
        return f"{self.sign * self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction('{self.sign * self.n}/{self.d}')"

    def __neg__(self):
        return Fraction(-self.sign * self.n, self.d)
