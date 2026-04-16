# Easy Note

A CLI tool that extracts structured study notes from documents using AI.

## About

The Watcher reads a document, sends its content to a language model, and returns clean, structured markdown notes focused on what matters for exams and real-world application.

Current version is v0.2 — the foundation of a larger vision: a background agent that automatically takes notes while you study, powered by screen capture and Obsidian integration.

## Supported Formats

- `.txt` — plain text
- `.md` — markdown
- `.pdf` — text-based PDFs (scanned PDFs not yet supported)
- `.docx` — Microsoft Word
- `.html` — saved webpages

## Installation

Requires Python 3.14+ and [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/4vernus/The-Watcher.git
cd The-Watcher
uv sync
```

Copy `.env.example` to `.env` and add your Gemini API key:

```bash
cp .env.example .env
```

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey).

## Usage

```bash
uv run main.py path/to/notes.pdf
```

With a custom output name:

```bash
uv run main.py path/to/notes.pdf -o my_notes
```

Output files are saved as markdown in the `outputs/` folder. If a file with the same name already exists, a numbered suffix is added automatically (e.g. `my_notes_2.md`).

## Roadmap

- [x] Text file to structured notes
- [x] PDF, DOCX, HTML, and Markdown support
- [ ] URL input (handling login/JS-rendered pages)
- [ ] PowerPoint (.pptx) support
- [ ] Scanned PDF support via OCR
- [ ] Multiple LLM provider support
- [ ] Screenpipe integration for automatic capture while studying
- [ ] Obsidian vault sync
- [ ] Flashcard generation

## License

MIT