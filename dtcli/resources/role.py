from typing import Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _roles(roles: list[dt.Organization],
           cfg: dict,
           **kwargs: Any,
           ) -> Table:

    table = Table(
        default_columns=[
            Column('role', False),
            Column('display_name', False),
            Column('description', False),
            Column('permissions', True),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(roles)
    table.new_entries(roles)

    return table


def get(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.role.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _roles(
        roles=dtcli.arguments.role.GET.call(
            method=dt.Role.get_role,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )
