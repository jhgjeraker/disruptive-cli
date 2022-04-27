from typing import Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _dataconnectors(dataconnectors: list[dt.DataConnector],
                    cfg: dict,
                    **kwargs: Any,
                    ) -> Table:

    table = Table(
        default_columns=[
            Column('data_connector_id', False),
            Column('display_name', False),
            Column('data_connector_type', False),
            Column('status', False),
            Column('project_id', True),
            Column('event_types', True),
            Column('labels', True),
            Column('config', True),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(dataconnectors)
    table.new_entries(dataconnectors)

    return table


def _metrics(metrics: list[dt.DataConnector],
             cfg: dict,
             **kwargs: Any,
             ) -> Table:

    table = Table(
        default_columns=[
            Column('success_count', False),
            Column('error_count', False),
            Column('latency', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(metrics)
    table.new_entries(metrics)

    return table


def dcon_get(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _dataconnectors(
        dataconnectors=dtcli.arguments.dataconnector.GET.call(
            method=dt.DataConnector.get_data_connector,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_list(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _dataconnectors(
        dataconnectors=dtcli.arguments.dataconnector.LIST.call(
            method=dt.DataConnector.list_data_connectors,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_create_http_push(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.CREATE_HTTP_PUSH.reparse(**kwargs)
    if not ok:
        return Table.empty()

    args['config'] = dt.DataConnector.HttpPushConfig(
        url=args['url'],
        signature_secret=args['signature_secret'],
        headers=args['headers'],
    )

    # Since `args` is propegated as **kwargs into
    # the `disruptive` package, `url` and `headers`
    # must be removed to avoid conflict with request.
    args.pop('url')
    args.pop('headers')

    return _dataconnectors(
        dataconnectors=dtcli.arguments.dataconnector.CREATE_HTTP_PUSH.call(
            method=dt.DataConnector.create_data_connector,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_update_http_push(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.UPDATE_HTTP_PUSH.reparse(**kwargs)
    if not ok:
        return Table.empty()

    args['config'] = dt.DataConnector.HttpPushConfig(
        url=args['url'],
        signature_secret=args['signature_secret'],
        headers=args['headers'],
    )

    # Since `args` is propegated as **kwargs into
    # the `disruptive` package, `url` and `headers`
    # must be removed to avoid conflict with request.
    args.pop('url')
    args.pop('headers')

    return _dataconnectors(
        dataconnectors=dtcli.arguments.dataconnector.UPDATE_HTTP_PUSH.call(
            method=dt.DataConnector.update_data_connector,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_delete(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.DELETE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.arguments.dataconnector.DELETE.call(
        method=dt.DataConnector.delete_data_connector,
        method_args=args,
    )

    return Table.empty()


def dcon_sync(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.SYNC.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.arguments.dataconnector.SYNC.call(
        method=dt.DataConnector.sync_data_connector,
        method_args=args,
    )

    return Table.empty()


def dcon_metrics(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.dataconnector.METRICS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _metrics(
        metrics=dtcli.arguments.dataconnector.METRICS.call(
            method=dt.DataConnector.get_metrics,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )
