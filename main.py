from pywebio import start_server
from pywebio.output import put_markdown


def main():
    """A game of Sudoku"""
    put_markdown("# Sudoku")


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)
