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

