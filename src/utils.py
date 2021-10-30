from random import sample
from typing import List

BLANK_CELL = 0
GRID_SIZE = 9
BOARD_SIZE = GRID_SIZE * GRID_SIZE
SUBGRID_SIZE = GRID_SIZE // 3


def generate_sudoku_grid() -> List[List[int]]:
    """Randomly generates a 9x9 valid Sudoku grid/board

    Note that the Sudoku board generated may have > 1 solution

    https://stackoverflow.com/a/56581709/10067850
    """
    def pattern(r, c):
        return (SUBGRID_SIZE * (r % SUBGRID_SIZE) + r // SUBGRID_SIZE + c) % GRID_SIZE

    def shuffle(s):
        return sample(s, len(s))

    rows = [
        g * SUBGRID_SIZE + r for g in shuffle(range(SUBGRID_SIZE))
        for r in shuffle(range(SUBGRID_SIZE))
    ]

    cols = [
        g * SUBGRID_SIZE + c for g in shuffle(range(SUBGRID_SIZE))
        for c in shuffle(range(SUBGRID_SIZE))
    ]

    digits = shuffle(range(1, SUBGRID_SIZE * SUBGRID_SIZE + 1))

    board = [[digits[pattern(r, c)] for c in cols] for r in rows]

    empties = BOARD_SIZE * SUBGRID_SIZE // 4

    for p in sample(range(BOARD_SIZE), empties):
        board[p // GRID_SIZE][p % GRID_SIZE] = BLANK_CELL

    return board
