from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def length(self, other: Point) -> float:
        return round(
            (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2) ** 0.5, 2
        )


point = Point(3, 5)
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
