from typing import Callable, Any
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


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

    # ----------------
    # organization get
    get_parser = organization_subparser.add_parser(
        name='get',
        help='get a single organization',
    )
    dtcli.arguments.organization.GET.to_parser(get_parser)
    common_opts(get_parser)

    assert isinstance(organization_parser, ArgumentParser)

    return {'organization': organization_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['organization'] == 'get':
        return dtcli.resources.organization.get(cfg, **kwargs)
    else:
        print(parsers['organization'].format_help())

    return Table.empty()
