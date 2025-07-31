import importlib


def test_import():
    module = importlib.import_module('voice_bridge')
    assert hasattr(module, 'run')
    assert hasattr(module, 'listen')
    assert hasattr(module, 'speak')
