import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def _events(events: list, cfg: dict, **kwargs: dict) -> Table:
    table = Table(
        default_columns=[
            Column('event_id', False),
            Column('event_type', False),
            Column('device_id', True),
            Column('project_id', True),
            Column('data', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )

    table.expand_rows(events)
    table.new_entries(events)

    return table


def list_events(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.event.LIST.reparse(**kwargs)
    if not ok:
        return Table.empty()

    results = dtcli.args.event.LIST.call(
        method=dt.EventHistory.list_events,
        method_args=args,
    )

    return _events(results, cfg, **kwargs)


def stream_events(cfg: dict, **kwargs: dict) -> Table:
    ok, args = dtcli.args.event.STREAM.reparse(**kwargs)
    if not ok:
        return Table.empty()

    stream = dtcli.args.event.STREAM.call(
        method=dt.Stream.event_stream,
        method_args=args,
    )[0]

    table = Table(
        default_columns=[
            Column('event_id', False),
            Column('event_type', False),
            Column('device_id', True),
            Column('project_id', True),
            Column('data', False),
        ],
        cfg=cfg,
        opts=kwargs,
    )

    # Do a workaround to print header immediately.
    if not table.opts['no_header']:
        dtcli.format.stdout(table._resolve_row_func()(None, header=True))
        table.n_rows += 1

    for event in stream:
        table.new_entry(event)

    return table
