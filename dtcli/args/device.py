import dtcli


GET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_id',
        flags=['device-id'],
        xid=True,
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['--project-id'],
        xid=True,
        metavar='',
        format=dtcli.format.to_string,
    )
])

LIST = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        xid=True,
        help='identifier of owning project',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='query',
        flags=['--query'],
        help='keyword-based device search',
        metavar='',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='device_ids',
        flags=['--device-ids'],
        metavar='',
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='device_types',
        flags=['--device-types'],
        metavar='',
        help='comma-separated device types',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='label_filters',
        flags=['--label-filters'],
        metavar='',
        help='comma-separated key=value labels',
        format=dtcli.format.str2dict,
    )
])

TRANSFER = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_ids',
        flags=['device-ids'],
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='source_project_id',
        flags=['source-project-id'],
        help='source project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='target_project_id',
        flags=['target-project-id'],
        help='target project identifier',
        format=dtcli.format.to_string,
    ),
])

LABEL_SET = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_ids',
        flags=['device-ids'],
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='identifier of owning project',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='set_labels',
        flags=['labels'],
        help='comma-separated key=value labels',
        format=dtcli.format.str2dict,
    ),
])

LABEL_REMOVE = dtcli.parser.CmdArgs([
    dtcli.parser.Arg(
        key='device_ids',
        flags=['device-ids'],
        help='comma-separated device identifiers',
        format=dtcli.format.str2list,
    ),
    dtcli.parser.Arg(
        key='project_id',
        flags=['project-id'],
        help='owning project identifier',
        format=dtcli.format.to_string,
    ),
    dtcli.parser.Arg(
        key='remove_labels',
        flags=['labels'],
        help='comma-separated label keys',
        format=dtcli.format.str2list,
    ),
])
