Ingest — something comes in (right now: a file or raw text you paste)
Process — an LLM reads it and extracts structured notes
Output — the result gets written somewhere (right now: a text file)


Git-Hub Folders
The-Watcher/
├── uv.lock
├── pyproject.toml
├── .python-version
├── .env
├── .env.example
├── .gitignore
├── README.md
├── main.py
├── src/
│   ├── __init__.py
│   ├── ingest.py
│   ├── process.py
│   └── output.py
├── output/
|   └── .gitkeep
├── prompts/
    └── extract_notes.md
