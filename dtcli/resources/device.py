from typing import List

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _devices(devices: List[dt.Device], cfg: dict, **kwargs: dict) -> Table:
    table = Table(
        default_columns=[
            Column('device_id', False),
            Column('project_id', True),
            Column('display_name', False),
            Column('device_type', False),
            Column('product_number', False),
            Column('labels', True),
            Column('is_emulated', True),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(devices)
    table.new_entries(devices)

    return table


def device_get(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.device.GET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _devices(
        devices=dtcli.args.device.GET.call(
            method=dt.Device.get_device,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_list(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.device.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _devices(
        devices=dtcli.args.device.LIST.call(
            method=dt.Device.list_devices,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def _errors(errors: list, cfg: dict, **kwargs: dict) -> Table:
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('device_id', False),
            dtcli.table.Column('project_id', False),
            dtcli.table.Column('status_code', False),
            dtcli.table.Column('message', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )

    table.expand_rows(errors)
    table.new_entries(errors)

    return table


def device_transfer(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.device.TRANSFER.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _errors(
        errors=dtcli.args.device.TRANSFER.call(
            method=dt.Device.transfer_devices,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_set(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.device.LABEL_SET.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _errors(
        errors=dtcli.args.device.LABEL_SET.call(
            method=dt.Device.batch_update_labels,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_remove(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.device.LABEL_REMOVE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    return _errors(
        errors=dtcli.args.device.LABEL_REMOVE.call(
            method=dt.Device.batch_update_labels,
            method_args=args,
        ),
        cfg=cfg,
        **kwargs,
    )
