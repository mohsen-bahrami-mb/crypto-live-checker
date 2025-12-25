# crypto-check

## What this project does

crypto-check is a small Python project for checking and processing cryptocurrency-related data. It provides a minimal command-line entry point and a focused module under `src` that implements the checking logic. The project is intended to be lightweight and practical for small applications, CLI tools, or integrations with public crypto APIs.

## Why it might be useful

- A compact, clear structure for a small Python crypto utility.
- Implement and test simple crypto data checks or parsers.
- Serve as the basis for a small CLI tool or API integration.

## Key features

- Minimal structure with `main.py` as the entry point.
- `src/crypto_checker.py` holds the core checking logic.

## Prerequisites

- Python 3.8+
- Pipenv (optional) or any virtual environment tool such as `venv`

## Install & run

Using Pipenv (recommended):

```bash
pipenv install
pipenv shell
python main.py
```

Using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate
# If you create a requirements.txt, install it with:
# pip install -r requirements.txt
python main.py
```

## Project layout

- `main.py` — program entry point.
- `src/crypto_checker.py` — crypto checking logic.
- `src/__init__.py`

## Development notes

- Add dependencies to `Pipfile` or create a `requirements.txt` for pip installs.
- Consider adding small tests and running them before commits.