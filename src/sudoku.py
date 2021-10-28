from typing import List

EXAMPLE_BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


class Sudoku:
    """A Sudoku object with custom methods"""
    BOARD_SIZE = 9
    SUB_BOXES_SIZE = 9 // 3

    def __init__(self, board) -> None:
        self.board = board
        self.row_check = [set() for _ in range(self.BOARD_SIZE)]
        self.col_check = [set() for _ in range(self.BOARD_SIZE)]
        self.box_check = [[set() for _ in range(self.SUB_BOXES_SIZE)] for _ in range(self.SUB_BOXES_SIZE)]

    def print_board(self) -> None:
        """Prints a Sudoku board"""
        print("-" * self.BOARD_SIZE * 3)
        for i in range(self.BOARD_SIZE):
            print(self.board[i])

    def validate(self) -> bool:
        """Validates a Sudoku board"""
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                number = self.board[i][j]
                if number == 0:
                    continue

                if number in self.row_check[i]:
                    return False
                self.row_check[i].add(number)

                if number in self.col_check[j]:
                    return False
                self.col_check[j].add(number)

                if number in self.box_check[i // 3][j // 3]:
                    return False
                self.box_check[i // 3][j // 3].add(number)

        return True

    def solve(self) -> List[List[int]]:
        """Solves a valid Sudoku board"""
        if self.validate():
            for i in range(self.BOARD_SIZE):
                for j in range(self.BOARD_SIZE):
                    if self.board[i][j] == 0:
                        self._backtrack(i, j)
            return self.board

        raise ValueError("Invalid board")

    def _backtrack(self, i: int, j: int) -> bool:
        """A backtracking helper function for self.solve()"""
        self.print_board()

        if self.board[i][j] != 0:
            j += 1
            if j == self.BOARD_SIZE:
                i += 1
                j = 0

            if i == self.BOARD_SIZE:
                return True

            return self._backtrack(i, j)

        for number in range(1, self.BOARD_SIZE + 1):
            if number not in self.row_check[i] and number not in self.col_check[j] and number not in self.box_check[i // 3][j // 3]:
                self.board[i][j] = number
                self.row_check[i].add(number)
                self.col_check[j].add(number)
                self.box_check[i // 3][j // 3].add(number)

                if self._backtrack(i, j):
                    return True

                self.board[i][j] = 0
                self.row_check[i].remove(number)
                self.col_check[j].remove(number)
                self.box_check[i // 3][j // 3].remove(number)

        return False


if __name__ == "__main__":
    sudoku = Sudoku(EXAMPLE_BOARD)
    sudoku.solve()
    sudoku.print_board()
