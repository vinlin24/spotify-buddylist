"""__init__.py

Initialize the API namespace.
"""

from .models import *
# By default, export the synchronous versions
# To use the asynchronous versions, import from the async module
from .sync import get_friend_activity, get_web_access_token

__author__ = "Vincent Lin"
__version__ = "0.0.0"
