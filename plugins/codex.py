from __future__ import annotations

import os
from typing import Any

import openai

from . import ResponsePlugin


def _call_openai(prompt: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    openai.api_key = api_key
    response: Any = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"].strip()


class Plugin(ResponsePlugin):
    """Use the OpenAI API to generate a response."""

    name = "codex"

    def get_response(self, text: str) -> str:
        return _call_openai(text)
