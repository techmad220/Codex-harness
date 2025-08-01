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

`voice_bridge.always_listen()` can run continuously in the background. It waits
for you to say **"hey codex"** and then processes the next phrase as a command.
Saying **"repeat"** will speak back the last processed phrase.

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

 
