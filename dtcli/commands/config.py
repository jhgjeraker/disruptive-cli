from typing import Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def add(subparser: _SubParsersAction) -> Dict[str, ArgumentParser]:
    config_parser = subparser.add_parser(
        name='config',
        help='configure CLI behavior',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    config_subparser = config_parser.add_subparsers(
        title='available commands',
        dest='config',
        metavar=None,
    )

    # --------------
    # config default
    config_subparser.add_parser(
        name='default',
        help='generate default config file'
    )

    # --------------
    # config padding
    padding_parser = config_subparser.add_parser(
        name='padding',
        help='set table column padding',
    )
    dtcli.args.config.PADDING.to_parser(padding_parser)

    assert isinstance(config_parser, ArgumentParser)
    return {'config': config_parser}


def do(parsers: dict, cfg: dict, **kwargs: dict) -> Table:
    if kwargs['config'] == 'default':
        return dtcli.resources.config.set_default()
    elif kwargs['config'] == 'padding':
        return dtcli.resources.config.set_padding(**kwargs)
    else:
        print(parsers['config'].format_help())
        return Table.empty()
