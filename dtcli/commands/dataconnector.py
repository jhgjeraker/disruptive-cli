from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def create_add(subparser: _SubParsersAction,
               common_opts: Callable,
               ) -> ArgumentParser:

    create_parser = subparser.add_parser(
        name='create',
        help='create a new data connector',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    create_subparser = create_parser.add_subparsers(
        title='available commands',
        dest='create',
        metavar=None,
    )

    # ----------------
    # create http-push
    http_push_parser = create_subparser.add_parser(
        name='http-push',
        help='create a new HTTP_PUSH data connector',
    )
    dtcli.args.dataconnector.CREATE_HTTP_PUSH.to_parser(http_push_parser)
    common_opts(http_push_parser)

    assert isinstance(create_parser, ArgumentParser)
    return create_parser


def update_add(subparser: _SubParsersAction,
               common_opts: Callable,
               ) -> ArgumentParser:

    update_parser = subparser.add_parser(
        name='update',
        help='update a data connector',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    update_subparser = update_parser.add_subparsers(
        title='available commands',
        dest='update',
        metavar=None,
    )

    # ----------------
    # update http-push
    http_push_parser = update_subparser.add_parser(
        name='http-push',
        help='update a HTTP_PUSH data connector',
    )
    dtcli.args.dataconnector.UPDATE_HTTP_PUSH.to_parser(http_push_parser)
    common_opts(http_push_parser)

    assert isinstance(update_parser, ArgumentParser)
    return update_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

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

    # -----------------
    # dataconnector get
    get_parser = dataconnector_subparser.add_parser(
        name='get',
        help='get a single data connector',
    )
    dtcli.args.dataconnector.GET.to_parser(get_parser)
    common_opts(get_parser)

    # ------------------
    # dataconnector list
    list_parser = dataconnector_subparser.add_parser(
        name='list',
        help='list data connectors in a project',
    )
    dtcli.args.dataconnector.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # --------------------
    # dataconnector create
    create_parser = create_add(
        dataconnector_subparser,
        common_opts,
    )

    # ------------------
    # dataconnector update
    update_parser = update_add(
        dataconnector_subparser,
        common_opts,
    )

    # --------------------
    # dataconnector delete
    delete_parser = dataconnector_subparser.add_parser(
        name='delete',
        help='delete a data connector',
    )
    dtcli.args.dataconnector.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # ------------------
    # dataconnector sync
    sync_parser = dataconnector_subparser.add_parser(
        name='sync',
        help='sync a data connector',
    )
    dtcli.args.dataconnector.SYNC.to_parser(sync_parser)
    common_opts(sync_parser)

    # ---------------------
    # dataconnector metrics
    metrics_parser = dataconnector_subparser.add_parser(
        name='metrics',
        help='get data connector metrics',
    )
    dtcli.args.dataconnector.SYNC.to_parser(metrics_parser)
    common_opts(metrics_parser)

    assert isinstance(create_parser, ArgumentParser)
    assert isinstance(update_parser, ArgumentParser)
    assert isinstance(dataconnector_parser, ArgumentParser)

    return {
        'dataconnector': dataconnector_parser,
        'create': create_parser,
        'update': update_parser,
    }


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['dataconnector'] == 'get':
        return dtcli.resources.dataconnector.dcon_get(cfg, **kwargs)
    elif kwargs['dataconnector'] == 'list':
        return dtcli.resources.dataconnector.dcon_list(cfg, **kwargs)
    elif kwargs['dataconnector'] == 'create':
        if kwargs['create'] == 'http-push':
            return dtcli.resources.dataconnector.\
                dcon_create_http_push(cfg, **kwargs)
        else:
            print(parsers['create'].format_help())
    elif kwargs['dataconnector'] == 'update':
        if kwargs['update'] == 'http-push':
            return dtcli.resources.dataconnector.\
                dcon_update_http_push(cfg, **kwargs)
        else:
            print(parsers['update'].format_help())
    elif kwargs['dataconnector'] == 'delete':
        return dtcli.resources.dataconnector.dcon_delete(cfg, **kwargs)
    elif kwargs['dataconnector'] == 'sync':
        return dtcli.resources.dataconnector.dcon_sync(cfg, **kwargs)
    elif kwargs['dataconnector'] == 'metrics':
        return dtcli.resources.dataconnector.dcon_metrics(cfg, **kwargs)
    else:
        print(parsers['dataconnector'].format_help())

    return Table.empty()
