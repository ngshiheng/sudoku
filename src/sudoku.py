import copy
from random import sample
from typing import List


class Sudoku:
    """A Sudoku puzzle

    https://en.wikipedia.org/wiki/Sudoku
    """
    BLANK_CELL = 0
    GRID_SIZE = 9
    SUBGRID_SIZE = GRID_SIZE // 3
    GRID_AREA = GRID_SIZE * GRID_SIZE

    def __init__(self, grid: List[List[int]] = None) -> None:
        """Initialize the Sudoku

        Generates our own Sudoku puzzle if grid is not provided
        """
        if not grid:
            grid = self.__generate_grid()

        self.__init_checkers()
        self.grid = copy.deepcopy(grid)
        self.original_grid = copy.deepcopy(grid)

    def __init_checkers(self) -> None:
        """Initializes all *_checker, which are lists of sets

        The *_checker is used to ensure that the same digit is not present in the current row, current column, and current 3x3 subgrid
        """
        self.row_checker = [set() for _ in range(self.GRID_SIZE)]
        self.col_checker = [set() for _ in range(self.GRID_SIZE)]
        self.subgrid_checker = [[set() for _ in range(self.SUBGRID_SIZE)] for _ in range(self.SUBGRID_SIZE)]

    def __fill_checkers(self) -> None:
        """Fill up the *_checkers"""
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                digit = self.grid[i][j]
                if digit == self.BLANK_CELL:
                    continue

                if any([
                    digit in self.row_checker[i],
                    digit in self.col_checker[j],
                    digit in self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE],
                ]):
                    raise ValueError("Invalid grid")

                self.row_checker[i].add(digit)
                self.col_checker[j].add(digit)
                self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE].add(digit)

    def __generate_grid(self) -> List[List[int]]:
        """Randomly generates a 9x9 valid Sudoku grid/board puzzle

        Note that the Sudoku board generated may have > 1 solution
        Does not modify the current state of the Sudoku board

        https://stackoverflow.com/a/56581709/10067850
        """
        def pattern(r, c):
            return (self.SUBGRID_SIZE * (r % self.SUBGRID_SIZE) + r // self.SUBGRID_SIZE + c) % self.GRID_SIZE

        def shuffle(s):
            return sample(s, len(s))

        rows = [
            g * self.SUBGRID_SIZE + r for g in shuffle(range(self.SUBGRID_SIZE))
            for r in shuffle(range(self.SUBGRID_SIZE))
        ]

        cols = [
            g * self.SUBGRID_SIZE + c for g in shuffle(range(self.SUBGRID_SIZE))
            for c in shuffle(range(self.SUBGRID_SIZE))
        ]

        digits = shuffle(range(1, self.SUBGRID_SIZE * self.SUBGRID_SIZE + 1))

        board = [[digits[pattern(r, c)] for c in cols] for r in rows]

        empties = self.GRID_AREA * self.SUBGRID_SIZE // 4

        for p in sample(range(self.GRID_AREA), empties):
            board[p // self.GRID_SIZE][p % self.GRID_SIZE] = self.BLANK_CELL

        return board

    def display_grid(self) -> None:
        """Displays the current state of the Sudoku grid to stdout"""
        print("-" * self.GRID_SIZE * 3)
        for i in range(self.GRID_SIZE):
            print(self.grid[i])

    def generate_grid(self) -> None:
        """Overrides the current grid with a brand new valid Sudoku grid"""
        self.new_grid = self.__generate_grid()

        self.__init_checkers()
        self.grid = copy.deepcopy(self.new_grid)
        self.original_grid = copy.deepcopy(self.new_grid)

    def reset_grid(self) -> None:
        """Resets the current grid to its original state"""
        self.__init_checkers()
        self.grid = copy.deepcopy(self.original_grid)

    def solve_grid(self) -> List[List[int]]:
        """Solves a valid Sudoku grid"""
        self.__fill_checkers()

        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.grid[i][j] == self.BLANK_CELL and self._backtrack(i, j):
                    return self.grid

        raise ValueError("Unable to solve Sudoku puzzle, are you sure that the puzzle is valid?")

    def _backtrack(self, i: int, j: int) -> bool:
        """A backtracking helper function to help solve the Sudoku puzzle"""
        if self.grid[i][j] != self.BLANK_CELL:
            j += 1
            if j == self.GRID_SIZE:
                i += 1
                j = 0

            if i == self.GRID_SIZE:
                return True

            return self._backtrack(i, j)

        for digit in range(1, self.GRID_SIZE + 1):
            if all([
                digit not in self.row_checker[i],
                digit not in self.col_checker[j],
                digit not in self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE],
            ]):
                self.grid[i][j] = digit
                self.row_checker[i].add(digit)
                self.col_checker[j].add(digit)
                self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE].add(digit)

                if self._backtrack(i, j):
                    return True

                self.grid[i][j] = self.BLANK_CELL
                self.row_checker[i].remove(digit)
                self.col_checker[j].remove(digit)
                self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE].remove(digit)

        return False


if __name__ == "__main__":
    sudoku = Sudoku()
    sudoku.display_grid()
    sudoku.solve_grid()
    sudoku.display_grid()
