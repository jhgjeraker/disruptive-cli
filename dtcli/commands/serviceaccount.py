from typing import Callable, Any
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


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

    # ------------------
    # serviceaccount get
    get_parser = serviceaccount_subparser.add_parser(
        name='get',
        help='get a single service account'
    )
    dtcli.arguments.serviceaccount.GET.to_parser(get_parser)
    common_opts(get_parser)

    assert isinstance(serviceaccount_parser, ArgumentParser)

    return {'serviceaccount': serviceaccount_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['serviceaccount'] == 'get':
        return dtcli.resources.serviceaccount.get(cfg, **kwargs)
    else:
        print(parsers['serviceaccount'].format_help())

    return Table.empty()
