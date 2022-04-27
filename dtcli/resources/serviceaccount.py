from typing import Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _service_accounts(service_accounts: list[dt.ServiceAccount],
                      cfg: dict,
                      **kwargs: Any,
                      ) -> Table:

    table = Table(
        default_columns=[
            Column('service_account_id', False),
            Column('display_name', False),
            Column('basic_auth_enabled', False),
            Column('email', False),
            Column('create_time', True),
            Column('update_time', True),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(service_accounts)
    table.new_entries(service_accounts)

    return table


def get(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.serviceaccount.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _service_accounts(
        service_accounts=dtcli.arguments.serviceaccount.GET.call(
            method=dt.ServiceAccount.get_service_account,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )
