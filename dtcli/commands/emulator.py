from typing import Callable, Any, Dict
from argparse import _SubParsersAction, ArgumentParser

import dtcli
from dtcli.table import Table


def publish_add(subparser: _SubParsersAction,
                common_opts: Callable,
                ) -> ArgumentParser:

    publish_parser = subparser.add_parser(
        name='publish',
        help='publish an event from the emulator device',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    publish_subparser = publish_parser.add_subparsers(
        title='available commands',
        dest='publish',
        metavar=None,
    )

    # -------------
    # publish touch
    touch_parser = publish_subparser.add_parser(
        name='touch',
        help='publish touch event',
    )
    dtcli.args.emulator.PUBLISH_TOUCH.to_parser(touch_parser)
    common_opts(touch_parser)

    # -------------------
    # publish temperature
    temperature_parser = publish_subparser.add_parser(
        name='temperature',
        help='publish temperature event',
    )
    dtcli.args.emulator.PUBLISH_TEMPERATURE.to_parser(temperature_parser)
    common_opts(temperature_parser)

    # ----------------------
    # publish object-present
    object_present_parser = publish_subparser.add_parser(
        name='object-present',
        help='publish objectPresent event',
    )
    dtcli.args.emulator.PUBLISH_OBJECT_PRESENT.to_parser(object_present_parser)
    common_opts(object_present_parser)

    # ----------------
    # publish humidity
    humidity_parser = publish_subparser.add_parser(
        name='humidity',
        help='publish humidity event',
    )
    dtcli.args.emulator.PUBLISH_HUMIDITY.to_parser(humidity_parser)
    common_opts(humidity_parser)

    # ----------------------------
    # publish object-present-count
    object_present_count_parser = publish_subparser.add_parser(
        name='object-present-count',
        help='publish objectPresentCount event',
    )
    dtcli.args.emulator.PUBLISH_OBJECT_PRESENT_COUNT.\
        to_parser(object_present_count_parser)
    common_opts(object_present_count_parser)

    # -------------------
    # publish touch-count
    touch_count_parser = publish_subparser.add_parser(
        name='touch-count',
        help='publish touchCount event',
    )
    dtcli.args.emulator.PUBLISH_TOUCH_COUNT.\
        to_parser(touch_count_parser)
    common_opts(touch_count_parser)

    # ---------------------
    # publish water-present
    water_present_parser = publish_subparser.add_parser(
        name='water-present',
        help='publish waterPresent event',
    )
    dtcli.args.emulator.PUBLISH_WATER_PRESENT.\
        to_parser(water_present_parser)
    common_opts(water_present_parser)

    # ----------------------
    # publish network-status
    network_status_parser = publish_subparser.add_parser(
        name='network-status',
        help='publish networkStatus event',
    )
    dtcli.args.emulator.PUBLISH_NETWORK_STATUS.\
        to_parser(network_status_parser)
    common_opts(network_status_parser)

    # ----------------------
    # publish battery-status
    battery_status_parser = publish_subparser.add_parser(
        name='battery-status',
        help='publish batteryStatus event',
    )
    dtcli.args.emulator.PUBLISH_BATTERY_STATUS.\
        to_parser(battery_status_parser)
    common_opts(battery_status_parser)

    # -------------------------
    # publish connection-status
    connection_status_parser = publish_subparser.add_parser(
        name='connection-status',
        help='publish connectionStatus event',
    )
    dtcli.args.emulator.PUBLISH_CONNECTION_STATUS.\
        to_parser(connection_status_parser)
    common_opts(connection_status_parser)

    # -----------------------
    # publish ethernet-status
    ethernet_status_parser = publish_subparser.add_parser(
        name='ethernet-status',
        help='publish ethernetStatus event',
    )
    dtcli.args.emulator.PUBLISH_ETHERNET_STATUS.\
        to_parser(ethernet_status_parser)
    common_opts(ethernet_status_parser)

    # -----------------------
    # publish cellular-status
    cellular_status_parser = publish_subparser.add_parser(
        name='cellular-status',
        help='publish cellularStatus event',
    )
    dtcli.args.emulator.PUBLISH_CELLULAR_STATUS.\
        to_parser(cellular_status_parser)
    common_opts(cellular_status_parser)

    # -----------
    # publish co2
    co2_parser = publish_subparser.add_parser(
        name='co2',
        help='publish co2 event',
    )
    dtcli.args.emulator.PUBLISH_CO2.\
        to_parser(co2_parser)
    common_opts(co2_parser)

    # ----------------
    # publish pressure
    pressure_parser = publish_subparser.add_parser(
        name='pressure',
        help='publish pressure event',
    )
    dtcli.args.emulator.PUBLISH_PRESSURE.\
        to_parser(pressure_parser)
    common_opts(pressure_parser)

    # --------------
    # publish motion
    motion_parser = publish_subparser.add_parser(
        name='motion',
        help='publish motion event',
    )
    dtcli.args.emulator.PUBLISH_MOTION.\
        to_parser(motion_parser)
    common_opts(motion_parser)

    assert isinstance(publish_parser, ArgumentParser)

    return publish_parser


def add(subparser: _SubParsersAction,
        common_opts: Callable,
        ) -> Dict[str, ArgumentParser]:

    emulator_parser = subparser.add_parser(
        name='emulator',
        help='Interact with the Emulator resource.',
        formatter_class=dtcli.format.SubcommandHelpFormatter,
    )
    emulator_subparser = emulator_parser.add_subparsers(
        title='available commands',
        dest='emulator',
        metavar=None,
    )

    # ---------------
    # emulator create
    create_parser = emulator_subparser.add_parser(
        name='create',
        help='create a new emulated device',
    )
    dtcli.args.emulator.CREATE.to_parser(create_parser)
    common_opts(create_parser)

    # ---------------
    # emulator delete
    delete_parser = emulator_subparser.add_parser(
        name='delete',
        help='delete an emulated device',
    )
    dtcli.args.emulator.DELETE.to_parser(delete_parser)
    common_opts(delete_parser)

    # ----------------
    # emulator publish
    publish_parser = publish_add(
        emulator_subparser,
        common_opts,
    )

    assert isinstance(emulator_parser, ArgumentParser)
    assert isinstance(publish_parser, ArgumentParser)

    return {'emulator': emulator_parser, 'publish': publish_parser}


def do(parsers: Dict[str, ArgumentParser],
       cfg: dict,
       **kwargs: Any,
       ) -> Table:

    if kwargs['emulator'] == 'create':
        return dtcli.resources.emulator.emulator_create(cfg, **kwargs)
    elif kwargs['emulator'] == 'delete':
        return dtcli.resources.emulator.emulator_delete(cfg, **kwargs)
    elif kwargs['emulator'] == 'publish':
        if kwargs['publish'] == 'touch':
            return dtcli.resources.emulator.publish_touch(**kwargs)
        elif kwargs['publish'] == 'temperature':
            return dtcli.resources.emulator.publish_temperature(**kwargs)
        elif kwargs['publish'] == 'object-present':
            return dtcli.resources.emulator.publish_object_present(**kwargs)
        elif kwargs['publish'] == 'object-present-count':
            return dtcli.resources.emulator.\
                publish_object_present_count(**kwargs)
        elif kwargs['publish'] == 'humidity':
            return dtcli.resources.emulator.publish_humidity(**kwargs)
        elif kwargs['publish'] == 'touch-count':
            return dtcli.resources.emulator.publish_touch_count(**kwargs)
        elif kwargs['publish'] == 'water-present':
            return dtcli.resources.emulator.publish_water_present(**kwargs)
        elif kwargs['publish'] == 'network-status':
            return dtcli.resources.emulator.publish_network_status(**kwargs)
        elif kwargs['publish'] == 'battery-status':
            return dtcli.resources.emulator.publish_battery_status(**kwargs)
        elif kwargs['publish'] == 'connection-status':
            return dtcli.resources.emulator.publish_connection_status(**kwargs)
        elif kwargs['publish'] == 'ethernet-status':
            return dtcli.resources.emulator.publish_ethernet_status(**kwargs)
        elif kwargs['publish'] == 'cellular-status':
            return dtcli.resources.emulator.publish_cellular_status(**kwargs)
        elif kwargs['publish'] == 'co2':
            return dtcli.resources.emulator.publish_co2(**kwargs)
        elif kwargs['publish'] == 'pressure':
            return dtcli.resources.emulator.publish_pressure(**kwargs)
        elif kwargs['publish'] == 'motion':
            return dtcli.resources.emulator.publish_motion(**kwargs)
        else:
            print(parsers['publish'].format_help())
    else:
        print(parsers['emulator'].format_help())

    return Table.empty()
