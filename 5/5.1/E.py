class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = self._ensure_point(p1)
        self.p2 = self._ensure_point(p2)

    def _ensure_point(self, obj):
        """Преобразовать кортеж в Point или вернуть Point."""
        if isinstance(obj, tuple):
            return Point(*obj)
        elif isinstance(obj, Point):
            return obj
        else:
            raise TypeError("Ожидается Point или кортеж (x, y)")

    def perimeter(self):
        return round(abs(self.p1.x - self.p2.x) * 2 + abs(self.p1.y - self.p2.y) * 2, 2)

    def area(self):
        return round(abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y), 2)


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())
