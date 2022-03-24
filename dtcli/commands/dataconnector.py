import dtcli


def add(subparser, common_opts):
    dataconnector_parser = subparser.add_parser(
        name='dataconnector',
        help='Interact with the Data Connector resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    dataconnector_subparser = dataconnector_parser.add_subparsers(
        title='available commands',
        dest='dataconnector',
        metavar=None,
    )

    return {'dataconnector': dataconnector_parser}
