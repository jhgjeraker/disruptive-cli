from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def key_add(subparser: _SubParsersAction,
            common_opts: Callable,
            ) -> ArgumentParser:

    key_parser = subparser.add_parser(
        name='key',
        help='interact with service account keys',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    key_subparser = key_parser.add_subparsers(
        title='available commands',
        dest='service_account_key',
        metavar=None,
    )

    # -------
    # key get
    get_parser = key_subparser.add_parser(
        name='get',
        help='get a service account key',
    )
    dtcli.args.service_account.KEY_GET.to_parser(get_parser)
    common_opts(get_parser)

    # --------
    # key list
    list_parser = key_subparser.add_parser(
        name='list',
        help='list all service account keys',
    )
    dtcli.args.service_account.KEY_LIST.to_parser(list_parser)
    common_opts(list_parser)

    # ----------
    # key create
    create_parser = key_subparser.add_parser(
        name='create',
        help='create a new service account key',
    )
    dtcli.args.service_account.KEY_CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # ----------
    # key delete
    delete_parser = key_subparser.add_parser(
        name='delete',
        help='delete a service account key',
    )
    dtcli.args.service_account.KEY_DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    assert isinstance(key_parser, ArgumentParser)

    return key_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    service_account_parser = subparser.add_parser(
        name='service-account',
        help='interact with your service accounts',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    service_account_subparser = service_account_parser.add_subparsers(
        title='available commands',
        dest='service-account',
        metavar=None,
    )

    # ------------------
    # service-account get
    get_parser = service_account_subparser.add_parser(
        name='get',
        help='get a single service account'
    )
    dtcli.args.service_account.GET.to_parser(get_parser)
    common_opts(get_parser)

    # -------------------
    # service-account list
    list_parser = service_account_subparser.add_parser(
        name='list',
        help='list all service accounts in project'
    )
    dtcli.args.service_account.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # ---------------------
    # service-account create
    create_parser = service_account_subparser.add_parser(
        name='create',
        help='create a new service account'
    )
    dtcli.args.service_account.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # ---------------------
    # service-account update
    update_parser = service_account_subparser.add_parser(
        name='update',
        help='update a service account'
    )
    dtcli.args.service_account.UPDATE.to_parser(update_parser)
    common_opts(update_parser)

    # ---------------------
    # service-account delete
    delete_parser = service_account_subparser.add_parser(
        name='delete',
        help='delete a service account'
    )
    dtcli.args.service_account.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # --------------
    # project member
    key_parser = key_add(
        service_account_subparser,
        common_opts,
    )

    assert isinstance(key_parser, ArgumentParser)
    assert isinstance(service_account_parser, ArgumentParser)

    return {
        'service_account': service_account_parser,
        'service_account_key': key_parser,
    }


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['service_account'] == 'get':
        return dtcli.resources.service_account.sa_get(cfg, **kwargs)
    elif kwargs['service_account'] == 'list':
        return dtcli.resources.service_account.sa_list(cfg, **kwargs)
    elif kwargs['service_account'] == 'create':
        return dtcli.resources.service_account.sa_create(cfg, **kwargs)
    elif kwargs['service_account'] == 'update':
        return dtcli.resources.service_account.sa_update(cfg, **kwargs)
    elif kwargs['service_account'] == 'delete':
        return dtcli.resources.service_account.sa_delete(cfg, **kwargs)
    elif kwargs['service_account'] == 'key':
        if kwargs['service_account_key'] == 'get':
            return dtcli.resources.service_account.sa_key_get(cfg, **kwargs)
        elif kwargs['service_account_key'] == 'list':
            return dtcli.resources.service_account.sa_key_list(cfg, **kwargs)
        elif kwargs['service_account_key'] == 'create':
            return dtcli.resources.service_account.sa_key_create(cfg, **kwargs)
        elif kwargs['service_account_key'] == 'delete':
            return dtcli.resources.service_account.sa_key_delete(cfg, **kwargs)
        else:
            print(parsers['service_account_key'].format_help())
    else:
        print(parsers['service_account'].format_help())

    return Table.empty()
