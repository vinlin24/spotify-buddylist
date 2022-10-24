<h1 style="text-align: center">
  spotify-buddylist
</h1>

<!-- START BADGES -->

<div style="text-align: center">
  <span>
    <img
      src="https://img.shields.io/badge/Version-0.0.0-brightgreen"
      alt="project version info"
    >
  </span>
  <span>
    <img
      src="https://img.shields.io/badge/Python-3.8%2B-blue"
      alt="supported python version"
    >
  </span>
  <span>
    <a href="https://requests.readthedocs.io/en/latest/">
      <img
        src="https://img.shields.io/badge/Dependency-requests-orange"
        alt="dependency name"
      >
    </a>
  </span>
</div>

<br>

<!-- END BADGES -->

A minimal Python version of the [spotify-buddylist](https://www.npmjs.com/package/spotify-buddylist) Node library by [valeriangalliat](https://github.com/valeriangalliat).


## Ported Features

- `getWebAccessToken` -> `get_web_access_token`
- `getFriendActivity` -> `get_friend_activity`

However, this package uses a more object-oriented approach. These functions return objects instead of raw JSON dictionaries. Data fields can then be extracted from them with familiar dot notation.


## Quickstart

```python
import spotify_buddylist as buddylist

SP_DC = "YOUR_SP_DC_COOKIE_VALUE_HERE"

creds = buddylist.get_web_access_token(SP_DC)
activities = buddylist.get_friend_activity(creds.accessToken)

for activity in activities:
    print(activity.user.name)
```


## sp_dc Cookie Instructions

<!-- TODO -->

As [designed in the original library](https://www.npmjs.com/package/spotify-buddylist#sp_dc-cookie), you only have to (annually) retrieve the value of the `sp_dc` cookie from 'spotify.com' in your browser.

<!-- TODO  -->
