"""__init__.py

Initialize the API namespace.
"""

from .async_api import fetch_friend_activity, fetch_web_access_token
from .models import *
from .sync_api import get_friend_activity, get_web_access_token

__author__ = "Vincent Lin"
__version__ = "0.1.0"
