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


def sa_get(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.serviceaccount.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _service_accounts(
        service_accounts=dtcli.args.serviceaccount.GET.call(
            method=dt.ServiceAccount.get_service_account,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def sa_list(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.serviceaccount.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _service_accounts(
        service_accounts=dtcli.args.serviceaccount.LIST.call(
            method=dt.ServiceAccount.list_service_accounts,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def sa_create(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.serviceaccount.CREATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _service_accounts(
        service_accounts=dtcli.args.serviceaccount.CREATE.call(
            method=dt.ServiceAccount.create_service_account,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def sa_update(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.serviceaccount.UPDATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _service_accounts(
        service_accounts=dtcli.args.serviceaccount.UPDATE.call(
            method=dt.ServiceAccount.update_service_account,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def sa_delete(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.serviceaccount.DELETE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.serviceaccount.DELETE.call(
        method=dt.ServiceAccount.delete_service_account,
        method_args=args,
    )

    return Table.empty()
