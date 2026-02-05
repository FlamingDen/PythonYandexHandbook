class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                z = list(map(int, args[0].split("/")))
                if len(z) == 1:
                    # Fraction("2") -> 2/1
                    self.sign = -1 if z[0] < 0 else 1
                    self.n = abs(z[0])
                    self.d = 1
                else:
                    # Fraction("1/3")
                    self.sign = -1 if z[0] * z[1] < 0 else 1
                    self.n = abs(z[0])
                    self.d = abs(z[1])
            else:
                # Fraction(3) -> 3/1
                self.sign = -1 if args[0] < 0 else 1
                self.n = abs(args[0])
                self.d = 1
        else:
            # Fraction(1, 2)
            self.sign = -1 if args[0] * args[1] < 0 else 1
            self.n = abs(args[0])
            self.d = abs(args[1])
        self.__normalize()

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __lcm(self, a, b):
        return a * b // self.__gcd(a, b)

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

    def __add__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(
            self.sign * self.n * other.d + other.sign * other.n * self.d,
            self.d * other.d,
        )

    def __iadd__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        n = self.sign * self.n * other.d + other.sign * other.n * self.d
        d = self.d * other.d
        self.n = abs(n)
        self.d = abs(d)
        self.sign = -1 if n * d < 0 else 1
        self.__normalize()
        return self

    def __sub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(
            self.sign * self.n * other.d - other.sign * other.n * self.d,
            self.d * other.d,
        )

    def __isub__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        n = self.sign * self.n * other.d - other.sign * other.n * self.d
        d = self.d * other.d
        self.n = abs(n)
        self.d = abs(d)
        self.sign = -1 if n * d < 0 else 1
        self.__normalize()
        return self

    def __mul__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.sign * self.n * other.sign * other.n, self.d * other.d)

    def __imul__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        res = self * other
        self.sign = res.sign
        self.n = res.n
        self.d = res.d
        return self

    def __truediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return Fraction(self.sign * self.n * other.sign * other.d, self.d * other.n)

    def __itruediv__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        res = self / other
        self.sign = res.sign
        self.n = res.n
        self.d = res.d
        return self

    def reverse(self):
        return Fraction(self.sign * self.d, self.n)

    def __lt__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.sign * self.n / self.d < other.sign * other.n / other.d

    def __le__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.sign * self.n / self.d <= other.sign * other.n / other.d

    def __eq__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.sign * self.n / self.d == other.sign * other.n / other.d

    def __ne__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.sign * self.n / self.d != other.sign * other.n / other.d

    def __gt__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.sign * self.n / self.d > other.sign * other.n / other.d

    def __ge__(self, other):
        other = other if isinstance(other, Fraction) else Fraction(other)
        return self.sign * self.n / self.d >= other.sign * other.n / other.d

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Fraction(other) - self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return Fraction(other) / self


a = Fraction(1, 2)
b = Fraction("2/3")
print(3 - a)
print(Fraction.reverse(3 - a))
# c, d = map(Fraction.reverse, (3 - a, 2 / b))
# print(a, b, c, d)
