# Copilot / AI Agent Instructions — Zippy Quotes
````instructions
# Copilot / AI Agent Instructions — Zippy Quotes

Purpose
- Small CLI app that prints Zippy quotes. Runtime data is a JSON array in `src/quotes.json`.

Big picture (what to know quickly)
- Runtime: `src/cli.py` loads a JSON file (`quotes.json`) from CWD and prints a random entry.
- Package: `src/zippy/quotes.py` currently contains the canonical `quotes` list (large array) used by the project.
- Data duplication: there's also a `quotes.json` at repo root; the runtime behavior depends on where you run the CLI (see "Run" below).

Run & developer workflows
- Install deps: `pip install -r requirements.txt`.
- Typical runs:
    - From `src/`: `cd src && python cli.py` (simplest; `quotes.json` is found by filename).
    - From repo root: `PYTHONPATH=src python src/cli.py` (Windows: `set PYTHONPATH=src && python src/cli.py`).
- Tests: none included. Use the CLI interactively as a smoke check.

Key files to inspect
- `src/cli.py` — entrypoint. Uses `load_quotes(filename="quotes.json")` and `random.choice(quotes)`; it also `from zippy.quotes import get_random_quote` but `get_random_quote` is not implemented.
- `src/zippy/quotes.py` — contains the `quotes` array (primary source for quotes when importing the package).
- `src/quotes.json` — JSON array used when running from `src/`.
- `quotes.json` (repo root) — duplicate; update if you expect users to run from repo root.

Project-specific patterns & gotchas
- CWD vs PYTHONPATH matters: the CLI opens `quotes.json` from the working directory, not a package resource. Either run from `src/` or set `PYTHONPATH`.
- Large data: `src/zippy/quotes.py` and `src/quotes.json` contain very large arrays — prefer editing `src/quotes.json` for data changes and keep encoding as UTF-8.
- Import vs runtime API mismatch: `src/cli.py` imports `get_random_quote` from `zippy.quotes` but that helper is missing. Two safe approaches:
    1. Implement `get_random_quote()` inside `src/zippy/quotes.py` (recommended minimal change).
    2. Remove the unused import in `src/cli.py` and continue to use `load_quotes()` + `random.choice(...)`.

Small, recommended fixes (copy-paste)
- Implement package helper in `src/zippy/quotes.py`:

```python
import random

def get_random_quote():
        # uses in-package `quotes` list
        return random.choice(quotes)
```

- Or centralize loading and expose it from the package (more robust):

```python
import json
import random
from pathlib import Path

def load_quotes(path=None):
        path = Path(path or Path(__file__).parents[1] / "quotes.json")
        with path.open("r", encoding="utf-8") as f:
                return json.load(f)

def get_random_quote(path=None):
        q = load_quotes(path)
        return random.choice(q)
```

Integration points & external dependencies
- No external services. Only dependency is Python standard library; check `requirements.txt` (currently empty/minimal).

PR guidance & conventions
- Keep changes focused and minimal. If you change where `quotes.json` is loaded from, update README.md examples and ensure CI/local runs still find the data.
- For data edits: prefer editing `src/quotes.json` and run `cd src && python cli.py` to validate.

Where to start as an AI agent
- Inspect `src/cli.py` and `src/zippy/quotes.py` first. Small, safe PRs are:
    - Add `get_random_quote()` to `src/zippy/quotes.py`.
    - Add a `load_quotes()` in the package and update `cli.py` to use it.
    - Sync `quotes.json` files if you change data.

If anything here is unclear or you want an automated smoke test, say which change you'd like me to implement and I'll prepare the patch and run a local check.

````
