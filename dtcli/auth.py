import sys

import dtcli
import disruptive


def auth() -> None:
    # Attempt to authenticate immediately.
    try:
        disruptive.default_auth.refresh()
    except disruptive.errors.Unauthorized:
        dtcli.format.stderr('Unauthorized')
        sys.exit(1)
