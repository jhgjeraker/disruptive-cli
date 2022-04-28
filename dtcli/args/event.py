import dtcli

LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='event_types',
        flags=['--event-types'],
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='start_time',
        flags=['--start-time'],
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='end_time',
        flags=['--end-time'],
        format=dtcli.format.to_string,
    ),
])


STREAM = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='device_ids',
        flags=['--device-ids'],
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='label_filters',
        flags=['--label-filters'],
        format=dtcli.format.str2dict,
    ),
    dtcli.parser.Arg(
        key='device_types',
        flags=['--device-types'],
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='event_types',
        flags=['--event-types'],
        format=dtcli.format.str2list,
    ),
])
