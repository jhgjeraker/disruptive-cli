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


def get(cfg: dict, **kwargs: Any) -> Table:
    return _dataconnectors(
        dataconnectors=dtcli.arguments.dataconnector.GET.call(
            method=dt.DataConnector.get_data_connector,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def list(cfg: dict, **kwargs: Any) -> Table:
    return _dataconnectors(
        dataconnectors=dtcli.arguments.dataconnector.LIST.call(
            method=dt.DataConnector.list_data_connectors,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )
