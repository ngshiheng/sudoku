from pywebio import start_server
from pywebio.output import put_markdown, put_table

PAGE_DESCRIPTION = r"""
# Sudoku

> Sudoku browser game built using Python

1. Ability to generate a random and valid Sudoku board
2. A button that solves the generated board using backtracking

"""


def show_board():
    """Renders the Sudoku board"""
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

    put_table(EXAMPLE_BOARD)


def main():
    """A game of Sudoku"""
    put_markdown(PAGE_DESCRIPTION)
    show_board()


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
