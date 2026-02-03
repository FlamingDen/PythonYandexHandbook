#  ABCDEFGH
# 1
# 2
# .
class Checkers:

    def __init__(self):
        self.__row = 8
        self.__col = 8
        self.board = [[Cell(col + row) for col in "ABCDEFGH"] for row in "87654321"]

        # black
        for i in range(3):
            for j in range((i + 1) % 2, len(self.board[i]), 2):
                self.board[i][j].set_val(2)

        # White
        st = len(self.board) - 1
        end = st - 3
        for i in range(st, end, -1):
            for j in range((i + 1) % 2, len(self.board[i]), 2):
                self.board[i][j].set_val(1)

    def get_cell(self, position: str):
        return self.board[len(self.board) - int(position[1])][ord(position[0]) - 65]

    def get_index(self, position: str):
        return (len(self.board) - int(position[1]), ord(position[0]) - 65)

    def move(self, old_pos, new_pos):
        old_ind = self.get_index(old_pos)
        new_ind = self.get_index(new_pos)
        self.board[old_ind[0]][old_ind[1]], self.board[new_ind[0]][new_ind[1]] = (
            self.board[new_ind[0]][new_ind[1]],
            self.board[old_ind[0]][old_ind[1]],
        )


class Cell:

    _values = ["X", "W", "B"]

    def __init__(self, coord, value=0):
        self.coord = coord
        self.value = self._values[value]

    def status(self):
        return self.value

    def set_val(self, val):
        self.value = self._values[val]


checkers = Checkers()
checkers.move("C3", "D4")
checkers.move("H6", "G5")
for row in "87654321":
    for col in "ABCDEFGH":
        print(checkers.get_cell(col + row).status(), end="")
    print()
