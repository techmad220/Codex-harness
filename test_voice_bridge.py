import voice_bridge


class DummyEngine:
    def __init__(self):
        self.spoken = []

    def say(self, text):
        self.spoken.append(text)

    def runAndWait(self):
        pass


class DummyRecognizer:
    def __init__(self, responses):
        self._responses = iter(responses)

    def listen(self, source):
        return object()

    def recognize_google(self, audio):
        return next(self._responses)


class DummyMicrophone:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass


class DummySR:
    def __init__(self, responses):
        self._responses = responses

    def Recognizer(self):
        return DummyRecognizer(self._responses)

    Microphone = DummyMicrophone


def test_always_listen_repeat(monkeypatch):
    responses = ["hey codex", "hello world", "hey codex", "repeat"]
    engine = DummyEngine()
    monkeypatch.setattr(voice_bridge, "sr", DummySR(responses))
    monkeypatch.setattr(
        voice_bridge,
        "pyttsx3",
        type("E", (), {"init": lambda: engine}),
    )
    voice_bridge.always_listen(iterations=2)
    assert engine.spoken == ["hello world", "hello world"]
