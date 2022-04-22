from typing import Callable
from argparse import _SubParsersAction, ArgumentParser

import dtcli


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> dict[str, ArgumentParser]:

    role_parser = subparser.add_parser(
        name='role',
        help='Interact with the Role resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    role_subparser = role_parser.add_subparsers(
        title='available commands',
        dest='role',
        metavar=None,
    )

    assert isinstance(role_parser, ArgumentParser)

    return {'role': role_parser}
