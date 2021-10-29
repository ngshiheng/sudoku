import copy
from typing import List

from pywebio.output import output, put_table  # noqa


class Sudoku:
    """A Sudoku puzzle object

    https://en.wikipedia.org/wiki/Sudoku
    """
    BLANK_CELL = 0
    GRID_SIZE = 9
    SUBGRID_SIZE = GRID_SIZE // 3

    def __init__(self, grid: List[List[int]]) -> None:
        self.grid = copy.deepcopy(grid)
        self.original_grid = copy.deepcopy(grid)

        self.row_check = [set() for _ in range(self.GRID_SIZE)]
        self.col_check = [set() for _ in range(self.GRID_SIZE)]
        self.subgrid_check = [[set() for _ in range(self.SUBGRID_SIZE)] for _ in range(self.SUBGRID_SIZE)]

    def show_grid(self) -> None:
        """Shows the current state of the Sudoku grid to stdout"""
        print("-" * self.GRID_SIZE * 3)
        for i in range(self.GRID_SIZE):
            print(self.grid[i])

    def reset_grid(self) -> List[List[int]]:
        """Resets the Sudoku grid to its original state, creates a new copy from the original grid"""
        self.grid = copy.deepcopy(self.original_grid)

        self.row_check = [set() for _ in range(self.GRID_SIZE)]
        self.col_check = [set() for _ in range(self.GRID_SIZE)]
        self.subgrid_check = [[set() for _ in range(self.SUBGRID_SIZE)] for _ in range(self.SUBGRID_SIZE)]
        return self.grid

    def generate_grid(self) -> None:
        """Generates a random valid Sudoku grid"""
        raise NotImplementedError

    def validate_grid(self) -> bool:
        """Validates a Sudoku grid"""
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                digit = self.grid[i][j]
                if digit == self.BLANK_CELL:
                    continue

                if digit in self.row_check[i]:
                    return False
                self.row_check[i].add(digit)

                if digit in self.col_check[j]:
                    return False
                self.col_check[j].add(digit)

                if digit in self.subgrid_check[i // 3][j // 3]:
                    return False
                self.subgrid_check[i // 3][j // 3].add(digit)

        return True

    def solve_grid(self) -> List[List[int]]:
        """Solves a valid Sudoku grid"""
        if not self.validate_grid():
            raise ValueError("Invalid grid")

        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.grid[i][j] == self.BLANK_CELL and self._backtrack(i, j):
                    return self.grid

        raise ValueError("Unable to solve Sudoku puzzle")

    def _backtrack(self, i: int, j: int) -> bool:
        """A backtracking helper function to help solve the Sudoku"""
        if self.grid[i][j] != self.BLANK_CELL:
            j += 1
            if j == self.GRID_SIZE:
                i += 1
                j = 0

            if i == self.GRID_SIZE:
                return True

            return self._backtrack(i, j)

        for digit in range(1, self.GRID_SIZE + 1):
            if digit not in self.row_check[i] and digit not in self.col_check[j] and digit not in self.subgrid_check[i // 3][j // 3]:
                self.grid[i][j] = digit
                self.row_check[i].add(digit)
                self.col_check[j].add(digit)
                self.subgrid_check[i // 3][j // 3].add(digit)

                if self._backtrack(i, j):
                    return True

                self.grid[i][j] = self.BLANK_CELL
                self.row_check[i].remove(digit)
                self.col_check[j].remove(digit)
                self.subgrid_check[i // 3][j // 3].remove(digit)

        return False


class PyWebIOSudoku(Sudoku):
    def __init__(self, grid: List[List[int]]) -> None:
        self.pywebio_grid = copy.deepcopy(grid)

        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                exec(f"self.grid_{i}{j} = output(grid[i][j])")
                exec(f"self.pywebio_grid[{i}][{j}] = self.grid_{i}{j}")

        super().__init__(grid)

    def show_grid(self) -> None:
        """Shows the current state of the Sudoku grid to the browser"""
        put_table(self.pywebio_grid)

    def reset_grid(self) -> List[List[int]]:
        """Resets the Sudoku grid to its original state, creates a new copy from the original grid"""
        super().reset_grid()

        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                exec(f"self.grid_{i}{j}.reset(self.grid[i][j])")

        return self.grid

    def _backtrack(self, i: int, j: int) -> bool:
        """A backtracking helper function to help solve the Sudoku

        This private method mutates and displays the state change of PyWebIO table on the browser
        """
        if self.grid[i][j] != self.BLANK_CELL:
            j += 1
            if j == self.GRID_SIZE:
                i += 1
                j = 0

            if i == self.GRID_SIZE:
                return True

            return self._backtrack(i, j)

        for digit in range(1, self.GRID_SIZE + 1):
            if digit not in self.row_check[i] and digit not in self.col_check[j] and digit not in self.subgrid_check[i // 3][j // 3]:
                self.grid[i][j] = digit
                self.row_check[i].add(digit)
                self.col_check[j].add(digit)
                self.subgrid_check[i // 3][j // 3].add(digit)
                exec(f"self.grid_{i}{j}.reset({digit})")

                if self._backtrack(i, j):
                    return True

                self.grid[i][j] = self.BLANK_CELL
                self.row_check[i].remove(digit)
                self.col_check[j].remove(digit)
                self.subgrid_check[i // 3][j // 3].remove(digit)
                exec(f"self.grid_{i}{j}.reset(0)")

        return False


if __name__ == "__main__":
    grid = [
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

    sudoku = Sudoku(grid)
    sudoku.show_grid()
    sudoku.solve_grid()
    sudoku.show_grid()
