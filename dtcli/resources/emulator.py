from typing import Any

import disruptive as dt

import dtcli
from dtcli.table import Table, Column


def emulator_create(cfg: dict, **kwargs: Any) -> Table:
    ok, args = dtcli.arguments.emulator.CREATE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    results = dtcli.arguments.emulator.CREATE.call(
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
