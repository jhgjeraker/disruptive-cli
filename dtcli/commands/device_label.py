import dtcli


def add_command(subparser, common_opts):
    label_parser = subparser.add_parser(
        name='label',
        help='Manipulate one- or more devices.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    label_subparser = label_parser.add_subparsers(
        title='available commands',
        dest='label',
        metavar=None,
    )

    # ---------
    # Set Label
    set_parser = label_subparser.add_parser(
        name='set',
        help='Set or update a label.',
    )
    set_parser.add_argument(
        'device-ids',
        help='Comma-separated device IDs to add labels to.',
    )
    set_parser.add_argument(
        'project-id',
        help='Identifier of project holding devices.'
    )
    set_parser.add_argument(
        'labels',
        help='Comma-separated key=value label pairs.',
    )
    common_opts(set_parser)

    # ------------
    # Remove Label
    remove_parser = label_subparser.add_parser(
        name='remove',
        help='Remove one- or more labels.',
    )
    remove_parser.add_argument(
        'device-ids',
        help='Comma-separated device IDs from which to remove labels.',
    )
    remove_parser.add_argument(
        'project-id',
        help='Identifier of project holding devices.'
    )
    remove_parser.add_argument(
        'labels',
        help='Comma-separated list of label keys to remove.',
    )
    common_opts(remove_parser)

    return label_parser


def do(parsers: dict, cfg: dict, **kwargs):
    if kwargs['label'] == 'set':
        dtcli.resources.device.device_label_set(cfg, **kwargs)
    elif kwargs['label'] == 'remove':
        dtcli.resources.device.device_label_remove(cfg, **kwargs)
    else:
        print(parsers['label'].format_help())
