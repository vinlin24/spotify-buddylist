"""test_readme.py

Test the code snippet in README.md.
"""

import os

import dotenv

dotenv.load_dotenv(override=True)
SP_DC = os.environ["SPOTIFY_SP_DC_COOKIE"]

# Make this programmatic and not hard-coded later
SNIPPET = """\
import spotify_buddylist as buddylist

SP_DC = "YOUR_SP_DC_COOKIE_VALUE_HERE"

creds = buddylist.get_web_access_token(SP_DC)
activities = buddylist.get_friend_activity(creds.accessToken)

for activity in activities:
    print(activity.user.name)
"""


def test_snippet(capsys) -> None:
    """Test the code snippet in README.md"""
    snippet = SNIPPET.replace("YOUR_SP_DC_COOKIE_VALUE_HERE", SP_DC)
    # pylint: disable-next=exec-used
    exec(snippet)
    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert len(stdout.split("\n")) > 1
