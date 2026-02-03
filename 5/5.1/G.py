class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1, p2):
        norm_points = self.normalize(self._ensure_point(p1), self._ensure_point(p2))
        self.p1 = norm_points[0]
        self.p2 = norm_points[1]

    def _ensure_point(self, obj):
        if isinstance(obj, tuple):
            return Point(*obj)
        elif isinstance(obj, Point):
            return obj
        else:
            raise TypeError("Ожидается Point или кортеж (x, y)")

    def normalize(self, pt1: Point, pt2: Point):
        norm_pt1 = Point(min(pt1.x, pt2.x), max(pt1.y, pt2.y))
        norm_pt2 = Point(max(pt1.x, pt2.x), min(pt1.y, pt2.y))
        return (norm_pt1, norm_pt2)

    def perimeter(self):
        return round(abs(self.p1.x - self.p2.x) * 2 + abs(self.p1.y - self.p2.y) * 2, 2)

    def area(self):
        return round(abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y), 2)

    def get_pos(self):
        return (round(self.p1.x, 2), round(self.p1.y, 2))

    def get_size(self):
        return (
            round(abs(self.p1.x - self.p2.x), 2),
            round(abs(self.p1.y - self.p2.y), 2),
        )

    def move(self, dx, dy):
        self.p1.x += dx
        self.p1.y += dy
        self.p2.x += dx
        self.p2.y += dy

    def resize(self, width, height):
        self.p2.x = self.p1.x + width
        self.p2.y = self.p1.y - height

    def get_center(self):
        return ((self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2)

    def set_points(self, center, size):
        self.p1.x = center[0] - size[0] / 2
        self.p1.y = center[1] + size[1] / 2

        self.p2.x = center[0] + size[0] / 2
        self.p2.y = center[1] - size[1] / 2

    def turn(self):
        center = self.get_center()
        size_x, size_y = self.get_size()
        size_x, size_y = size_y, size_x
        self.set_points(center, (size_x, size_y))

    def scale(self, factor):
        center = self.get_center()
        size_x, size_y = self.get_size()
        size_x, size_y = round(size_x * factor, 2), round(size_y * factor, 2)
        self.set_points(center, (size_x, size_y))


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep="\n")
rect.scale(0.5)
rect.turn()
rect.scale(2)
rect.turn()
print(rect.get_pos(), rect.get_size(), sep="\n")
