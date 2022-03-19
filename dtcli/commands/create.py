import dtcli


def add_command(subparser, common_opts):
    create_parser = subparser.add_parser(
        name='create',
        help='CREATE one- or more resources.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    create_subparser = create_parser.add_subparsers(
        title='available commands',
        dest='create',
        metavar=None,
    )

    return create_parser


def do(parser, **kwargs):
    print(parser.format_help())
