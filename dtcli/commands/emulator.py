from typing import Callable, Any
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> dict[str, ArgumentParser]:

    emulator_parser = subparser.add_parser(
        name='emulator',
        help='Interact with the Emulator resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    emulator_subparser = emulator_parser.add_subparsers(
        title='available commands',
        dest='emulator',
        metavar=None,
    )

    # ---------------
    # emulator create
    create_parser = emulator_subparser.add_parser(
        name='create',
        help='create a new emulated device',
    )
    dtcli.arguments.emulator.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    assert isinstance(emulator_parser, ArgumentParser)
    return {'emulator': emulator_parser}


def do(parsers: dict[str, ArgumentParser],
       cfg: dict,
       **kwargs: Any,
       ) -> Table:

    if kwargs['emulator'] == 'create':
        return dtcli.resources.emulator.emulator_create(cfg, **kwargs)
    else:
        print(parsers['emulator'].format_help())

    return Table.empty()
