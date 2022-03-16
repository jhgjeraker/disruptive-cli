import dtcli
import disruptive


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


def _projects(projects: list[disruptive.Project], **kwargs):
    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('id', False),
            dtcli.table.Column('display_name', True),
            dtcli.table.Column('organization_id', False),
            dtcli.table.Column('organization_display_name', True),
            dtcli.table.Column('sensor_count', False),
            dtcli.table.Column('cloud_connector_count', False),
        ],
        opts=kwargs,
    )
    table.expand_rows(projects)
    table.new_entries(projects)


def project(**kwargs):
    _projects([disruptive.Project.get_project(kwargs['project_id'])], **kwargs)


def projects(**kwargs):
    _projects(disruptive.Project.list_projects(
        organization_id=kwargs['organization_id'],
        query=kwargs['query'],
    ), **kwargs)


def history(**kwargs):
    if kwargs['event_types'] is None:
        ignore = [
            disruptive.events.NETWORK_STATUS,
            disruptive.events.ETHERNET_STATUS,
            disruptive.events.CELLULAR_STATUS,
            disruptive.events.BATTERY_STATUS,
            disruptive.events.CONNECTION_STATUS,
        ]
        types = [e for e in disruptive.events.EVENT_TYPES if e not in ignore]
    else:
        types = kwargs['event_types'].split(',')

    history = disruptive.EventHistory.list_events(
        device_id=kwargs['device_id'],
        project_id=kwargs['project_id'],
        event_types=types,
        start_time=kwargs['start_time'],
        end_time=kwargs['end_time'],
    )

    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('event_id', False),
            dtcli.table.Column('event_type', False),
            dtcli.table.Column('device_id', True),
            dtcli.table.Column('project_id', True),
            dtcli.table.Column('data', False),
        ],
        opts=kwargs,
    )

    table.expand_rows(history)
    table.new_entries(history)
