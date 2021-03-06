import unittest

from src.sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self) -> None:
        self.grid_test_cases = [
            {
                "given": [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9],
                ],
                "expected":[
                    [5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9],
                ],
            },
            {
                "given": [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7],
                ],
                "expected":[
                    [7, 8, 5, 4, 3, 9, 1, 2, 6],
                    [6, 1, 2, 8, 7, 5, 3, 4, 9],
                    [4, 9, 3, 6, 2, 1, 5, 7, 8],
                    [8, 5, 7, 9, 4, 3, 2, 6, 1],
                    [2, 6, 1, 7, 5, 8, 9, 3, 4],
                    [9, 3, 4, 1, 6, 2, 7, 8, 5],
                    [5, 7, 8, 3, 9, 4, 6, 1, 2],
                    [1, 2, 6, 5, 8, 7, 4, 9, 3],
                    [3, 4, 9, 2, 1, 6, 8, 5, 7],
                ],
            },
            {
                "given": [
                    [0, 0, 0, 0, 3, 0, 0, 0, 9],
                    [0, 4, 0, 5, 0, 0, 0, 7, 8],
                    [2, 9, 0, 0, 0, 1, 0, 5, 0],
                    [0, 7, 8, 0, 0, 3, 0, 0, 6],
                    [0, 3, 0, 0, 6, 0, 0, 8, 0],
                    [6, 0, 0, 8, 0, 0, 9, 3, 0],
                    [0, 6, 0, 9, 0, 0, 0, 2, 7],
                    [7, 2, 0, 0, 0, 5, 0, 6, 0],
                    [8, 0, 0, 0, 7, 0, 0, 0, 0],
                ],
                "expected":[
                    [1, 8, 5, 7, 3, 6, 2, 4, 9],
                    [3, 4, 6, 5, 2, 9, 1, 7, 8],
                    [2, 9, 7, 4, 8, 1, 6, 5, 3],
                    [5, 7, 8, 2, 9, 3, 4, 1, 6],
                    [9, 3, 2, 1, 6, 4, 7, 8, 5],
                    [6, 1, 4, 8, 5, 7, 9, 3, 2],
                    [4, 6, 3, 9, 1, 8, 5, 2, 7],
                    [7, 2, 9, 3, 4, 5, 8, 6, 1],
                    [8, 5, 1, 6, 7, 2, 3, 9, 4],
                ],
            },
            {
                "given": [
                    [5, 3, 8, 0, 1, 0, 0, 0, 0],
                    [0, 7, 9, 6, 0, 0, 0, 0, 0],
                    [0, 0, 4, 0, 0, 2, 0, 0, 0],
                    [0, 0, 7, 0, 2, 3, 4, 0, 0],
                    [0, 0, 5, 0, 8, 0, 0, 0, 9],
                    [4, 6, 0, 0, 9, 0, 0, 0, 1],
                    [0, 9, 0, 2, 3, 4, 1, 5, 0],
                    [0, 4, 1, 5, 0, 0, 2, 0, 0],
                    [0, 0, 0, 8, 6, 1, 0, 3, 0],
                ],
                "expected":[
                    [5, 3, 8, 9, 1, 7, 6, 4, 2],
                    [2, 7, 9, 6, 4, 8, 5, 1, 3],
                    [6, 1, 4, 3, 5, 2, 7, 9, 8],
                    [9, 8, 7, 1, 2, 3, 4, 6, 5],
                    [1, 2, 5, 4, 8, 6, 3, 7, 9],
                    [4, 6, 3, 7, 9, 5, 8, 2, 1],
                    [8, 9, 6, 2, 3, 4, 1, 5, 7],
                    [3, 4, 1, 5, 7, 9, 2, 8, 6],
                    [7, 5, 2, 8, 6, 1, 9, 3, 4],
                ],
            },
            {
                "given": [
                    [0, 2, 0, 0, 9, 0, 1, 0, 0],
                    [0, 0, 7, 8, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 3, 6, 0],
                    [0, 0, 1, 9, 0, 4, 0, 0, 0],
                    [0, 0, 0, 6, 0, 5, 0, 0, 7],
                    [8, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 0, 0, 0, 2, 0, 0, 0, 0],
                    [7, 0, 0, 0, 0, 0, 0, 8, 5],
                    [4, 9, 0, 0, 3, 0, 0, 0, 0],
                ],
                "expected":[
                    [5, 2, 4, 3, 9, 6, 1, 7, 8],
                    [3, 6, 7, 8, 4, 1, 9, 5, 2],
                    [1, 8, 9, 7, 5, 2, 3, 6, 4],
                    [2, 5, 1, 9, 7, 4, 8, 3, 6],
                    [9, 4, 3, 6, 8, 5, 2, 1, 7],
                    [8, 7, 6, 2, 1, 3, 5, 4, 9],
                    [6, 1, 5, 4, 2, 8, 7, 9, 3],
                    [7, 3, 2, 1, 6, 9, 4, 8, 5],
                    [4, 9, 8, 5, 3, 7, 6, 2, 1],
                ],
            },
        ]

    def test_solve_grid(self) -> None:
        for grid in self.grid_test_cases:
            sudoku = Sudoku(grid["given"])
            got = sudoku.solve_grid()
            self.assertListEqual(got, grid["expected"])
            self.assertListEqual(sudoku.grid, grid["expected"])
            self.assertIs(sudoku.grid, got)

    def test_reset_grid(self) -> None:
        for grid in self.grid_test_cases:
            sudoku = Sudoku(grid["given"])
            sudoku.solve_grid()
            sudoku.reset_grid()
            self.assertListEqual(sudoku.grid, sudoku.original_grid)
            self.assertIsNot(sudoku.grid, sudoku.original_grid)

    def test_solve_sudoku_after_reset_grid_does_not_raise_any_exceptions(self) -> None:
        for grid in self.grid_test_cases:
            sudoku = Sudoku(grid["given"])
            sudoku.solve_grid()
            sudoku.reset_grid()
            sudoku.solve_grid()
            self.assertListEqual(sudoku.grid, grid["expected"])

    def test_generate_grid(self) -> None:
        for grid in self.grid_test_cases[:2]:
            sudoku = Sudoku(grid["given"])
            self.assertListEqual(sudoku.grid, grid["given"])

            sudoku.solve_grid()
            self.assertListEqual(sudoku.grid, grid["expected"])

            sudoku.generate_grid()
            self.assertNotEqual(sudoku.grid, grid["given"])

            sudoku.solve_grid()
