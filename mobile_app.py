from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import speech_recognition as sr
import pyttsx3
import argparse


class VoiceBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.label = Label(text='Tap and speak')
        self.add_widget(self.label)
        btn = Button(text='Record')
        btn.bind(on_press=self.record)
        self.add_widget(btn)
        self.engine = pyttsx3.init()

    def record(self, instance):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            text = 'Could not understand'
        self.label.text = text
        self.engine.say(text)

        self.engine.runAndWait()


class VoiceApp(App):
    def __init__(self, plugin="default", **kwargs):
        super().__init__(**kwargs)
        self.plugin = plugin

    def build(self):
        print(f"Launching with plugin: {self.plugin}")
        return VoiceBox()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the mobile voice app')
    parser.add_argument('--plugin', default='default',
                        help='Name of plugin to load')
    args = parser.parse_args()
    VoiceApp(plugin=args.plugin).run()
