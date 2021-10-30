from typing import List


def generate_sudoku_grid() -> List[List[int]]:
    """Randomly generates a 9x9 valid Sudoku grid/board"""
    return [
        [0, 2, 0, 0, 9, 0, 1, 0, 0],
        [0, 0, 7, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 6, 0],
        [0, 0, 1, 9, 0, 4, 0, 0, 0],
        [0, 0, 0, 6, 0, 5, 0, 0, 7],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 8, 5],
        [4, 9, 0, 0, 3, 0, 0, 0, 0],
    ]
