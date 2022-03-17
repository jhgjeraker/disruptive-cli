import disruptive

import dtcli.table


def _devices(devices: list[disruptive.Device], **kwargs):
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('device_id', False),
            dtcli.table.Column('project_id', True),
            dtcli.table.Column('display_name', True),
            dtcli.table.Column('device_type', False),
            dtcli.table.Column('product_number', False),
            dtcli.table.Column('labels', True),
            dtcli.table.Column('is_emulated', True),
        ],
        opts=kwargs,
    )
    table.expand_rows(devices)
    table.new_entries(devices)


def device(**kwargs):
    _devices(disruptive.Device.get_device(
        device_id=kwargs['device_id'],
        project_id=kwargs['project_id'],
    ), **kwargs)


def devices(**kwargs):
    _devices(disruptive.Device.list_devices(
        project_id=kwargs['project_id'],
        query=kwargs['query'],
        device_ids=kwargs['device_ids'],
        device_types=kwargs['device_types'],
        label_filters=kwargs['label_filters'],
    ), **kwargs)
