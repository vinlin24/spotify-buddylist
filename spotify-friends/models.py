"""models.py

Defines the dataclass models used in this package.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime

URI_PATTERN = r"spotify:(album|artist|track|user|playlist):([a-zA-z-0-9]+)"
"""Regex total matcher for a Spotify resource URI.

Groups:
    1: One of "album", "artist", "track", "user", "playlist"
    2: The alphanumeric ID of the resource
"""

URL_TEMPLATE = "https://open.spotify.com/{category}/{id}"
"""The URL template for a Spotify resource.

Placeholders:
    category: One of "album", "artist", "track", "user", "playlist"
    id: The alphanumeric ID of the resource
"""

uri_matcher = re.compile(URI_PATTERN)


@dataclass
class _NamedBase:
    """Base for dataclasses that have a unique URI and a name field."""
    uri: str
    name: str
    url: str = field(init=False)

    def __post_init__(self) -> None:
        match = uri_matcher.match(self.uri)
        if match is None:
            raise ValueError(f"{self.uri=} does not match {URI_PATTERN=}")
        category, id_ = match.groups()
        self.url = URL_TEMPLATE.format(category=category, id=id_)


@dataclass
class User(_NamedBase):
    """A minimal model of the friend user."""
    image_url: str


@dataclass
class Album(_NamedBase):
    """A minimal model of the album of the displayed track."""


@dataclass
class Artist(_NamedBase):
    """A minimal model of the artist of the displayed track."""


@dataclass
class Context(_NamedBase):
    """The context of the displayed track."""
    index: int


@dataclass
class Track(_NamedBase):
    """The track displayed in friend activity."""
    image_url: str
    album: Album
    artist: Artist
    context: Context


@dataclass
class FriendActivity:
    """Class wrapper for the friend activity JSON data."""
    timestamp: datetime
    user: User
    track: Track
