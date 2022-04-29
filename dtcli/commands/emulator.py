from typing import Callable, Any
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def publish_add(subparser: _SubParsersAction,
                common_opts: Callable,
                ) -> ArgumentParser:

    publish_parser = subparser.add_parser(
        name='publish',
        help='publish an event from the emulator device',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    publish_subparser = publish_parser.add_subparsers(
        title='available commands',
        dest='publish',
        metavar=None,
    )

    # -------------
    # publish touch
    touch_parser = publish_subparser.add_parser(
        name='touch',
        help='publish touch event',
    )
    dtcli.args.emulator.PUBLISH_TOUCH.to_parser(touch_parser)
    common_opts(touch_parser)

    assert isinstance(publish_parser, ArgumentParser)

    return publish_parser


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
    dtcli.args.emulator.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # ---------------
    # emulator delete
    delete_parser = emulator_subparser.add_parser(
        name='delete',
        help='delete an emulated device',
    )
    dtcli.args.emulator.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # ----------------
    # emulator publish
    publish_parser = publish_add(
        emulator_subparser,
        common_opts,
    )

    assert isinstance(emulator_parser, ArgumentParser)
    assert isinstance(publish_parser, ArgumentParser)

    return {'emulator': emulator_parser, 'publish': publish_parser}


def do(parsers: dict[str, ArgumentParser],
       cfg: dict,
       **kwargs: Any,
       ) -> Table:

    if kwargs['emulator'] == 'create':
        return dtcli.resources.emulator.emulator_create(cfg, **kwargs)
    elif kwargs['emulator'] == 'delete':
        return dtcli.resources.emulator.emulator_delete(cfg, **kwargs)
    elif kwargs['emulator'] == 'publish':
        if kwargs['publish'] == 'touch':
            return dtcli.resources.emulator.publish_touch(cfg, **kwargs)
        else:
            print(parsers['publish'].format_help())
    else:
        print(parsers['emulator'].format_help())

    return Table.empty()
