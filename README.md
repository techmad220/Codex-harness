# Codex-harness

## Usage

Run the mobile app with a specific plugin:

```bash
python mobile_app.py --plugin myplugin
```

Replace `myplugin` with the plugin you want to load.
Plugins are discovered at runtime using `plugins.load_plugins()`. If the
requested plugin cannot be imported, the app continues without it and prints a
message.
This project demonstrates simple speech recognition and text-to-speech examples
written in Python.

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

## Project status

This repository is a minimal demonstration of speech recognition and
text-to-speech on the desktop. It is **not** production ready and should be used
as a learning resource or starting point. Production deployments require robust
error handling, structured logging, configuration management and a more formal
plugin API. Expanding the test suite and adding continuous integration would
also improve stability.

## Potential enhancements

- Add a command-line flag for saving recognized text to a file
- Provide a GUI control to select different input/output audio devices
- Package the plugin system as a dedicated API so third-party plugins can be
  discovered and configured easily

 
