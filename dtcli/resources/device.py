import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _devices(devices: list[dt.Device], cfg: dict, **kwargs: dict) -> Table:
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
    results = dtcli.arguments.device.GET.call(
        method=dt.Device.get_device,
        **kwargs,
    )

    return _devices(results, cfg, **kwargs)


def device_list(cfg: dict, **kwargs: dict) -> Table:
    results = dtcli.arguments.device.LIST.call(
        method=dt.Device.list_devices,
        **kwargs,
    )

    return _devices(results, cfg, **kwargs)


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
    return _errors(
        errors=dtcli.arguments.device.TRANSFER.call(
            method=dt.Device.transfer_devices,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_set(cfg: dict, **kwargs: dict) -> Table:
    return _errors(
        errors=dtcli.arguments.device.LABEL_SET.call(
            method=dt.Device.batch_update_labels,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_remove(cfg: dict, **kwargs: dict) -> Table:
    return _errors(
        errors=dtcli.arguments.device.LABEL_REMOVE.call(
            method=dt.Device.batch_update_labels,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )
