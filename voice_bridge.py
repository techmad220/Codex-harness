try:
    import speech_recognition as sr  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    sr = None

try:
    import pyttsx3  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    pyttsx3 = None


def listen_and_repeat():
    if sr is None or pyttsx3 is None:
        raise RuntimeError("voice dependencies are not installed")

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
