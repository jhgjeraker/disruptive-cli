from typing import Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _organizations(organizations: list[dt.Organization],
                   cfg: dict,
                   **kwargs: Any,
                   ) -> Table:

    table = Table(
        default_columns=[
            Column('organization_id', False),
            Column('display_name', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(organizations)
    table.new_entries(organizations)

    return table


def get(cfg: dict, **kwargs: Any) -> Table:
    return _organizations(
        organizations=dtcli.arguments.organization.GET.call(
            method=dt.Organization.get_organization,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )
