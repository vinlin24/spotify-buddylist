"""sync.py

Defines the synchronous API functions for this package.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List

import requests

from .models import (AccessFields, Album, Artist, Context, FriendActivity,
                     Track, User)


def get_web_access_token(sp_dc_cookie: str) -> AccessFields:
    """Return access credentials from get_access_token endpoint."""
    # Make the web request
    response = requests.get(
        url="https://open.spotify.com/get_access_token",
        params={
            "reason": "transport",
            "productType": "web_player",
        },
        headers={
            "Cookie": f"sp_dc={sp_dc_cookie}",
        },
        timeout=4.0,
    )

    # Process the JSON data
    data: Dict[str, Any] = response.json()
    # Convert millisecond timestamp to datetime
    timestamp_ms: int = data["accessTokenExpirationTimestampMs"]
    timestamp_dt = datetime.fromtimestamp(timestamp_ms / 1000, timezone.utc)
    data["accessTokenExpirationTimestampMs"] = timestamp_dt

    # Construct and return the dataclass
    return AccessFields(**data)


def _make_friend_activity(friend: Dict[str, Any]) -> FriendActivity:
    """Convert one JSON activity object into a FriendActivity."""
    user = User(**friend["user"])
    track = Track(
        uri=friend["track"]["uri"],
        name=friend["track"]["name"],
        imageUrl=friend["track"]["imageUrl"],
        album=Album(**friend["track"]["album"]),
        artist=Artist(**friend["track"]["artist"]),
        context=Context(**friend["track"]["context"]),
    )
    return FriendActivity(
        timestamp=friend["timestamp"],
        user=user,
        track=track,
    )


def get_friend_activity(access_token: str) -> List[FriendActivity]:
    """Return the friend activities as a list of dataclasses."""
    # Make the web request
    response = requests.get(
        url="https://guc-spclient.spotify.com/presence-view/v1/buddylist",
        headers={
            "Authorization": f"Bearer {access_token}",
        },
        timeout=4.0,
    )

    # Process the JSON data
    friends: List[Dict[str, Any]] = response.json()["friends"]

    # Construct and return the dataclasses
    return [_make_friend_activity(d) for d in friends]
