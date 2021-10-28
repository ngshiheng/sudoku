from pywebio import start_server
from pywebio.output import put_markdown, put_table

from src.fixtures import EXAMPLE_BOARD, PAGE_DESCRIPTION

SUDOKU_BOARD_SIZE = 9


def show_board():
    """Renders the Sudoku board"""
    put_table(EXAMPLE_BOARD)


def main():
    """A game of Sudoku"""
    put_markdown(PAGE_DESCRIPTION)
    show_board()


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
