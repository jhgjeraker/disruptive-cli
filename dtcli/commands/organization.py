from typing import Callable
from argparse import _SubParsersAction, ArgumentParser

import dtcli


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> dict[str, ArgumentParser]:

    organization_parser = subparser.add_parser(
        name='organization',
        help='Interact with the Organization resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    organization_subparser = organization_parser.add_subparsers(
        title='available commands',
        dest='organization',
        metavar=None,
    )

    assert isinstance(organization_parser, ArgumentParser)
    return {'organization': organization_parser}
