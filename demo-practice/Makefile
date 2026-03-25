.PHONY: help venv install install-dev run check-requirements typecheck format lint test check clean

PYTHON := .venv/bin/python
PIP := .venv/bin/pip
PYTEST := .venv/bin/pytest
MYPY := .venv/bin/mypy
RUFF := .venv/bin/ruff

SRC := src
TESTS := test

.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  make venv               - create virtual environment"
	@echo "  make install            - install runtime dependencies"
	@echo "  make install-dev        - install project and dev tools"
	@echo "  make run                - run application from project environment"
	@echo "  make check-requirements - compare imports with requirements.txt"
	@echo "  make typecheck          - run static type checks"
	@echo "  make format             - format source code"
	@echo "  make lint               - check formatting and style"
	@echo "  make test               - run tests"
	@echo "  make check              - run all checks"
	@echo "  make clean              - remove generated artifacts"

.venv:
	python3 -m venv .venv

venv: .venv

install: .venv requirements.txt
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt

install-dev: install setup.py
	$(PIP) install -e .

run: install-dev
	$(PYTHON) src/app.py

check-requirements: install-dev
	$(PYTHON) scripts/check_requirements.py

typecheck: install-dev
	$(MYPY) $(SRC)

all: check


format: install-dev
	$(RUFF) format $(SRC) $(TESTS)
	$(RUFF) check --fix $(SRC) $(TESTS)

lint: install-dev
	$(RUFF) format --check $(SRC) $(TESTS)
	$(RUFF) check $(SRC) $(TESTS)

test: install-dev
	$(PYTEST) -q

check: lint typecheck check-requirements test

clean:
	rm -rf .venv .mypy_cache .pytest_cache .ruff_cache .coverage build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
