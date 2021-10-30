<h1 align="center"><strong>Sudoku Solver</strong></h1>
<h3 align="center">A web-based Sudoku solver built using Python and Python only
</h3>

<p align="center">
  <img width=auto height=auto src="https://media.giphy.com/media/ZJFVjMIFiY9VC5UAom/giphy.gif">
</p>

<br />

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

To run locally on your browser:

```sh
poetry run python3 main.py --debug=True --port=8080
```

Then, visit `http://localhost:8080` on your browser.

---

## Deployment

This section is only required if you intend to deploy to [GAE](https://cloud.google.com/appengine).

For reference, do check [this](https://github.com/wang0618/pywebio-in-cloud) out.

### Dependencies

Configure all dependencies you will need for your web service in your `requirements.txt` file.

```sh
# This command exports the poetry lock file to other formats.
poetry export -f requirements.txt --output requirements.txt
```

### Google App Engine

```sh
# To deploy app configuration
gcloud init
gcloud app deploy app.yml --project xxx

# To stream logs
gcloud app logs tail -s default
```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Steps

1. Fork this
2. Create your feature branch (git checkout -b feature/fooBar)
3. Please make sure you have installed the pre-commit hook and make sure it passes all the lint and format check
4. Commit your changes (git commit -am 'Add some fooBar')
5. Push to the branch (git push origin feature/fooBar)
6. Create a new Pull Request

---

## References

-   https://leetcode.com/problems/sudoku-solver/
-   https://leetcode.com/problems/valid-sudoku/
