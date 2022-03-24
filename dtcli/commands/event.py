import dtcli


def add(subparser, common_opts):
    event_parser = subparser.add_parser(
        name='event',
        help='Fetch events for one- or more devices.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    event_subparser = event_parser.add_subparsers(
        title='available commands',
        dest='event',
        metavar=None,
    )

    # -----------
    # List Events
    list_parser = event_subparser.add_parser(
        name='list',
        help='List events from one- or more devices.',
    )
    list_parser.add_argument('device-id')
    list_parser.add_argument('project-id')
    list_parser.add_argument('--event-types')
    list_parser.add_argument('--start-time')
    list_parser.add_argument('--end-time')
    common_opts(list_parser)

    # -------------
    # Stream Events
    stream_parser = event_subparser.add_parser(
        name='stream',
        help='Stream events from one- or more devices.',
    )
    stream_parser.add_argument('project-id')
    stream_parser.add_argument('--device-ids')
    stream_parser.add_argument('--label-filters')
    stream_parser.add_argument('--device-types')
    stream_parser.add_argument('--event-types')
    common_opts(stream_parser)

    return {'event': event_parser}


def do(parser, **kwargs):
    if kwargs['event'] == 'list':
        dtcli.resources.event.list_events(**kwargs)
    elif kwargs['event'] == 'stream':
        dtcli.resources.event.stream_events(**kwargs)
    else:
        print(parser.format_help())
