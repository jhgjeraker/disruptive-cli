import dtcli


def add(subparser, common_opts):
    serviceaccount_parser = subparser.add_parser(
        name='serviceaccount',
        help='Interact with the Service Account resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    serviceaccount_subparser = serviceaccount_parser.add_subparsers(
        title='available commands',
        dest='serviceaccount',
        metavar=None,
    )

    return {'serviceaccount': serviceaccount_parser}
