"""utils.py

Defines some useful tools for tests.
"""

from __future__ import annotations

from pathlib import Path


class AbsPath(str):
    """str subclass for making a string path resolved and absolute."""
    def __new__(cls, relative: str) -> AbsPath:
        path = (Path(__file__).parent / relative).resolve()
        # Raise this earlier than later
        if not path.exists():
            raise FileNotFoundError(path)
        return super().__new__(cls, str(path))
