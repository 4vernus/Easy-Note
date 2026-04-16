# Easy Note

A CLI tool that extracts structured study notes from text files using AI.

## About

Easy Note reads a text file, sends it to a language model, and returns clean, structured markdown notes focused on what matters for exams and real-world application.

This is v0.1 — the foundation of a larger vision: a background agent that automatically takes notes while you study, powered by screen capture and Obsidian integration.

## Installation

Requires Python 3.14+ and [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/4vernus/Easy-Note.git
cd Easy-Note
uv sync
```

Copy `.env.example` to `.env` and add your Gemini API key:

```bash
cp .env.example .env
```

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey).

## Usage

```bash
uv run main.py path/to/notes.txt
```

With a custom output name:

```bash
uv run main.py path/to/notes.txt -o my_notes
```

Output files are saved as markdown in the `outputs/` folder.

## Roadmap

- [x] Text file to structured notes
- [ ] PDF and DOCX support
- [ ] Multiple LLM provider support
- [ ] Screenpipe integration for automatic capture while studying
- [ ] Obsidian vault sync
- [ ] Flashcard generation

## License

MIT