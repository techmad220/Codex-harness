import importlib


def test_has_function():
    mod = importlib.import_module('auto_fix_merge')
    assert hasattr(mod, 'fix_conflicts')
