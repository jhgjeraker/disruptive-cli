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


def publish_touch(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_TOUCH.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Touch that is injected into args.
    data_args = {}
    for key in ['timestamp']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Touch(**data_args)

    dtcli.args.emulator.PUBLISH_TOUCH.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_temperature(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_TEMPERATURE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Temperature that is injected into args.
    data_args = {}
    for key in ['timestamp', 'celsius']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Temperature(**data_args)

    dtcli.args.emulator.PUBLISH_TEMPERATURE.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_object_present(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_OBJECT_PRESENT.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of ObjectPresent that is injected into args.
    data_args = {}
    for key in ['timestamp', 'state']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.ObjectPresent(**data_args)

    dtcli.args.emulator.PUBLISH_OBJECT_PRESENT.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_object_present_count(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.\
        PUBLISH_OBJECT_PRESENT_COUNT.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of ObjectPresentCount that is injected into args.
    data_args = {}
    for key in ['timestamp', 'total']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.ObjectPresentCount(**data_args)

    dtcli.args.emulator.PUBLISH_OBJECT_PRESENT_COUNT.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_humidity(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_HUMIDITY.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Humidity that is injected into args.
    data_args = {}
    for key in ['timestamp', 'celsius', 'relative_humidity']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Humidity(**data_args)

    dtcli.args.emulator.PUBLISH_HUMIDITY.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_touch_count(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_TOUCH_COUNT.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of TouchCount that is injected into args.
    data_args = {}
    for key in ['timestamp', 'total']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.TouchCount(**data_args)

    dtcli.args.emulator.PUBLISH_TOUCH_COUNT.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_water_present(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_WATER_PRESENT.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of WaterPresent that is injected into args.
    data_args = {}
    for key in ['timestamp', 'state']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.WaterPresent(**data_args)

    dtcli.args.emulator.PUBLISH_WATER_PRESENT.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_network_status(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_NETWORK_STATUS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of NetworkStatus that is injected into args.
    data_args = {}
    for key in [
            'timestamp', 'signal_strength', 'rssi',
            'transmission_mode',
    ]:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)

    args['data'] = dt.events.NetworkStatus(**data_args)

    dtcli.args.emulator.PUBLISH_NETWORK_STATUS.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_battery_status(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_BATTERY_STATUS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of BatteryStatus that is injected into args.
    data_args = {}
    for key in ['timestamp', 'percentage']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.BatteryStatus(**data_args)

    dtcli.args.emulator.PUBLISH_BATTERY_STATUS.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_connection_status(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_CONNECTION_STATUS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of ConnectionStatus that is injected into args.
    data_args = {}
    for key in ['timestamp', 'connection', 'available']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.ConnectionStatus(**data_args)

    dtcli.args.emulator.PUBLISH_CONNECTION_STATUS.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_ethernet_status(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_ETHERNET_STATUS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of EthernetStatus that is injected into args.
    data_args = {}
    for key in ['timestamp', 'mac_address', 'ip_address']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.EthernetStatus(**data_args)

    dtcli.args.emulator.PUBLISH_ETHERNET_STATUS.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_cellular_status(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_CELLULAR_STATUS.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of CellularStatus that is injected into args.
    data_args = {}
    for key in ['timestamp', 'signal_strength']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.CellularStatus(**data_args)

    dtcli.args.emulator.PUBLISH_CELLULAR_STATUS.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_co2(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_CO2.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Co2 that is injected into args.
    data_args = {}
    for key in ['timestamp', 'ppm']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Co2(**data_args)

    dtcli.args.emulator.PUBLISH_CO2.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_pressure(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_PRESSURE.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Pressure that is injected into args.
    data_args = {}
    for key in ['timestamp', 'pascal']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Pressure(**data_args)

    dtcli.args.emulator.PUBLISH_PRESSURE.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()


def publish_motion(**kwargs: Any) -> Table:
    ok, args = dtcli.args.emulator.PUBLISH_MOTION.reparse(**kwargs)
    if not ok:
        return Table.empty()

    # Create an instance of Motion that is injected into args.
    data_args = {}
    for key in ['timestamp', 'state']:
        if key in args:
            data_args[key] = args[key]
            args.pop(key)
    args['data'] = dt.events.Motion(**data_args)

    dtcli.args.emulator.PUBLISH_MOTION.call(
        method=dt.Emulator.publish_event,
        method_args=args
    )

    return Table.empty()
