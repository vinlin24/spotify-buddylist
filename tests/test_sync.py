"""test_sync.py

Tester for the synchronous API.
"""

import json
import os
import re
from datetime import datetime, timezone

import dotenv
import pytest
from spotify_buddylist import (FriendActivity, get_friend_activity,
                               get_web_access_token)

from utils import AbsPath

dotenv.load_dotenv(override=True)

# I guess?
ACCESS_TOKEN_PATTERN = r"[A-Za-z0-9]+"
CLIENT_ID_PATTERN = r"[A-Za-z0-9]+"

SP_DC = os.environ["SPOTIFY_SP_DC_COOKIE"]

with open(AbsPath("test_data.json"), "rt", encoding="utf-8") as fp:
    test_data = json.load(fp)


@pytest.mark.dependency()
def test_get_web_access_token():
    """Test the get_web_access_token function."""
    creds = get_web_access_token(SP_DC)
    assert re.match(ACCESS_TOKEN_PATTERN, creds.accessToken)
    assert creds.accessTokenExpirationTimestamp > datetime.now(timezone.utc)
    assert re.match(CLIENT_ID_PATTERN, creds.clientId)
    assert creds.isAnonymous is False


@pytest.mark.dependency()
@pytest.mark.dependency(depends=["test_get_web_access_token"])
def test_get_friend_activity() -> None:
    """Test the get_friend_activity() function."""
    token = get_web_access_token(SP_DC).accessToken
    activities = get_friend_activity(token)
    # Test the typing? I don't even know lol
    assert isinstance(activities, list)
    assert all(isinstance(a, FriendActivity) for a in activities)
