NAME := sudoku
SHELL=/bin/bash
POETRY := $(shell command -v poetry 2> /dev/null)

.DEFAULT_GOAL := help

.PHONY: help
help:	## display this help message
	@awk 'BEGIN {FS = ":.*##"; printf "Use make \033[36m<target>\033[0m where \033[36m<target>\033[0m is one of:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: install
install:	## install all dependencies
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	@$(POETRY) install --no-root

.PHONY: lint
lint:	## run flake8
	@$(POETRY) run flake8 --statistics --ignore=W503,E501 --show-source

.PHONY: test
test:	## run unit tests
	@$(POETRY) run python3 -m unittest -v

.PHONY: dev
dev:	## run sudoku locally
	@$(POETRY) run python3 main.py --debug=True --port=8080
