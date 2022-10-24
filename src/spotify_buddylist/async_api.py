"""async.py

Defines the asynchronous API functions for this package.
"""

from asyncio import AbstractEventLoop, get_event_loop
from typing import List, Optional

from .models import AccessFields, FriendActivity
from .sync_api import get_friend_activity, get_web_access_token


async def fetch_web_access_token(sp_dc_cookie: str,
                                 loop: Optional[AbstractEventLoop] = None,
                                 ) -> AccessFields:
    """Return access credentials from get_access_token endpoint."""
    loop = loop or get_event_loop()
    return await loop.run_in_executor(
        None,
        get_web_access_token,
        sp_dc_cookie,
    )


async def fetch_friend_activity(access_token: str,
                                loop: Optional[AbstractEventLoop] = None
                                ) -> List[FriendActivity]:
    """Return the friend activities as a list of dataclasses."""
    loop = loop or get_event_loop()
    return await loop.run_in_executor(
        None,
        get_friend_activity,
        access_token,
    )
