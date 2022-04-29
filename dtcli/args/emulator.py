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
