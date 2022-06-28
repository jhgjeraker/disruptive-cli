from typing import Any, List

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _dataconnectors(dataconnectors: List[dt.DataConnector],
                    cfg: dict,
                    **kwargs: Any,
                    ) -> Table:

    table = Table(
        default_columns=[
            Column('data_connector_id', False),
            Column('project_id', False),
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


def _metrics(metrics: List[dt.DataConnector],
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
    ok, args = dtcli.args.dataconnector.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _dataconnectors(
        dataconnectors=dtcli.args.dataconnector.GET.call(
            method=dt.DataConnector.get_data_connector,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_list(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.dataconnector.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _dataconnectors(
        dataconnectors=dtcli.args.dataconnector.LIST.call(
            method=dt.DataConnector.list_data_connectors,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_create_http_push(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.dataconnector.CREATE_HTTP_PUSH.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of HttpPushConfig that is injected into args.
    http_push_config_args = {}
    for key in ['url', 'signature_secret', 'headers']:
        if key in args:
            http_push_config_args[key] = args[key]
            args.pop(key)
    args['config'] = dt.DataConnector.HttpPushConfig(**http_push_config_args)

    return _dataconnectors(
        dataconnectors=dtcli.args.dataconnector.CREATE_HTTP_PUSH.call(
            method=dt.DataConnector.create_data_connector,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_update_http_push(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.dataconnector.UPDATE_HTTP_PUSH.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of HttpPushConfig that is injected into args.
    http_push_config_args = {}
    for key in ['url', 'signature_secret', 'headers']:
        if key in args:
            http_push_config_args[key] = args[key]
            args.pop(key)
    args['config'] = dt.DataConnector.HttpPushConfig(**http_push_config_args)

    return _dataconnectors(
        dataconnectors=dtcli.args.dataconnector.UPDATE_HTTP_PUSH.call(
            method=dt.DataConnector.update_data_connector,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def dcon_delete(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.dataconnector.DELETE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.dataconnector.DELETE.call(
        method=dt.DataConnector.delete_data_connector,
        method_args=args,
    )

    return Table.empty()


def dcon_sync(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.dataconnector.SYNC.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.dataconnector.SYNC.call(
        method=dt.DataConnector.sync_data_connector,
        method_args=args,
    )

    return Table.empty()


def dcon_metrics(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.dataconnector.METRICS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _metrics(
        metrics=dtcli.args.dataconnector.METRICS.call(
            method=dt.DataConnector.get_metrics,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )
