import dtcli


def add(subparser, common_opts):
    organization_parser = subparser.add_parser(
        name='organization',
        help='Interact with the Organization resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    organization_subparser = organization_parser.add_subparsers(
        title='available commands',
        dest='organization',
        metavar=None,
    )

    return {'organization': organization_parser}
