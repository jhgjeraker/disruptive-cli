from typing import Callable, Any
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


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
    dtcli.arguments.dataconnector.GET.to_parser(get_parser)
    common_opts(get_parser)

    # ------------------
    # dataconnector list
    list_parser = dataconnector_subparser.add_parser(
        name='list',
        help='list data connectors in a project',
    )
    dtcli.arguments.dataconnector.LIST.to_parser(list_parser)
    common_opts(list_parser)

    assert isinstance(dataconnector_parser, ArgumentParser)

    return {'dataconnector': dataconnector_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['dataconnector'] == 'get':
        return dtcli.resources.dataconnector.get(cfg, **kwargs)
    elif kwargs['dataconnector'] == 'list':
        return dtcli.resources.dataconnector.list(cfg, **kwargs)
    else:
        print(parsers['dataconnector'].format_help())

    return Table.empty()
