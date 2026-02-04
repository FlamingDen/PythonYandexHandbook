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
