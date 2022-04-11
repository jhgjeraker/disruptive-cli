import dtcli


GET_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        xid=True,
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['--project-id'],
        xid=True,
        metavar='',
        format=dtcli.format.to_string,
    )
])

LIST_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        xid=True,
        help='identifier of owning project',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='query',
        flags=['--query'],
        help='keyword-based device search',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='device_ids',
        flags=['--device-ids'],
        metavar='',
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='device_types',
        flags=['--device-types'],
        metavar='',
        help='comma-separated device types',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='label_filters',
        flags=['--label-filters'],
        metavar='',
        help='comma-separated key=value labels',
        format=dtcli.format.to_string,
    )
])

TRANSFER_ARGS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_ids',
        flags=['device-ids'],
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='source_project_id',
        flags=['source-project-id'],
        help='source project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='target_project_id',
        flags=['target-project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])


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
    # device get
    get_parser = device_subparser.add_parser(
        name='get',
        help='Get a single device.',
    )
    GET_ARGS.to_parser(get_parser)
    common_opts(get_parser)

    # -----------
    # Device List
    list_parser = device_subparser.add_parser(
        name='list',
        help='Get one or more devices.',
    )
    LIST_ARGS.to_parser(list_parser)
    common_opts(list_parser)

    # ----------------
    # Devices Transfer
    transfer_parser = device_subparser.add_parser(
        name='transfer',
        help='Transfer one or more devices.'
    )
    TRANSFER_ARGS.to_parser(transfer_parser)
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
        dtcli.resources.device.device_get(cfg, **kwargs)
    elif kwargs['device'] == 'list':
        dtcli.resources.device.device_list(cfg, **kwargs)
    elif kwargs['device'] == 'transfer':
        dtcli.resources.device.device_transfer(cfg, **kwargs)
    elif kwargs['device'] == 'label':
        dtcli.commands.device_label.do(parsers, cfg, **kwargs)
    else:
        print(parsers['device'].format_help())
