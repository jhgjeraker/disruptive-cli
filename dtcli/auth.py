import sys

import dtcli
import disruptive


def auth():
    # Attempt to authenticate immediately.
    try:
        disruptive.default_auth.refresh()
    except disruptive.errors.Unauthorized:
        dtcli.output.stderr('Unauthorized')
        sys.exit(1)
