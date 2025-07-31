from __future__ import annotations

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import pyttsx3
import speech_recognition as sr

from plugins import load_plugins


class VoiceBox(BoxLayout):
    def __init__(self, plugin_name: str, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="Tap and speak")
        self.add_widget(self.label)
        btn = Button(text="Record")
        btn.bind(on_press=self.record)
        self.add_widget(btn)
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.plugins = load_plugins()
        self.plugin = self.plugins.get(plugin_name, self.plugins["echo"])

    def record(self, _instance):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            text = ""
        if not text:
            self.label.text = "Could not understand"
            self.engine.say(self.label.text)
            self.engine.runAndWait()
            return
        response = self.plugin.get_response(text)
        self.label.text = response
        self.engine.say(response)
        self.engine.runAndWait()


class VoiceApp(App):
    def __init__(self, plugin_name: str = "echo", **kwargs):
        super().__init__(**kwargs)
        self.plugin_name = plugin_name

    def build(self):
        return VoiceBox(self.plugin_name)


if __name__ == "__main__":
    VoiceApp().run()
