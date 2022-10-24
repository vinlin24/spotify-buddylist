# spotify-friends

Python: 3.8+

A minimal Python version of the [spotify-buddylist](https://www.npmjs.com/package/spotify-buddylist) Node library by [valeriangalliat](https://github.com/valeriangalliat).

## Ported Features

- `getWebAccessToken` -> `get_web_access_token`
- `getFriendActivity` -> `get_friend_activity`

However, `get_friend_activity` now has the option to return the data as a `list` of `FriendActivity` objects instead of raw JSON.

## sp_dc Cookie Instructions

<!-- TODO -->

As [designed in the original library](https://www.npmjs.com/package/spotify-buddylist#sp_dc-cookie), you only have to (annually) retrieve the value of the `sp_dc` cookie from spotify.com in your browser.

<!-- TODO  -->
