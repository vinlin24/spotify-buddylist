"""async.py

Defines the asynchronous API functions for this package.
"""

from asyncio import AbstractEventLoop, get_event_loop
from typing import List

from .models import AccessFields, FriendActivity
from .sync import get_friend_activity as sync_get_friend_activity
from .sync import get_web_access_token as sync_get_web_access_token


async def get_web_access_token(sp_dc_cookie: str,
                               loop: AbstractEventLoop | None = None,
                               ) -> AccessFields:
    """Return access credentials from get_access_token endpoint."""
    loop = loop or get_event_loop()
    return await loop.run_in_executor(
        None,
        sync_get_web_access_token,
        sp_dc_cookie,
    )


async def get_friend_activity(access_token: str,
                              loop: AbstractEventLoop | None = None
                              ) -> List[FriendActivity]:
    """Return the friend activities as a list of dataclasses."""
    loop = loop or get_event_loop()
    return await loop.run_in_executor(
        None,
        sync_get_friend_activity,
        access_token,
    )
