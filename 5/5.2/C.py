class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def length(self, other) -> float:
        return round(
            (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2) ** 0.5, 2
        )


class PatchedPoint(Point):
    def __init__(self, *coord):
        size = len(coord)
        if size == 0:
            super().__init__(0, 0)
        if size == 1:
            super().__init__(coord[0][0], coord[0][1])
        if size == 2:
            super().__init__(coord[0], coord[1])

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, pair: tuple):
        return PatchedPoint(self.x + pair[0], self.y + pair[1])

    def __iadd__(self, pair: tuple):
        self.move(pair[0], pair[1])
        return self


point = PatchedPoint()
# print(point)
# new_point = point + (2, -3)
# print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
