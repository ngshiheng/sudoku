from pywebio.output import put_buttons, put_markdown

from src.pywebio_sudoku import PyWebIOSudoku

INTRODUCTION = r"""
# PyWebIO Sudoku Solver

## Motivation

To demonstrate how [Backtracking](https://en.wikipedia.org/wiki/Backtracking) algorithm works with Sudoku, visually. You may find the source code [here](https://github.com/ngshiheng/sudoku).

## Demo
"""

DETAILS = r"""
### Rationale

- Before assigning a digit to a cell, we should check whether it is safe to assign.
- Check that the same digit is not present in the current row, current column, and current 3x3 subgrid.
- After checking for safety, assign the digit, and recursively check whether this assignment leads to a solution or not.
- If the assignment doesn’t lead to a solution, then try the next digit for the current empty cell.
- And if none of the digits (1 to 9) leads to a solution, return `False`.
- We return `True` if we have reached gone through the entire grid.

## Sudoku, 数独

A popular Japanese puzzle game based on the logical placement of digits.

Sudoku doesn’t require any calculation nor special math skills.


### How to play

The goal of Sudoku is to fill in a 9×9 grid with digits so that each column, row, and 3×3 section contain the digits between 1 to 9.

At the beginning of the game, the 9×9 grid will have some of the squares filled in.

Your job is to use logic to fill in the missing digits and complete the grid.

### Rules

A move is **incorrect** if:

- Any row contains more than one of the same digit from 1 to 9
- Any column contains more than one of the same digit from 1 to 9
- Any 3×3 grid contains more than one of the same digit from 1 to 9
"""


def main():
    """Sudoku Solver"""
    put_markdown(INTRODUCTION)

    sudoku = PyWebIOSudoku()
    sudoku.display_grid()

    put_buttons(
        [
            dict(label="Solve", value="Solve", color="primary"),
            dict(label="Clear", value="Clear", color="warning"),
            dict(label="Next Puzzle", value="Next Puzzle", color="secondary"),
        ], onclick=[
            sudoku.solve_grid,
            sudoku.reset_grid,
            sudoku.generate_grid,
        ],
    )

    put_markdown(DETAILS)


if __name__ == "__main__":
    import argparse

    from pywebio import start_server as start_ws_server
    from pywebio.platform.tornado_http import start_server as start_http_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help='Run on the given port', type=int, default=8080)
    parser.add_argument("-d", "--debug", help='Run on debug mode', type=bool, default=False)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')

    args = parser.parse_args()

    if args.http:
        start_http_server(main, port=args.port, debug=args.debug)
    else:
        start_ws_server(main, port=args.port, websocket_ping_interval=30, debug=args.debug)
