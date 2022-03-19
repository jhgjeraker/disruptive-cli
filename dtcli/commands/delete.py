import dtcli


def add_command(subparser, common_opts):
    delete_parser = subparser.add_parser(
        name='delete',
        help='DELETE one- or more resources.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    delete_subparser = delete_parser.add_subparsers(
        title='available commands',
        dest='delete',
        metavar=None,
    )

    return delete_parser


def do(parser, **kwargs):
    print(parser.format_help())
