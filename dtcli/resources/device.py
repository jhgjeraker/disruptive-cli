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


def device_get(cfg, **kwargs) -> None:
    results = dtcli.commands.device.GET_ARGS.call(
        method=dt.Device.get_device,
        **kwargs,
    )

    _devices(results, cfg, **kwargs)


def device_list(cfg, **kwargs) -> None:
    results = dtcli.commands.device.LIST_ARGS.call(
        method=dt.Device.list_devices,
        **kwargs,
    )

    _devices(results, cfg, **kwargs)


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


def device_transfer(cfg, **kwargs):
    _errors(
        errors=dtcli.commands.device.TRANSFER_ARGS.call(
            method=dt.Device.transfer_devices,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_set(cfg, **kwargs):
    _errors(
        errors=dtcli.commands.device_label.SET_ARGS.call(
            method=dt.Device.batch_update_labels,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )


def device_label_remove(cfg, **kwargs):
    _errors(
        errors=dtcli.commands.device_label.REMOVE_ARGS.call(
            method=dt.Device.batch_update_labels,
            **kwargs,
        ),
        cfg=cfg,
        **kwargs,
    )
