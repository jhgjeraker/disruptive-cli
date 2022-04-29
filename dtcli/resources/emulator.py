from typing import Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def emulator_create(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.CREATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    results = dtcli.args.emulator.CREATE.call(
        method=dt.Emulator.create_device,
        method_args=args,
    )

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
    table.expand_rows(results)
    table.new_entries(results)

    return table


def emulator_delete(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.DELETE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    dtcli.args.emulator.DELETE.call(
        method=dt.Emulator.delete_device,
        method_args=args,
    )

    return Table.empty()


def publish_touch(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_TOUCH.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Touch that is injected into args.
    touch_args = {}
    for key in ['timestamp']:
        if key in args:
            touch_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Touch(**touch_args)

    dtcli.args.emulator.PUBLISH_TOUCH.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()
