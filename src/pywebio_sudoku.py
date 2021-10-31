import copy
from typing import List

from pywebio.output import output, put_table, style  # noqa

from .sudoku import Sudoku


class PyWebIOSudoku(Sudoku):
    """A modified Sudoku puzzle that renders on the browser using PyWebIO"""

    def __init__(self, grid: List[List[int]] = None) -> None:
        super().__init__(grid)

        self.pywebio_grid = copy.deepcopy(self.grid)
        self.__init_pywebio_grid()

    def __init_pywebio_grid(self) -> None:
        """Updates each individual cell to be of type Output"""
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.pywebio_grid[i][j] == self.BLANK_CELL:
                    exec(f"self.grid_{i}{j} = style(output(self.grid[i][j]), 'color:red; font-weight:bold')")
                else:
                    exec(f"self.grid_{i}{j} = style(output(self.grid[i][j]), 'color:black; font-weight:bold')")

                exec(f"self.pywebio_grid[{i}][{j}] = self.grid_{i}{j}")

    def __reset_pywebio_grid(self) -> None:
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                if self.grid[i][j] == self.BLANK_CELL:
                    exec(f"self.grid_{i}{j}.reset(style(output(self.grid[i][j]), 'color:red; font-weight:bold'))")
                else:
                    exec(f"self.grid_{i}{j}.reset(style(output(self.grid[i][j]), 'color:black; font-weight:bold'))")

    def display_grid(self) -> None:
        """Displays the current state of the Sudoku grid to the browser"""
        put_table(self.pywebio_grid)

    def generate_grid(self) -> None:
        """Overrides the current grid with a brand new valid Sudoku grid"""
        super().generate_grid()
        self.__reset_pywebio_grid()

    def reset_grid(self) -> None:
        """Resets the current grid to its original state"""
        super().reset_grid()
        self.__reset_pywebio_grid()

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
            if all([
                digit not in self.row_checker[i],
                digit not in self.col_checker[j],
                digit not in self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE],
            ]):
                self.grid[i][j] = digit
                self.row_checker[i].add(digit)
                self.col_checker[j].add(digit)
                self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE].add(digit)
                exec(f"self.grid_{i}{j}.reset(style(output({digit}), 'color:blue; font-weight:bold'))")

                if self._backtrack(i, j):
                    return True

                self.grid[i][j] = self.BLANK_CELL
                self.row_checker[i].remove(digit)
                self.col_checker[j].remove(digit)
                self.subgrid_checker[i // self.SUBGRID_SIZE][j // self.SUBGRID_SIZE].remove(digit)
                exec(f"self.grid_{i}{j}.reset(0)")

        return False
