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
    _devices([dt.Device.get_device(
        device_id=kwargs['device_id'],
        project_id=kwargs['project_id'],
    )], cfg, **kwargs)


def device_list(cfg, **kwargs) -> None:
    devices = []

    # Allows for `project-id` to be read from stdin.
    project_ids = []
    for entry in dtcli.format.str2list(kwargs['project_ids'], stdin=True):
        if dtcli.format.is_xid(entry):
            project_ids.append(entry)
        else:
            dtcli.format.stderr(f'Invalid project ID "{entry}".')

    # One API call has to be made for each project.
    for project_id in project_ids:
        try:
            devices += dt.Device.list_devices(
                project_id=project_id,
                query=kwargs['query'],
                device_ids=dtcli.format.str2list(kwargs['device_ids']),
                device_types=dtcli.format.str2list(kwargs['device_types']),
                label_filters=dtcli.format.str2dict(kwargs['label_filters']),
            )
        except dt.errors.Forbidden:
            msg = f'could not get devices in project with ID "{project_id}"'
            dtcli.format.stderr(msg)

    _devices(devices, cfg, **kwargs)


def device_transfer(cfg, **kwargs):
    device_ids = []
    for entry in dtcli.format.str2list(kwargs['device_ids'], stdin=True):
        if dtcli.format.is_xid(entry):
            device_ids.append(entry)
        else:
            dtcli.format.stderr(f'Invalid device ID "{entry}".')

    errors = dt.Device.transfer_devices(
        device_ids=device_ids,
        source_project_id=kwargs['source'],
        target_project_id=kwargs['target'],
    )

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


def device_label_set(cfg, **kwargs):
    device_ids = []
    for entry in dtcli.format.str2list(kwargs['device_ids'], stdin=True):
        if dtcli.format.is_xid(entry):
            device_ids.append(entry)
        else:
            dtcli.format.stderr(f'Invalid device ID "{entry}".')

    errors = dt.Device.batch_update_labels(
        device_ids=device_ids,
        project_id=kwargs['project_id'],
        set_labels=dtcli.format.str2dict(kwargs['labels']),
    )

    for err in errors:
        dtcli.format.stderr(err)


def device_label_remove(cfg, **kwargs):
    device_ids = []
    for entry in dtcli.format.str2list(kwargs['device_ids'], stdin=True):
        if dtcli.format.is_xid(entry):
            device_ids.append(entry)
        else:
            dtcli.format.stderr(f'Invalid device ID "{entry}".')

    errors = dt.Device.batch_update_labels(
        device_ids=device_ids,
        project_id=kwargs['project_id'],
        remove_labels=dtcli.format.str2list(kwargs['labels']),
    )

    for err in errors:
        dtcli.format.stderr(err)
