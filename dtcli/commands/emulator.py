import dtcli


def add(subparser, common_opts):
    emulator_parser = subparser.add_parser(
        name='emulator',
        help='Interact with the Emulator resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    emulator_subparser = emulator_parser.add_subparsers(
        title='available commands',
        dest='emulator',
        metavar=None,
    )

    return {'emulator': emulator_parser}
