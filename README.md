# Sudoku

> Sudoku browser game built using Python

## Goals

1. Ability to generate a random and valid Sudoku board
2. A button that solves the generated board using backtracking

## Development

### Installation

Make sure you have [poetry](https://python-poetry.org/docs/#installation) installed on your machine.

```sh
poetry install

# Installing dependencies only
poetry install --no-root

# Updating dependencies to their latest versions
poetry update
```

### Setup Pre-commit Hooks

Before you begin your development work, make sure you have installed [pre-commit hooks](https://pre-commit.com/index.html#installation).

Some example useful invocations:

-   `pre-commit install`: Default invocation. Installs the pre-commit script alongside any existing git hooks.
-   `pre-commit install --install-hooks --overwrite`: Idempotently replaces existing git hook scripts with pre-commit, and also installs hook environments.
-   `pre-commit run`: Run hooks.

---

## Usage

To run the game locally

```sh
poetry run python3 main.py --debug=True --port=8080
```

---

## References

-   https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
