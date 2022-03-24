import dtcli


def add(subparser, common_opts):
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
    # Device Get
    get_parser = device_subparser.add_parser(
        name='get',
        help='Get a single device.',
    )
    get_parser.add_argument(
        'device-id',
        help='Device identifier.'
    )
    get_parser.add_argument(
        '--project-id',
        default='-',
        metavar='',
        help='Owning project identifier.'
    )
    common_opts(get_parser)

    # -----------
    # Device List
    list_parser = device_subparser.add_parser(
        name='list',
        help='Get one or more devices.',
    )
    list_parser.add_argument(
        'project-ids',
        help='Device identifier.'
    )
    list_parser.add_argument(
        '--query',
        metavar='',
        help='Keyword-based device search.',
    )
    list_parser.add_argument(
        '--device-ids',
        metavar='',
        help='Space-separated device identifiers.',
    )
    list_parser.add_argument(
        '--device-types',
        metavar='',
        help='Comma-separeted device types.',
    )
    list_parser.add_argument(
        '--label-filters',
        metavar='',
        help='Space-separated key=value labels.',
    )
    common_opts(list_parser)

    # ----------------
    # Devices Transfer
    transfer_parser = device_subparser.add_parser(
        name='transfer',
        help='Transfer one or more devices.'
    )
    transfer_parser.add_argument(
        'device-ids',
        help='Comma-separated device IDs to be transferred.',
    )
    transfer_parser.add_argument('source')
    transfer_parser.add_argument('target')
    common_opts(transfer_parser)

    # ------------
    # Device Label
    label_parser = dtcli.commands.device_label.add_command(
        device_subparser,
        common_opts,
    )

    return {'device': device_parser, 'label': label_parser}


def do(parsers: dict, cfg: dict, **kwargs):
    if kwargs['device'] == 'get':
        dtcli.resources.device.device_list(cfg, **kwargs)
    elif kwargs['device'] == 'list':
        dtcli.resources.device.device_list(cfg, **kwargs)
    elif kwargs['device'] == 'transfer':
        dtcli.resources.device.device_transfer(cfg, **kwargs)
    elif kwargs['device'] == 'label':
        dtcli.commands.device_label.do(parsers, cfg, **kwargs)
    else:
        print(parsers['device'].format_help())
