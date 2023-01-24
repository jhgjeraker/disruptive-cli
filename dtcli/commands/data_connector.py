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
        help='create a new http-push data connector',
    )
    dtcli.args.data_connector.CREATE_HTTP_PUSH.to_parser(http_push_parser)
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
        help='update a http-push data connector',
    )
    dtcli.args.data_connector.UPDATE_HTTP_PUSH.to_parser(http_push_parser)
    common_opts(http_push_parser)

    assert isinstance(update_parser, ArgumentParser)
    return update_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    data_connector_parser = subparser.add_parser(
        name='data-connector',
        help='interact with your data connectors',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    data_connector_subparser = data_connector_parser.add_subparsers(
        title='available commands',
        dest='data-connector',
        metavar=None,
    )

    # -----------------
    # data-connector get
    get_parser = data_connector_subparser.add_parser(
        name='get',
        help='get a single data connector',
    )
    dtcli.args.data_connector.GET.to_parser(get_parser)
    common_opts(get_parser)

    # ------------------
    # data-connector list
    list_parser = data_connector_subparser.add_parser(
        name='list',
        help='list data connectors in a project',
    )
    dtcli.args.data_connector.LIST.to_parser(list_parser)
    common_opts(list_parser)

    # --------------------
    # data-connector create
    create_parser = create_add(
        data_connector_subparser,
        common_opts,
    )

    # ------------------
    # data-connector update
    update_parser = update_add(
        data_connector_subparser,
        common_opts,
    )

    # --------------------
    # data-connector delete
    delete_parser = data_connector_subparser.add_parser(
        name='delete',
        help='delete a data connector',
    )
    dtcli.args.data_connector.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # ------------------
    # data-connector sync
    sync_parser = data_connector_subparser.add_parser(
        name='sync',
        help='sync a data connector',
    )
    dtcli.args.data_connector.SYNC.to_parser(sync_parser)
    common_opts(sync_parser)

    # ---------------------
    # data-connector metrics
    metrics_parser = data_connector_subparser.add_parser(
        name='metrics',
        help='get data connector metrics',
    )
    dtcli.args.data_connector.SYNC.to_parser(metrics_parser)
    common_opts(metrics_parser)

    assert isinstance(create_parser, ArgumentParser)
    assert isinstance(update_parser, ArgumentParser)
    assert isinstance(data_connector_parser, ArgumentParser)

    return {
        'data_connector': data_connector_parser,
        'create': create_parser,
        'update': update_parser,
    }


def do(parsers: dict, cfg: dict, **kwargs: Any) -> Table:
    if kwargs['data_connector'] == 'get':
        return dtcli.resources.data_connector.dcon_get(cfg, **kwargs)
    elif kwargs['data_connector'] == 'list':
        return dtcli.resources.data_connector.dcon_list(cfg, **kwargs)
    elif kwargs['data_connector'] == 'create':
        if kwargs['create'] == 'http-push':
            return dtcli.resources.data_connector.\
                dcon_create_http_push(cfg, **kwargs)
        else:
            print(parsers['create'].format_help())
    elif kwargs['data_connector'] == 'update':
        if kwargs['update'] == 'http-push':
            return dtcli.resources.data_connector.\
                dcon_update_http_push(cfg, **kwargs)
        else:
            print(parsers['update'].format_help())
    elif kwargs['data_connector'] == 'delete':
        return dtcli.resources.data_connector.dcon_delete(cfg, **kwargs)
    elif kwargs['data_connector'] == 'sync':
        return dtcli.resources.data_connector.dcon_sync(cfg, **kwargs)
    elif kwargs['data_connector'] == 'metrics':
        return dtcli.resources.data_connector.dcon_metrics(cfg, **kwargs)
    else:
        print(parsers['data_connector'].format_help())

    return Table.empty()
