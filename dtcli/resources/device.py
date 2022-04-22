import disruptive as dt

import dtcli


def _devices(devices: list[dt.Device], cfg, **kwargs):
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('device_id', False),
            dtcli.table.Column('project_id', True),
            dtcli.table.Column('display_name', False),
            dtcli.table.Column('device_type', False),
            dtcli.table.Column('product_number', False),
            dtcli.table.Column('labels', True),
            dtcli.table.Column('is_emulated', True),
        ],
        cfg=cfg,
        opts=kwargs,
    )
    table.expand_rows(devices)
    table.new_entries(devices)

    return table


def device_get(cfg, **kwargs):
    results = dtcli.arguments.device.GET.call(
        method=dt.Device.get_device,
        **kwargs,
    )

    return _devices(results, cfg, **kwargs)


def device_list(cfg, **kwargs):
    results = dtcli.arguments.device.LIST.call(
        method=dt.Device.list_devices,
        **kwargs,
    )

    return _devices(results, cfg, **kwargs)


def _errors(errors: list, cfg, **kwargs):
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


def device_transfer(cfg, **kwargs):
    return _errors(
        errors=dtcli.arguments.device.TRANSFER.call(
            method=dt.Device.transfer_devices,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_set(cfg, **kwargs):
    return _errors(
        errors=dtcli.arguments.device.LABEL_SET.call(
            method=dt.Device.batch_update_labels,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_remove(cfg, **kwargs):
    return _errors(
        errors=dtcli.arguments.device.LABEL_REMOVE.call(
            method=dt.Device.batch_update_labels,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )
