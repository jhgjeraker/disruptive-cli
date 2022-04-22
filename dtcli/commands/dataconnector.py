from typing import Callable
from argparse import _SubParsersAction, ArgumentParser

import dtcli


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> dict[str, ArgumentParser]:

    dataconnector_parser = subparser.add_parser(
        name='dataconnector',
        help='Interact with the Data Connector resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    dataconnector_subparser = dataconnector_parser.add_subparsers(
        title='available commands',
        dest='dataconnector',
        metavar=None,
    )

    # -----------------
    # dataconnector get
    get_parser = dataconnector_subparser.add_parser(
        name='get',
        help='get a single data connector',
    )
    common_opts(get_parser)

    assert isinstance(dataconnector_parser, ArgumentParser)
    return {'dataconnector': dataconnector_parser}
