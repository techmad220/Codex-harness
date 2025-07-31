# Codex Voice Harness

This project provides a simple bridge between voice input and Codex (or other
chat backends) with a plugin system for extensibility. It also ships with a
helper script to automatically resolve merge conflicts in git repositories.

## Components

- `voice_bridge.py` – command line interface for recording speech, routing it
  through a response plugin and reading the reply aloud.
- `mobile_app.py` – minimal Kivy app using the same plugins for mobile use.
- `plugins/` – directory containing response plugins.
  - `echo.py` – echoes back the spoken text.
  - `codex.py` – sends the text to the OpenAI API (requires `OPENAI_API_KEY`).
- `auto_fix_merge.py` – resolves git merge conflicts with a chosen strategy.

## Usage

To run the desktop bridge with the default echo plugin:

```bash
python voice_bridge.py
```

To use the Codex plugin:

```bash
OPENAI_API_KEY=... python voice_bridge.py codex
```

Run the mobile app similarly:

```bash
python mobile_app.py
```

To automatically fix merge conflicts:

```bash
python auto_fix_merge.py --strategy theirs
```

## Development

Install dependencies with `pip install -r requirements.txt` and run linters and
tests using `flake8` and `pytest`.
