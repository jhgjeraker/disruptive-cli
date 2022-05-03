from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def label_add(subparser: _SubParsersAction,
              common_opts: Callable,
              ) -> ArgumentParser:

    label_parser = subparser.add_parser(
        name='label',
        help='configure labels for one or more devices',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    label_subparser = label_parser.add_subparsers(
        title='available commands',
        dest='label',
        metavar=None,
    )

    # ---------
    # label set
    set_parser = label_subparser.add_parser(
        name='set',
        help='set or update a label',
    )
    dtcli.args.device.LABEL_SET.to_parser(set_parser)
    common_opts(set_parser)

    # ------------
    # label remove
    remove_parser = label_subparser.add_parser(
        name='remove',
        help='remove one or more labels',
    )
    dtcli.args.device.LABEL_REMOVE.to_parser(remove_parser)
    common_opts(remove_parser)

    assert isinstance(label_parser, ArgumentParser)

    return label_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    device_parser = subparser.add_parser(
        name='device',
        help='Interact with the Device resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    device_subparser = device_parser.add_subparsers(
        title='available commands',
        dest='device',
        metavar=None,
    )

    # ----------
    # device get
    get_parser = device_subparser.add_parser(
        name='get',
        help='Get a single device.',
    )
    dtcli.args.device.GET.to_parser(get_parser)
    common_opts(get_parser)

    # -----------
    # Device List
    list_parser = device_subparser.add_parser(
        name='list',
        help='Get one or more devices.',
    )
    dtcli.args.device.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # ----------------
    # Devices Transfer
    transfer_parser = device_subparser.add_parser(
        name='transfer',
        help='Transfer one or more devices.'
    )
    dtcli.args.device.TRANSFER.to_parser(transfer_parser)
    common_opts(transfer_parser)

    # ------------
    # Device Label
    label_parser = label_add(
        device_subparser,
        common_opts,
    )

    assert isinstance(device_parser, ArgumentParser)
    assert isinstance(label_parser, ArgumentParser)

    return {'device': device_parser, 'label': label_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['device'] == 'get':
        return dtcli.resources.device.device_get(cfg, **kwargs)
    elif kwargs['device'] == 'list':
        return dtcli.resources.device.device_list(cfg, **kwargs)
    elif kwargs['device'] == 'transfer':
        return dtcli.resources.device.device_transfer(cfg, **kwargs)
    elif kwargs['device'] == 'label':
        if kwargs['label'] == 'set':
            return dtcli.resources.device.device_label_set(cfg, **kwargs)
        elif kwargs['label'] == 'remove':
            return dtcli.resources.device.device_label_remove(cfg, **kwargs)
        else:
            print(parsers['label'].format_help())
    else:
        print(parsers['device'].format_help())

    return Table.empty()
