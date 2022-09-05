import argparse
from argparse import ArgumentParser
import importlib

import dtcli
from dtcli.table import Table


def _common_opts(parser: ArgumentParser) -> None:
    table_group = parser.add_argument_group('behavior')
    table_group.add_argument(
        '-i', '--interactive',
        action='store_true',
        help='Enabled interactive mode if available.',
    )
    table_group = parser.add_argument_group('table')
    table_group.add_argument(
        '--include',
        metavar='',
        help='Exclusively include named columns.',
    )
    table_group.add_argument(
        '--full',
        action='store_true',
        help='Show all available columns.',
    )
    table_group.add_argument(
        '--no-header',
        action='store_true',
        help='Excludes table header from output.',
    )

    format_group = parser.add_argument_group('formatting')
    format_group.add_argument(
        '--csv',
        action='store_true',
        help='Output formatted as comma-separated values.',
    )
    format_group.add_argument(
        '--tsv',
        action='store_true',
        help='Output formatted as tab-separated values.',
    )
    format_group.add_argument(
        '--json',
        action='store_true',
        help='Output formatted as individual JSON entries.',
    )


def cli_init(parsers: dict, args: dict) -> Table:
    # Load config from file if it exists.
    cfg = dtcli.resources.config.load_config()

    # Import the command module.
    m = importlib.import_module(f'dtcli.commands.{args["command"]}')

    # Execute the command.
    table = m.do(parsers, cfg, **args)

    assert isinstance(table, Table)

    return table


def main() -> Table:
    parser = argparse.ArgumentParser(
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    parser.add_argument(
        '-V', '--version',
        help='print current version',
        action='store_true',
    )

    # Create one subparser per command.
    # Global flags are provided by the _common_opts function.
    subparser = parser.add_subparsers(
        title='available commands',
        dest='command',
        metavar=None,
    )

    parsers = {}
    parsers.update(dtcli.commands.device.add(subparser, _common_opts))
    parsers.update(dtcli.commands.dataconnector.add(subparser, _common_opts))
    parsers.update(dtcli.commands.project.add(subparser, _common_opts))
    parsers.update(dtcli.commands.organization.add(subparser, _common_opts))
    parsers.update(dtcli.commands.serviceaccount.add(subparser, _common_opts))
    parsers.update(dtcli.commands.role.add(subparser, _common_opts))
    parsers.update(dtcli.commands.event.add(subparser, _common_opts))
    parsers.update(dtcli.commands.emulator.add(subparser, _common_opts))
    parsers.update(dtcli.commands.claim.add(subparser, _common_opts))

    # Add configuration parsers.
    parsers.update(dtcli.commands.config.add(subparser))

    _common_opts(parser)

    # Finally, once the parser and subparsers are constructed, build the
    # output dictionary of arguments which we will use for executing functions.
    args = vars(parser.parse_args())

    # Also, for some reason, argparse converts all argument-dashes (-) to
    # underscore, **except** for positional arguments. There is probably a
    # good reason for this, but it is one I do not need. For constistency's
    # sake, I convert them all to underscore myself.
    args = dtcli.format.args_replace_dash(args)

    # The initialization phase is wrapped in a general function cli_init().
    # This is mainly to avoid running the auth-sequence when no command
    # is provided, but also separates the setup from actual cli executions.
    if args['version']:
        dtcli.format.stdout(dtcli.__VERSION__)
    elif args['command'] is not None:
        return cli_init(parsers, args)
    else:
        print(parser.format_help())

    return Table.empty()


def entry_point() -> None:
    main()
