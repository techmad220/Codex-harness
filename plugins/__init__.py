from importlib import import_module
from pathlib import Path


class ResponsePlugin:
    """Base class for response-generating plugins."""

    name = "base"

    def get_response(self, text: str) -> str:
        raise NotImplementedError


def load_plugins(path: Path | None = None):
    """Dynamically load plugins from a directory."""
    plugins = {}
    plugin_dir = path or Path(__file__).parent
    for file in plugin_dir.glob("*.py"):
        if file.name.startswith("_") or file.stem == "__init__":
            continue
        module = import_module(f"plugins.{file.stem}")
        plugin_cls = getattr(module, "Plugin", None)
        if plugin_cls:
            instance = plugin_cls()
            plugins[instance.name] = instance
    return plugins
