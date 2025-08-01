try:
    import speech_recognition as sr  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    sr = None

try:
    import pyttsx3  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    pyttsx3 = None


def _speak(engine, text: str) -> None:
    """Helper that speaks the provided text."""
    engine.say(text)
    engine.runAndWait()


def _handle_command(command: str, engine, last: str) -> str:
    """Execute a voice command and return the updated last message."""
    if command.lower() == "repeat" and last:
        _speak(engine, last)
        return last

    _speak(engine, command)
    return command


def listen_and_repeat():
    """Listen once and repeat the spoken phrase via text-to-speech."""
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
    _handle_command(text, engine, "")


def always_listen(
    trigger_word: str = "hey codex", *, iterations: int | None = None
) -> None:
    """Continuously listen and respond after the trigger word.

    Parameters
    ----------
    trigger_word:
        Phrase that activates command listening.
    iterations:
        Optional number of command cycles to process before returning. ``None``
        runs indefinitely. This is mainly useful for tests.
    """

    if sr is None or pyttsx3 is None:
        raise RuntimeError("voice dependencies are not installed")

    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    last_message = ""
    processed = 0

    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            heard = recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            continue

        if trigger_word in heard:
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                continue
            last_message = _handle_command(command, engine, last_message)
            processed += 1
            if iterations is not None and processed >= iterations:
                break


if __name__ == "__main__":
    listen_and_repeat()
