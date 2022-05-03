from typing import Any, List

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _roles(roles: List[dt.Organization],
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


def role_get(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.role.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _roles(
        roles=dtcli.args.role.GET.call(
            method=dt.Role.get_role,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def role_list(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.role.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _roles(
        roles=dtcli.args.role.LIST.call(
            method=dt.Role.list_roles,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )
