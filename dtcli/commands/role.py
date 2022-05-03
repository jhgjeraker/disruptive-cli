from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    role_parser = subparser.add_parser(
        name='role',
        help='Interact with the Role resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    # Note that the dest argument should usually just be "role" here.
    # The "_cmd" suffix is a result of the method get_role() having
    # an argument with the same name, "role", which overwrites
    # the key in the dictionary if not separeted. This has no effect
    # for the user as the CLI call is still "dt role get <role>".
    role_subparser = role_parser.add_subparsers(
        title='available commands',
        dest='role_cmd',
        metavar=None,
    )

    # --------
    # role get
    get_parser = role_subparser.add_parser(
        name='get',
        help='get a single role',
    )
    dtcli.args.role.GET.to_parser(get_parser)
    common_opts(get_parser)

    # ---------
    # role list
    list_parser = role_subparser.add_parser(
        name='list',
        help='list all roles',
    )
    dtcli.args.role.LIST.to_parser(list_parser)
    common_opts(list_parser)

    assert isinstance(role_parser, ArgumentParser)

    return {'role': role_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['role_cmd'] == 'get':
        return dtcli.resources.role.role_get(cfg, **kwargs)
    elif kwargs['role_cmd'] == 'list':
        return dtcli.resources.role.role_list(cfg, **kwargs)
    else:
        print(parsers['role'].format_help())

    return Table.empty()
