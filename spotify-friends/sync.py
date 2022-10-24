"""sync.py

Defines the synchronous API functions for this package.
"""

from datetime import datetime

import requests

from .models import AccessFields


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
    data = response.json()
    client_id = data["clientId"]
    access_token = data["accessToken"]
    expiration_dt = datetime.fromtimestamp(
        int(data["accessTokenExpirationTimestampMs"]) / 1000
    )
    is_anonymous = data["isAnonymous"]

    # Construct and return the dataclass
    return AccessFields(
        client_id=client_id,
        access_token=access_token,
        access_token_expiration=expiration_dt,
        is_anonymous=is_anonymous,
    )
