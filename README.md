<h1 align="center"><strong>PyWebIO Sudoku Solver</strong></h1>
<h3 align="center">A web-based Sudoku solver built using Python and Python only
</h3>

<p align="center">
  <img width=auto height=auto src="https://media.giphy.com/media/AmEh0Bo8B1XQ7869i1/giphy.gif">
</p>

<br />

> The motivation is to demonstrate how [Backtracking](https://en.wikipedia.org/wiki/Backtracking) algorithm works.

Some of the key highlights/features of this Sudoku solver app:

-   Ability to generate a random, valid Sudoku puzzle
-   Solves a Sudoku puzzle using backtracking
-   Able to check if a Sudoku board is valid
-   Demo is hosted on [Heroku](https://pywebio-sudoku.herokuapp.com/)

## Getting Started

### Installation

Make sure you have [poetry](https://python-poetry.org/docs/#installation) installed on your machine.

```sh
poetry install

# Optional: Installing dependencies only
poetry install --no-root

# Optional: Updating dependencies to their latest versions
poetry update
```

### Usage

To run on debug mode locally on your browser:

```sh
poetry run python3 main.py --debug=True --port=8080
```

Then, visit `http://localhost:8080/` on your browser.

## Pre-commit Hooks

Before you begin your development work, make sure you have installed [pre-commit hooks](https://pre-commit.com/index.html#installation).

Some example useful invocations:

-   `pre-commit install`: Default invocation. Installs the pre-commit script alongside any existing git hooks.
-   `pre-commit install --install-hooks --overwrite`: Idempotently replaces existing git hook scripts with pre-commit, and also installs hook environments.
-   `pre-commit run`: Run hooks.

## Deployment

Check [this](https://github.com/wang0618/pywebio-in-cloud) out.

To generate a [`requirements.txt`](./requirements.txt) file:

```sh
# This command exports the poetry lock file to other formats.
poetry export -f requirements.txt --output requirements.txt
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

## References

-   https://leetcode.com/problems/sudoku-solver/
-   https://leetcode.com/problems/valid-sudoku/
