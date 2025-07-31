from __future__ import annotations

import argparse

import pyttsx3
import speech_recognition as sr

from plugins import load_plugins


def listen(recognizer: sr.Recognizer) -> str:
    """Record audio and return transcribed text."""
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return ""


def speak(engine: pyttsx3.Engine, text: str) -> None:
    engine.say(text)
    engine.runAndWait()


def run(plugin_name: str) -> None:
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    plugins = load_plugins()
    plugin = plugins.get(plugin_name)
    if not plugin:
        raise SystemExit(f"Plugin '{plugin_name}' not found")
    text = listen(recognizer)
    if not text:
        speak(engine, "Sorry, I did not understand.")
        return
    print(f"You said: {text}")
    response = plugin.get_response(text)
    print(f"Response: {response}")
    speak(engine, response)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("plugin", nargs="?", default="echo", help="Plugin name")
    args = parser.parse_args()
    run(args.plugin)
