**Project Summary**: This repository is titled "YouTube channel statistics project" (workspace root). Currently there is no application source code present — only a Python virtual environment at `.venv`. The only Python file detected is a simple pandas example inside the environment: `.venv/Include/main.py` which prints a DataFrame (see that file for a minimal pandas usage example).

**Primary Goal For AI Agents**: Help scaffold and iterate a small, well-tested Python data project that fetches, transforms, and analyzes YouTube channel metrics. Avoid editing or committing contents of `.venv`.

**High-level Architecture**: Expected components for this project (scaffold if missing):
- `src/` — application code (API clients, ETL pipelines, data models, CLI entry points).
- `notebooks/` — exploratory analysis and visualizations using pandas/matplotlib.
- `tests/` — pytest unit and integration tests mirroring `src/` structure.
- `data/` — sample or cached CSVs; **do not** commit large datasets; use `.gitignore`.

**Key Developer Workflows & Commands**
- Setup virtual env (Windows PowerShell):
  - `python -m venv .venv`
  - `.\.venv\Scripts\Activate`
  - `pip install -r requirements.txt`
- Run the app (when scaffolded): `python -m src.main` or `python -m src.analytics`.
- Run tests: `pytest --maxfail=1 -q`.
- Format and lint: `black . && ruff .`.

**Conventions & Patterns**
- Use `src` layout (modules under `src/<package>`), not top-level packages.
- Name modules in snake_case; public classes in PascalCase.
- Use environment variables for secrets; expect a `YOUTUBE_API_KEY` or OAuth credential files (do not commit keys).
- Use pandas for ETL, but keep transformations pure functions where easy to test.
- API calls: wrap YouTube Data API calls in a single client module and mock it in tests.

**Scaffolding Suggestions for Agents**
- If `src/` is missing, create minimal structure and an entry point: `src/analytics/__init__.py` + `src/analytics/cli.py`.
- Add a small `src/analytics/yt_client.py` that reads `YOUTUBE_API_KEY` and exposes a `get_channel_stats(channel_id)` function. Mock with a simple local JSON in tests.
- Add `requirements.txt` with `pandas`, `google-api-python-client` (if using the API), `pytest`, `black`, and `ruff`.
- Add `.gitignore` that excludes `/.venv`, `/data`, and `/logs`.

**Testing & CI Expectations**
- Keep unit tests fast and use fixtures: mock network calls for YouTube API with `responses` or `unittest.mock`.
- Integration tests may be gated behind environment variables and must be optional.
- Avoid committing secrets to the repo; use `.env` and `python-dotenv` during developer runs.

**What To Avoid**
- Do not modify or commit files inside `.venv`.
- Do not attempt to infer private API keys or OAuth tokens—ask the user to provide them or use mocks/stubs.

**Areas Where Human Input Is Needed**
- Clarify if YouTube Data API or scraped data will be the canonical source.
- Confirm preferred output targets: CSV, SQLite, cloud storage, or dashboards.

**Quick Example From Current Workspace**
- Observed example (for pandas usage): `.venv/Include/main.py` contains a minimal example that prints a DataFrame — use it only as a quick inspiration, not application code.

If you need further guidance, ask for confirmation before scaffolding and list the first scaffolded files for approval.
