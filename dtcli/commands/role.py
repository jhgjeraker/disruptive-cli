import dtcli


def add(subparser, common_opts):
    role_parser = subparser.add_parser(
        name='role',
        help='Interact with the Role resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    role_subparser = role_parser.add_subparsers(
        title='available commands',
        dest='role',
        metavar=None,
    )

    return {'role': role_parser}
