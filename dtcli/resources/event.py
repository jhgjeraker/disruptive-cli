import dtcli
import disruptive


def list_events(**kwargs):
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

    args = {
        'device_id': kwargs['device_id'],
        'project_id': kwargs['project_id'],
        'event_types': types if kwargs['event_types'] is None else [
            t for t in kwargs['event_types'].split(',')
        ],
        'start_time': kwargs['start_time'],
        'end_time': kwargs['end_time'],
    }

    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('event_id', False, 20),
            dtcli.table.Column('event_type', False, 15),
            dtcli.table.Column('device_id', False, 23),
            dtcli.table.Column('project_id', True, 20),
            dtcli.table.Column('data', False),
        ],
        opts=kwargs,
    )

    for event in disruptive.EventHistory.list_events(**args):
        table.new_entry(event)


def stream_events(**kwargs):
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

    args = {
        'project_id': kwargs['project_id'],
        'device_ids': None if kwargs['device_ids'] is None else [
            xid for xid in kwargs['device_ids'].split(',')
        ],
        'label_filters': None if kwargs['label_filters'] is None else [
            f for f in kwargs['label_filters'].split(',')
        ],
        'device_types': None if kwargs['device_types'] is None else [
            t for t in kwargs['device_types'].split(',')
        ],
        'event_types': types if kwargs['event_types'] is None else [
            t for t in kwargs['event_types'].split(',')
        ],
    }

    table = dtcli.table.Table(
        default_columns=[
            dtcli.table.Column('event_id', False, 20),
            dtcli.table.Column('event_type', False, 15),
            dtcli.table.Column('device_id', False, 23),
            dtcli.table.Column('project_id', True, 20),
            dtcli.table.Column('data', False),
        ],
        opts=kwargs,
    )

    # Do a workaround to print header immediately.
    if not table.opts['no_header']:
        dtcli.format.stdout(table._resolve_row_func()(None, header=True))
        table.row_count += 1

    for event in disruptive.Stream.event_stream(**args):
        table.new_entry(event)