import argparse
import importlib

import dtcli


def _common_opts(parser):
    table_group = parser.add_argument_group('table')
    table_group.add_argument('--full', action='store_true')
    table_group.add_argument('--no-header', action='store_true')
    table_group.add_argument('--exclude')

    format_group = parser.add_argument_group('formatting')
    format_group.add_argument('--csv', action='store_true')
    format_group.add_argument('--tsv', action='store_true')
    format_group.add_argument('--json', action='store_true')


def entry_point():
    parser = argparse.ArgumentParser(
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )

    # Create one subparser per command.
    # Global flags are provided by the _common_opts function.
    subparser = parser.add_subparsers(
        title='available commands',
        dest='command',
        metavar=None,
    )
    subs = {}
    subs['get'] = dtcli.commands.get.add_command(subparser, _common_opts)
    subs['create'] = dtcli.commands.create.add_command(subparser, _common_opts)
    subs['delete'] = dtcli.commands.delete.add_command(subparser, _common_opts)
    subs['stream'] = dtcli.commands.stream.add_command(subparser, _common_opts)
    subs['config'] = dtcli.commands.config.add_command(subparser, _common_opts)

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
    if args['command'] is not None:
        cli_init(args['command'], subs[args['command']], args)
    else:
        print(parser.format_help())


def cli_init(command: str, parser, args):
    # Load config from file if it exists.
    dtcli.cfg = dtcli.config.load_config()

    cmd_module = importlib.import_module(f'dtcli.commands.{command}')
    cmd_module.do(parser, **args)
