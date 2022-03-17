import disruptive

import dtcli.table


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
