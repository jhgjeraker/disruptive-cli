import dtcli


SET_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_ids',
        flags=['device-ids'],
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='identifier of owning project',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='set_labels',
        flags=['labels'],
        help='comma-separated key=value labels',
        format=dtcli.format.str2dict,
    ),
])

REMOVE_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_ids',
        flags=['device-ids'],
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='owning project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='remove_labels',
        flags=['labels'],
        help='comma-separated label keys',
        format=dtcli.format.str2list,
    ),
])


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
    SET_ARGS.to_parser(set_parser)
    common_opts(set_parser)

    # ------------
    # Remove Label
    remove_parser = label_subparser.add_parser(
        name='remove',
        help='Remove one- or more labels.',
    )
    REMOVE_ARGS.to_parser(remove_parser)
    common_opts(remove_parser)

    return label_parser


def do(parsers: dict, cfg: dict, **kwargs):
    if kwargs['label'] == 'set':
        return dtcli.resources.device.device_label_set(cfg, **kwargs)
    elif kwargs['label'] == 'remove':
        return dtcli.resources.device.device_label_remove(cfg, **kwargs)
    else:
        print(parsers['label'].format_help())
