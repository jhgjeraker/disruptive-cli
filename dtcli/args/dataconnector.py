import dtcli

GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='data_connector_id',
        flags=['dataconnector-id'],
        help='target data connector id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])

LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])

CREATE_HTTP_PUSH = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='url',
        flags=['url'],
        help='target url endpoint',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='signature_secret',
        flags=['--signature-secret'],
        help='secret with which each event is signed',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='headers',
        flags=['--headers'],
        help='comma-separated key=value custom headers included in request',
        metavar='',
        format=dtcli.format.str2dict,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['--display-name'],
        help='give the data connector a name',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='status',
        flags=['--status'],
        help='either "ACTIVE" (default) or "USER_DISABLED"',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='event_types',
        flags=['--event-types'],
        help='comma-separated list of event-types to forward',
        metavar='',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='labels',
        flags=['--labels'],
        help='comma-separated list of label keys to include in request',
        metavar='',
        format=dtcli.format.str2list,
    ),
])

UPDATE_HTTP_PUSH = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='data_connector_id',
        flags=['data-connector-id'],
        help='target data connector id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='url',
        flags=['--url'],
        help='target url endpoint',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='signature_secret',
        flags=['--signature-secret'],
        help='secret with which each event is signed',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='headers',
        flags=['--headers'],
        help='comma-separated key=value custom headers included in request',
        metavar='',
        format=dtcli.format.str2dict,
    ),
    dtcli.parser.Arg(
        key='display_name',
        flags=['--display-name'],
        help='give the data connector a name',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='status',
        flags=['--status'],
        help='either "ACTIVE" (default) or "USER_DISABLED"',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='event_types',
        flags=['--event-types'],
        help='comma-separated list of event-types to forward',
        metavar='',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='labels',
        flags=['--labels'],
        help='comma-separated list of label keys to include in request',
        metavar='',
        format=dtcli.format.str2list,
    ),
])

DELETE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='data_connector_id',
        flags=['dataconnector-id'],
        help='target data connector id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])

SYNC = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='data_connector_id',
        flags=['dataconnector-id'],
        help='target data connector id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])

METRICS = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='data_connector_id',
        flags=['dataconnector-id'],
        help='target data connector id',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='target project id',
        format=dtcli.format.to_string,
    )
])
