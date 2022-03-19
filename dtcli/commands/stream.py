import dtcli


def add_command(subparser, common_opts):
    stream_parser = subparser.add_parser(
        name='stream',
        help='Stream events from one- or more devices.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    stream_subparser = stream_parser.add_subparsers(
        title='available commands',
        dest='stream',
        metavar=None,
    )

    # ----------
    # GET Device
    stream_events_parser = stream_subparser.add_parser(
        name='events',
        help='Stream events from one- or more devices.',
    )
    stream_events_parser.add_argument('project-id')
    stream_events_parser.add_argument('--device-ids')
    stream_events_parser.add_argument('--label-filters')
    stream_events_parser.add_argument('--device-types')
    stream_events_parser.add_argument('--event-types')
    common_opts(stream_events_parser)

    return stream_parser


def do(parser, **kwargs):
    if kwargs['stream'] == 'events':
        dtcli.resources.stream.stream_events(**kwargs)
    else:
        print(parser.format_help())
