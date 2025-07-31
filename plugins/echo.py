from . import ResponsePlugin


class Plugin(ResponsePlugin):
    """Simple plugin that echoes the user's text."""

    name = "echo"

    def get_response(self, text: str) -> str:
        return text
