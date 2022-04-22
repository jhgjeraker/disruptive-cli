from typing import Callable
from argparse import _SubParsersAction, ArgumentParser

import dtcli


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> dict[str, ArgumentParser]:

    serviceaccount_parser = subparser.add_parser(
        name='serviceaccount',
        help='Interact with the Service Account resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    serviceaccount_subparser = serviceaccount_parser.add_subparsers(
        title='available commands',
        dest='serviceaccount',
        metavar=None,
    )

    assert isinstance(serviceaccount_parser, ArgumentParser)

    return {'serviceaccount': serviceaccount_parser}
