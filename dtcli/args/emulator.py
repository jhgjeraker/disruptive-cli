import dtcli

CREATE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='device_type',
        flags=['device-type'],
        help='emulated device type',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['--display-name'],
        help='give the device a name',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='labels',
        flags=['--labels'],
        help='comma-separated list of key=value labels',
        format=dtcli.format.str2dict,
    ),
])

DELETE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_TOUCH = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_TEMPERATURE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='celsius',
        flags=['celsius'],
        help='temperature value in Celsius',
        format=dtcli.format.to_float,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_OBJECT_PRESENT = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='state',
        flags=['state'],
        help='either "PRESENT" or "NOT_PRESENT"',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_HUMIDITY = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='celsius',
        flags=['celsius'],
        help='temperature value in Celsius',
        format=dtcli.format.to_float,
    ),
    dtcli.parser.Arg(
        key='relative_humidity',
        flags=['relative-humidity'],
        help='relative humidity in percent',
        format=dtcli.format.to_float,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_OBJECT_PRESENT_COUNT = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='total',
        flags=['total'],
        help='number of state changes',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_TOUCH_COUNT = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='total',
        flags=['total'],
        help='number of state changes',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_WATER_PRESENT = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='state',
        flags=['state'],
        help='either "PRESENT" or "NOT_PRESENT"',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_NETWORK_STATUS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='signal_strength',
        flags=['--signal-strength'],
        help='the percentage signal strength of the strongest cloud connector',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='rssi',
        flags=['--rssi'],
        help='raw signal strength indication of the strongest cloud connector',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='transmission_mode',
        flags=['--transmission-mode'],
        help='either "LOW_POWER_STANDARD_MODE" or "HIGH_POWER_BOOST_MODE"',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_BATTERY_STATUS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target device identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='percentage',
        flags=['percentage'],
        help='remaining battery percentage',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_CONNECTION_STATUS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target cloud connector identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='connection',
        flags=['connection'],
        help='either "ETHERNET", "CELLULAR", or "OFFLINE"',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='available',
        flags=['available'],
        help='comma-separated list of available connections',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_ETHERNET_STATUS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target cloud connector identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='mac_address',
        flags=['mac-address'],
        help='local network interface MAC address',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='ip_address',
        flags=['ip-address'],
        help='cloud connector IP address on the local network',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_CELLULAR_STATUS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target cloud connector identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='signal_strength',
        flags=['signal-strength'],
        help='cloud connector signal strength percentage',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_CO2 = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target cloud connector identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='ppm',
        flags=['ppm'],
        help='concentration in parts per million',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_PRESSURE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target cloud connector identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='pascal',
        flags=['pascal'],
        help='barometric pressure in pascal',
        format=dtcli.format.to_int,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])

PUBLISH_MOTION = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        help='target cloud connector identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='state',
        flags=['state'],
        help='either "MOTION_DETECTED" or "NO_MOTION_DETECTED"',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='timestamp',
        flags=['--timestamp'],
        help='event timestamp',
        metavar='',
        format=dtcli.format.to_string,
    ),
])
