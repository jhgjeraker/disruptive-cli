from typing import Callable, Any
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> dict[str, ArgumentParser]:

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

    # ------------------
    # serviceaccount get
    get_parser = serviceaccount_subparser.add_parser(
        name='get',
        help='get a single service account'
    )
    dtcli.args.serviceaccount.GET.to_parser(get_parser)
    common_opts(get_parser)

    # -------------------
    # serviceaccount list
    list_parser = serviceaccount_subparser.add_parser(
        name='list',
        help='list all service accounts in project'
    )
    dtcli.args.serviceaccount.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # ---------------------
    # serviceaccount create
    create_parser = serviceaccount_subparser.add_parser(
        name='create',
        help='create a new service account'
    )
    dtcli.args.serviceaccount.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # ---------------------
    # serviceaccount update
    update_parser = serviceaccount_subparser.add_parser(
        name='update',
        help='update a service account'
    )
    dtcli.args.serviceaccount.UPDATE.to_parser(update_parser)
    common_opts(update_parser)

    # ---------------------
    # serviceaccount delete
    delete_parser = serviceaccount_subparser.add_parser(
        name='delete',
        help='delete a service account'
    )
    dtcli.args.serviceaccount.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    assert isinstance(serviceaccount_parser, ArgumentParser)

    return {'serviceaccount': serviceaccount_parser}


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['serviceaccount'] == 'get':
        return dtcli.resources.serviceaccount.sa_get(cfg, **kwargs)
    elif kwargs['serviceaccount'] == 'list':
        return dtcli.resources.serviceaccount.sa_list(cfg, **kwargs)
    elif kwargs['serviceaccount'] == 'create':
        return dtcli.resources.serviceaccount.sa_create(cfg, **kwargs)
    elif kwargs['serviceaccount'] == 'update':
        return dtcli.resources.serviceaccount.sa_update(cfg, **kwargs)
    elif kwargs['serviceaccount'] == 'delete':
        return dtcli.resources.serviceaccount.sa_delete(cfg, **kwargs)
    else:
        print(parsers['serviceaccount'].format_help())

    return Table.empty()
