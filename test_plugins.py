from plugins import load_plugins


def test_echo_plugin_loaded():
    plugins = load_plugins()
    assert "echo" in plugins
