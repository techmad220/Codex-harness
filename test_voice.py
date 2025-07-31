import importlib


def test_import():
    module = importlib.import_module('voice_bridge')
    assert hasattr(module, 'listen_and_repeat')
