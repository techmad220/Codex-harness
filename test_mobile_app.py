import mobile_app


def test_voice_app_loads_specified_plugin(monkeypatch):
    class DummyBox:
        pass

    monkeypatch.setattr(mobile_app, "VoiceBox", DummyBox)
    app = mobile_app.VoiceApp(plugin='echo')
    widget = app.build()
    assert app.plugin_module is not None
    assert app.plugin_module.echo('hi') == 'hi'
    assert isinstance(widget, DummyBox)
