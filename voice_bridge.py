import speech_recognition as sr
import pyttsx3


def listen_and_repeat():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        text = "Sorry, I did not understand."
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    listen_and_repeat()
