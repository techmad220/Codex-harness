# Codex-harness

This project demonstrates simple speech recognition and text-to-speech examples written in Python.

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### PyAudio system dependencies

`pyaudio` relies on the PortAudio library being available. On Debian-based systems you can install the necessary headers with:

```bash
sudo apt-get install portaudio19-dev
```

After installing the system package, run the `pip install` command again so that `pyaudio` can build successfully.

