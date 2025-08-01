import logging
import plugins


def test_load_plugins_handles_missing_dependencies(caplog):
    with caplog.at_level(logging.WARNING):
        loaded = plugins.load_plugins()
    assert 'echo' in loaded
    assert 'broken' not in loaded
    # ensure a warning was logged for the broken plugin
    assert any('broken' in record.message for record in caplog.records)
